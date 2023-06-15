import datetime
import math
import os

import pandas as pd
import pymysql
import requests
from lxml import etree


# obj工具类
class ObjUtils():
    @staticmethod
    def isEmpty(obj):
        if obj is None:
            return True
        if isinstance(obj, int) or isinstance(obj, float):
            return math.isnan(obj)
        if isinstance(obj, str):
            return len(obj) == 0 or obj.isspace()
        if isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, dict):
            return len(obj) == 0
        return False

    @staticmethod
    def isNotEmpty(obj):
        return not ObjUtils.isEmpty(obj)


# 字符串工具类
class StrUtils():
    @staticmethod
    def joinUnderline(*vals):
        return "_".join(vals)

    @staticmethod
    def wrap(origin, symbol):
        return symbol + origin + symbol

    @staticmethod
    def formatBatch(str_template, lists):
        """
        通过文件批量生成字符串
        :param str_template: 带占位符的字符串
        :param lists: 元素为字典类型的列表
        """
        str_list = list(map(lambda row: str_template.format(**row), lists))
        print('formatBatch列表容量=%s' % len(str_list))
        return str_list


# 日期工具类
class DateUtils():
    # 默认时间格式
    DEFAULT_FORMAT = '%Y-%m-%d %H:%M:%S'
    # 到天的时间格式
    DAY_FORMAT = '%Y-%m-%d'
    # 时间戳格式（天）
    TIMESTAMP_DAY_FORMAT = '%Y%m%d'
    # 时间戳格式（秒）
    TIMESTAMP_SECONDS_FORMAT = '%Y%m%d%H%M%S'
    # 时间戳格式（微秒）
    TIMESTAMP_MICROSECONDS_FORMAT = '%Y%m%d%H%M%S%f'

    @staticmethod
    def str2Date(date_string: str):
        return datetime.datetime.strptime(date_string, DateUtils.DEFAULT_FORMAT)

    @staticmethod
    def date2Str(date_object, format: str = DEFAULT_FORMAT):
        return date_object.strptime(format)

    @staticmethod
    def getNowTime():
        return datetime.datetime.now()

    @staticmethod
    def getNowTimeStr(format: str = DEFAULT_FORMAT):
        return datetime.datetime.now().strftime(format)

    @staticmethod
    def getNowTimestamp(format: str = TIMESTAMP_MICROSECONDS_FORMAT):
        return datetime.datetime.now().strftime(format)

    @staticmethod
    def getTimeDiffMs(start_time, end_time):
        subtract_time = end_time - start_time
        return subtract_time.microseconds // 1000


# http工具类
class HttpUtils():
    @staticmethod
    def get(url, params=None, headers=None, encoding=None) -> str:
        return HttpUtils.doInvoke('get', url, params=params, headers=headers, encoding=encoding)

    @staticmethod
    def post(url, params=None, data=None, headers=None, encoding=None) -> str:
        return HttpUtils.doInvoke('get', url, params=params, data=data, headers=headers, encoding=encoding)

    @staticmethod
    def doInvoke(method, url, params=None, data=None, headers=None, encoding=None) -> str:
        start_time = datetime.datetime.now()
        response = requests.request(method, url, params=params, data=data, headers=headers, timeout=10)
        if response.status_code != 200:
            raise RuntimeError("错误码: " + str(response.status_code) + ', 错误信息: ' + response.reason)
        end_time = datetime.datetime.now()
        content = response.content if encoding is None else response.content.decode(encoding)
        print('请求完成，耗时=%sms，url=%s，content=\n%s' % (DateUtils.getTimeDiffMs(start_time, end_time), url, content))
        return content


# 爬虫工具类
class SpiderUtils():
    def doCrawling(url, encoding=None) -> etree._Element | None:
        """
        爬取网页
        :param url: 网页url
        :param encoding: 解析网页的编码
        :return 文档对象
        """
        content = HttpUtils.get(url, encoding=encoding)
        if content is not None:
            return etree.HTML(content)


# 数据库工具
class DB():
    _db_conn = None
    _env = None

    def __init__(self, env='local') -> None:
        env_maps = {
            "local": ['127.0.0.1', 3306, 'test', 'root', 'root3306'],
            "dev": ['127.0.0.1', 3306, 'dev', 'root', 'root3306']
        }
        conf = env_maps.get(env)
        if not conf:
            raise RuntimeError('没有%s环境' % env)
        self._env = env
        self._db_conn = pymysql.connect(host=conf[0], port=conf[1], database=conf[2], user=conf[3], password=conf[4])

    def query(self, sql, args=None) -> list:
        cursor = self._db_conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql, args)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def execute(self, sql, args=None, auto_commit=True) -> int:
        cursor = self._db_conn.cursor()
        affect_number = cursor.execute(sql, args)
        if auto_commit:
            self.commit()
        cursor.close()
        return affect_number

    def commit(self):
        self._db_conn.commit()
        print('事务已提交')

    def rollback(self, e):
        self._db_conn.rollback()
        print('事务已回滚，异常信息如下：')
        print(e)

    def __del__(self):
        """
        对象销毁的时候调用此方法，关闭数据库连接
        """
        if self._db_conn:
            self._db_conn.close()
            print('%s数据库连接已关闭' % self._env)

    @staticmethod
    def migrate(originEnv, targetEnv, tableName, condition='1=1', excludeColumns=[]):
        start = datetime.datetime.now()
        # 获取待迁移的数据
        originDb = DB(originEnv)
        originQuerySql = 'select * from %s where %s' % (tableName, condition)
        originCursor = originDb._db_conn.cursor(cursor=pymysql.cursors.DictCursor)
        originCursor.execute(originQuerySql)
        originRowDatas = originCursor.fetchall()
        # 遍历所有行，一行一行插入
        targetDb = DB(targetEnv)
        try:
            for originRowData in originRowDatas:
                # 过滤掉值为空以及制定排除的列
                effectColumns = tuple(
                    filter(lambda item: item[1] is not None and item[0] not in excludeColumns, originRowData.items()))
                # 列名前后加反引号
                columns = [StrUtils.wrap(k, '`') for k, v in effectColumns]
                # 非数字类型的加单引号
                values = [str(v) if isinstance(v, (int, float)) else StrUtils.wrap(v, "'") for k, v in effectColumns]
                # 组装插入语句
                targetInsertSql = 'insert into %s (%s) values (%s)' % (tableName, ','.join(columns), ','.join(values))
                print(targetInsertSql)
                targetDb.execute(targetInsertSql, auto_commit=False)
            targetDb.commit()
            end = datetime.datetime.now()
            cost = DateUtils.getTimeDiffMs(start, end)
            print('数据迁移完成，%s->%s，总共%s行，总共耗时：%s秒' % (originEnv, targetEnv, len(originRowDatas), cost))
        except Exception as e:
            targetDb.rollback(e)


# excel、csv工具类
class ExcelUtils():

    @staticmethod
    def create(fileName, datas, headers=None, fileType='xlsx'):
        """
        创建excel表格
        :param fileName: 文件名称
        :param datas: 表格所有数据
        :param headers: 表格的表头
        :param fileType 文件类型，默认xlsx
        """
        filePath = getDestopPath(fileName + "_" + DateUtils.getNowTimestamp() + "." + fileType)
        print('准备创建表格...路径=%s' % filePath)
        df = pd.DataFrame(data=datas, columns=headers)
        if fileType == 'xlsx' or fileType == 'xls':
            df.to_excel(filePath, index=False)
        else:
            df.to_csv(filePath, index=False)
        print('创建表格完成，共%s行，%s' % (str(len(datas)), filePath))

    @staticmethod
    def readAsList(filePath, sheetIndex=0, rowFilter=None):
        """
        读取excel表格
        :param filePath: 完整的文件路径名
        :param sheetIndex: sheet名称或者下标
        :param rowFilter: 过滤的函数
        """
        print('表格读取中...路径=%s' % filePath)
        if filePath.endswith('xlsx') or filePath.endswith('xls'):
            df = pd.read_excel(filePath, sheet_name=sheetIndex, dtype='str')
        else:
            df = pd.read_csv(filePath, low_memory=True, dtype='str')
        rows = df.to_dict(orient='records')
        datas = list(filter(lambda row: rowFilter is None or rowFilter(row), rows))
        total = len(rows)
        count = len(datas)
        print('表格读取完成，共%s行，过滤掉%s行，最终剩下%s行，%s' % (total, (total - count), count, filePath))
        return datas

    @staticmethod
    def readAsKvStr(filePath, sheetIndex=0, rowFilter=None, keyCols=None, valCols=None):
        """
        读取excel表格，将某几列作为key和value，组装成字典
        :param filePath: 完整的文件路径名
        :param sheetIndex: sheet名称
        :param rowFilter: 过滤的函数
        :param keyCols key的列名集合
        :param valCols value的列名集合
        """
        rows = ExcelUtils.readAsList(filePath, sheetIndex, rowFilter=rowFilter)
        dicts = {}
        for row in rows:
            key = StrUtils.joinUnderline(*map(lambda keyColName: row.get(keyColName), keyCols))
            value = StrUtils.joinUnderline(*map(lambda valColName: row.get(valColName), valCols))
            dicts[key] = value
        print('readExcelAsKvStr字典容量=%s' % len(dicts))
        return dicts

    @staticmethod
    def readAsDictDistinct(filePath, sheetIndex=0, keyCols=None, rowFilter=None):
        """
        读取excel表格，将某几列作为key，整行数据作为value，组装成字典，注意后面的会覆盖前面的
        :param filePath: 完整的文件路径名
        :param sheetIndex: sheet名称
        :param keyCols: 字典的key的列名
        :param rowFilter: 过滤的函数
        """
        rows = ExcelUtils.readAsList(filePath, sheetIndex, rowFilter=rowFilter)
        dicts = {StrUtils.joinUnderline(*map(lambda keyColName: row.get(keyColName), keyCols)): row for row in rows}
        print('readExcelAsDictDistinct字典容量=%s' % len(dicts))
        return dicts

    @staticmethod
    def readAsDictGroupby(filePath, sheetIndex=0, keyCols=None, rowFilter=None):
        """
        读取excel表格，将某几列作为key，整行数据作为value-list，组装成字典，后面的不会覆盖前面的
        :param filePath: 完整的文件路径名
        :param sheetIndex: sheet名称
        :param keyCols: 字典的key的列名集合
        :param rowFilter: 过滤的函数
        """
        rows = ExcelUtils.readAsList(filePath, sheetIndex, rowFilter=rowFilter)
        dicts = {}
        for row in rows:
            key = StrUtils.joinUnderline(*map(lambda keyColName: row.get(keyColName), keyCols))
            if key in dicts:
                dicts[key].extend([row])
            else:
                dicts[key] = [row]
        print('readExcelAsDictGroupby字典容量=%s' % len(dicts))
        return dicts

    @staticmethod
    def splitListAndCreate(datas, size, fileName):
        """
        将一个大的字典列表按固定size分割成若干个小列表，每个表列表生成一个excel
        :param datas: 列表
        :param size: 固定长度
        :param fileName: 文件名
        :return excel文件
        """
        lists = ListUtils.split(datas, size)
        for i in range(len(lists)):
            ExcelUtils.create(StrUtils.joinUnderline(fileName, str(i + 1)), lists[i])


# 文本文件工具类
class TextUtils():
    @staticmethod
    def create(fileName, lineContents, fileType='sql'):
        """
        创建文本文件
        :param fileName: 文件名
        :param lineContents: 每一行内容
        :param fileType: 创建文件的类型
        """
        filePath = getDestopPath(fileName + "_" + DateUtils.getNowTimestamp() + "." + fileType)
        print('准备创建文本...路径=%s' % filePath)
        with open(filePath, 'w') as f:
            f.write('\n'.join(lineContents))
        print('创建文本完成，共%s行，路径=%s' % (filePath, str(len(lineContents))))

    @staticmethod
    def read(filePath) -> str:
        """
        读取文本文件，返回一个完整的字符串
        :param filePath: 文件完整路径名
        :return 文件内容
        """
        with open(filePath, 'r', encoding='utf-8') as f:
            return f.read()

    @staticmethod
    def readAsList(filePath) -> list:
        """
        读取文本文件，每一行作为集合的一个元素
        :param filePath: 文件完整路径名
        :return 文件内容
        """
        print('文本读取中...路径=%s' % filePath)
        rows = []
        with open(filePath, 'r', encoding='utf-8') as f:
            for line in f:
                rows.append(line)
        print('文本读取完成，共%s行，路径=%s' % (len(rows), filePath))
        return rows


class ListUtils():
    @staticmethod
    def split(dataList, size):
        """
        将一个大的列表按固定size分割成若干个小列表
        :param dataList: 列表
        :param size: 固定长度
        :return 包含若干个小列表的列表
        """
        total = len(dataList)
        count, mod = divmod(total, size)
        if mod > 0:
            count += 1
        return [dataList[i * size:(i + 1) * size] for i in range(count)]


# 获取桌面路径
def getDestopPath(filename):
    return os.path.join(os.path.expanduser("~"), 'Desktop') + '\\' + filename


# 获取默认下载路径
def getDownloadPath(filename):
    return os.path.join(os.path.expanduser("~"), 'Downloads') + '\\' + filename


if __name__ == '__main__':
    # print(ExcelUtils.readAsDictGroupby(getDestopPath('次新股_20230609.xlsx'), keyCols=['名称', '代码']))
    # db = DB()
    # rownumber = db.execute("update t_user set password='1234567' where id>1")
    # print(rownumber)
    DB.migrate('local', 'dev', 't_user', excludeColumns=['password'])

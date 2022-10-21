import datetime
import random
import warnings

import bs4
import pandas as pd
import requests
from bs4 import BeautifulSoup, GuessedAtParserWarning

# 默认时间格式
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# 时间戳格式（天）
TIMESTAMP_DAY_FORMAT = '%Y%m%d'
# 时间戳格式（秒）
TIMESTAMP_SECONDS_FORMAT = '%Y%m%d%H%M%S'
# 时间戳格式（微秒）
TIMESTAMP_MICROSECONDS_FORMAT = '%Y%m%d%H%M%S%f'


def isEmpty(obj):
    if obj is None:
        return True
    if obj != obj:
        return True
    if isinstance(obj, str):
        return len(obj) == 0 or obj.isspace()
    return False


def isNotEmpty(obj):
    return not isEmpty(obj)


def getDestopPath(filename):
    return 'C:\\Users\\19105\\Desktop\\' + filename


def str2Date(date_string: str):
    return datetime.datetime.strptime(date_string=date_string, format=DEFAULT_DATE_FORMAT)


def date2Str(date_object, format: str = DEFAULT_DATE_FORMAT):
    return date_object.strptime(format)


def getNowTime():
    return datetime.datetime.now()


def getNowDateStr(format: str = DEFAULT_DATE_FORMAT):
    return datetime.datetime.now().strftime(format)


def getNowTimestamp(format: str = TIMESTAMP_MICROSECONDS_FORMAT):
    return datetime.datetime.now().strftime(format)


def getTimeDiffMs(start_time, end_time):
    subtract_time = end_time - start_time
    return subtract_time.microseconds // 1000


def doHttpGet(url, params=None, retryTimes=0, encoding=None):
    """
    http的get请求
    :param url: 网页url
    :param params: url参数
    :param retryTimes: 重试次数
    :param encoding: 解析网页的编码
    :return 文档对象
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    proxies = [
        {'http': '220.173.37.128:7890'},
        {'http': '118.180.166.195:8060'},
        {'http': '120.26.160.120:7890'},
    ]
    exeptions = []
    response_body = None
    start_time = datetime.datetime.now()
    for i in range(retryTimes + 1):
        if (i > 0):
            print("准备重试第%s次..." % i)
        proxy = proxies[random.randint(0, len(proxies) - 1)]
        try:
            response = requests.get(url, params=params, headers=headers, proxies=proxy, timeout=10)
            if response.status_code != 200:
                raise RuntimeError("code: " + str(response.status_code) + ', message: ' + response.reason)
            response_body = response.content if encoding is None else response.content.decode(encoding)
            break
        except Exception as e:
            exeptions.append(e)
    if len(exeptions) == retryTimes + 1:
        print('请求异常：', exeptions)
    end_time = datetime.datetime.now()
    print('请求完成，耗时=%sms，url=%s' % (getTimeDiffMs(start_time, end_time), url))
    return response_body


def crawlWebPage(url, retryTimes=1, encoding=None) -> BeautifulSoup | None:
    """
    爬取网页
    :param url: 网页url
    :param retryTimes: 重试次数
    :param encoding: 解析网页的编码
    :return 文档对象
    """
    html = doHttpGet(url, retryTimes=retryTimes, encoding=encoding)
    if html is not None:
        warnings.filterwarnings('ignore', category=GuessedAtParserWarning)
        return bs4.BeautifulSoup(html, parser='html.parser')


def createExcel(fileName, datas, headers=None, fileType='xlsx'):
    """
    创建excel表格
    :param fileName: 文件名称
    :param datas: 表格所有数据
    :param headers: 表格的表头
    """
    df = pd.DataFrame(data=datas, columns=headers)
    filePath = getDestopPath(fileName + "_" + getNowTimestamp(TIMESTAMP_DAY_FORMAT) + "." + fileType)
    if fileType == 'xlsx' or fileType == 'xls':
        df.to_excel(filePath, index=False)
    else:
        df.to_csv(filePath, index=False)
    print('创建表格完成，共%s行，%s' % (str(len(datas)), filePath))


def readExcelAsList(filePath, sheetName='Sheet1', filterFunction=None):
    """
    读取excel表格
    :param filePath: 完整的文件路径名
    :param sheetName: sheet名称
    :param filterFunction: 过滤的函数
    """
    if filePath.endswith('xlsx') or filePath.endswith('xls'):
        df = pd.read_excel(filePath, sheet_name=sheetName, dtype='str')
    else:
        df = pd.read_csv(filePath, low_memory=True, dtype='str')
    datas, total, filter_count = _transfer_dataframe_and_filter(df, filterFunction)
    print('表格读取完成，共%s行，过滤掉%s行，最终剩下%s行，%s' % (total, filter_count, str(len(datas)), filePath))
    return datas


def readExcelAsKvStr(filePath, sheetName='Sheet1', filterFunction=None, keyCols=None, valCols=None):
    """
    读取excel表格，结果为字典类型，key和value都是字符串
    :param filePath: 完整的文件路径名
    :param sheetName: sheet名称
    :param filterFunction: 过滤的函数
    :param keyCols key的列名
    :param valCols value的列名
    """
    lists = readExcelAsList(filePath, sheetName, filterFunction=filterFunction)
    dicts = _transfer_data_to_kv_str(lists, keyCols, valCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def readExcelAsDictDistinct(filePath, sheetName='Sheet1', keyCols=None, filterFunction=None):
    """
    读取excel表格，结果为字典类型，注意后面的会覆盖前面的
    :param filePath: 完整的文件路径名
    :param sheetName: sheet名称
    :param keyCols: 字典的key的列名
    :param filterFunction: 过滤的函数
    """
    lists = readExcelAsList(filePath, sheetName, filterFunction=filterFunction)
    dicts = _transfer_data_to_dict_distinct(lists, keyCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def readExcelAsDictGroupby(filePath, sheetName='Sheet1', keyCols=None, filterFunction=None):
    """
    读取excel表格，结果为字典类型，按指定列分组
    :param filePath: 完整的文件路径名
    :param sheetName: sheet名称
    :param keyCols: 字典的key的列名
    :param filterFunction: 过滤的函数
    """
    lists = readExcelAsList(filePath, sheetName, filterFunction=filterFunction)
    dicts = _transfer_data_to_dict_groupby(lists, keyCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def createTextFile(fileName, lineContents, fileType='txt'):
    """
    创建文本文件
    :param fileName: 文件名
    :param lineContents: 所有行内容
    """
    filePath = getDestopPath(fileName + "_" + getNowTimestamp(TIMESTAMP_DAY_FORMAT) + "." + fileType)
    with open(filePath, 'w') as f:
        f.write('\n'.join(lineContents))
    print('创建文本完成，共%s行，%s' % (filePath, str(len(lineContents))))


def readTextFileAsList(filePath, filterFunction=None, sep=','):
    """
    读取文本文件，结果为集合类型，每个元素是字典类型，要求第一行是表头
    :param filePath: 完整的文件路径名
    :param filterFunction: 过滤的函数
    """
    rows = []
    with open(filePath, 'r', encoding='utf-8') as f:
        for line in f:
            rows.append(line)
    lists = []
    headers = rows[0].split(sep)
    filter_count = 0
    for i in range(1, len(rows)):
        row_data = rows[i].split(sep)
        dicts = {}
        for j in range(len(headers)):
            # 去掉前后空格、换行符、单引号、双引号
            headerName = headers[j].strip().replace("'", '').replace('"', '')
            value = row_data[j].strip().replace("'", '').replace('"', '')
            dicts[headerName] = value
        if filterFunction is None or filterFunction(row_data):
            lists.append(dicts)
        else:
            filter_count += 1
    print('文本读取完成，共%s行，过滤掉%s行，最终剩下%s行，%s' % (len(rows), filter_count, str(len(lists)), filePath))
    return lists


def readTextFileAsKvStr(filePath, filterFunction=None, keyCols=None, valCols=None):
    """
    读取文本文件，结果为字典类型，key和value都是字符串
    :param filePath: 完整的文件路径名
    :param filterFunction: 过滤的函数
    :param keyCols key的列名
    :param valCols value的列名
    """
    lists = readTextFileAsList(filePath, filterFunction=filterFunction)
    dicts = _transfer_data_to_kv_str(lists, keyCols, valCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def readTextFileAsDictDistinct(filePath, keyCols=None, filterFunction=None, sep=','):
    """
    读取文本文件，结果为字典类型，注意后面的会覆盖前面的，要求第一行是表头
    :param filePath: 完整的文件路径名
    :param keyCols: 字典的key的列名
    :param filterFunction: 过滤的函数
    """
    datas = readTextFileAsList(filePath, filterFunction=filterFunction, sep=sep)
    dicts = _transfer_data_to_dict_distinct(datas, keyCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def readTextFileAsDictGroupby(filePath, keyCols=None, filterFunction=None, sep=','):
    """
    读取文本文件，结果为字典类型，按指定列分组，要求第一行是表头
    :param filePath: 完整的文件路径名
    :param keyCols: 字典的key的列名
    :param filterFunction: 过滤的函数
    """
    datas = readTextFileAsList(filePath, filterFunction=filterFunction, sep=sep)
    dicts = _transfer_data_to_dict_groupby(datas, keyCols)
    print('字典容量=%s' % len(dicts))
    return dicts


def generateBatchStr(str_template, lists):
    """
    通过文件批量生成字符串
    :param str_template: 带占位符的字符串
    :param lists: 元素为字典类型的列表
    """
    str_list = list(map(lambda row: str_template.format(**row), lists))
    print('列表容量=%s' % len(str_list))
    return str_list


def generateBatchStrFromFile(str_template, filePath, sheetName='Sheet1', filterFunction=None, sep=','):
    """
    通过文件批量生成字符串
    :param str_template: 带占位符的字符串
    :param filePath: 完整的文件路径名
    :param sheetName: sheet名称
    :param filterFunction: 过滤的函数
    :param sep: 文本内容的分隔符
    """
    if filePath.endswith('.xlsx') or filePath.endswith('.xls') or filePath.endswith('.csv'):
        lists = readExcelAsList(filePath, sheetName, filterFunction)
    else:
        lists = readTextFileAsList(filePath, sep, filterFunction)
    return generateBatchStr(str_template, lists)


def _transfer_dataframe_and_filter(df: pd.DataFrame, filterFunction=None):
    columns = df.columns
    values = df.values
    datas = []
    filter_count = 0
    for rowNum in range(len(values)):
        rowData = {}
        for colNum in range(len(columns)):
            val = values[rowNum][colNum]
            val = '' if isEmpty(val) else val
            rowData[columns[colNum]] = val
        if filterFunction is None or filterFunction(rowData):
            datas.append(rowData)
        else:
            filter_count += 1
    return datas, len(values), filter_count


def _transfer_data_to_kv_str(datas, keyCols, valCols):
    dicts = {}
    for row in datas:
        key = '_'.join(map(lambda keyColName: row[keyColName], keyCols))
        value = '_'.join(map(lambda valColName: row[valColName], valCols))
        dicts[key] = value
    return dicts


def _transfer_data_to_dict_distinct(datas, keyCols):
    dicts = {}
    for row in datas:
        key = '_'.join(map(lambda keyColName: row[keyColName], keyCols))
        dicts[key] = row
    return dicts


def _transfer_data_to_dict_groupby(datas, keyCols):
    dicts = {}
    for row in datas:
        key = '_'.join(map(lambda keyColName: row[keyColName], keyCols))
        if key in dicts:
            dicts[key] = dicts[key] + [row]
        else:
            dicts[key] = [row]
    return dicts


if __name__ == '__main__':
    # doc = crawl_web_page('https://github.com/nluedtke/linux_kernel_cves/blob/master/data/4.1/4.1_CVEs.txt',
    #                      retryTimes=3)
    # create_excel('test', [[1, 2], [3, 4]], ['age', 'aaa'])
    # print(read_excel(get_destop_path('test_20221015.xlsx'), filterFunction=lambda row: row['name'] =='java编程基础'))
    # print(doc)
    # data = readExcelAsList(get_destop_path('tb_book.csv'))
    # print(data)
    # createExcel('ceshi2', [['123', '您好']], headers=['age', '姓名'], fileType='xls')
    data = readTextFileAsList(getDestopPath('tb_book.txt'))
    # print(data)
    # createTextFile('ces', ['123', '哈哈'])
    # print(readExcelAsKvStr(getDestopPath('tb_book.csv'), keyCols=['id'], valCols=['name']))
    # print(generateBatchStr('select {name} from dual',[{'name':'zhangsan'},{'name':'lisi'}]))
    # print(generateBatchStr('select {name} from dual', [{'name': 'zhangsan'}, {'name': 'lisi'}]))
    print(generateBatchStrFromFile('select {name} from dual', getDestopPath('tb_book.csv')))

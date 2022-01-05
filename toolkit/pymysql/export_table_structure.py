"""
mysql导出表结构
"""
import datetime

import xlwt

from mysql_utils import *

select_table_structure_sql = """
select
	c.table_name table_name,
	t.table_comment table_comment,
	c.column_name column_name,
	c.data_type data_type,
	c.is_nullable is_nullable,
	c.column_comment column_comment,
	c.column_key column_key
from
	information_schema.`COLUMNS` c,
	information_schema.`TABLES` t
where
	c.table_name = t.table_name
	and c.table_schema = '%s'
	and t.table_schema = '%s'
	and t.table_name in %s
order by
	c.table_name,
	c.ordinal_position;
"""


def getHeaderStyle():
    """
    表头样式
    """
    font = xlwt.Font()
    font.bold = True  # 字体加粗
    font.height = 12 * 20  # 12号字体
    font.name = '微软雅黑'

    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 50  # 背景颜色

    style = xlwt.XFStyle()
    style.font = font
    style.pattern = pattern
    return style


def getMergeRowStyle():
    """
    合并行的样式
    """
    font = xlwt.Font()
    font.bold = True  # 字体加粗

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 垂直居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 水平居中
    alignment.wrap = 1  # 自动换行

    style = xlwt.XFStyle()
    style.font = font
    style.alignment = alignment
    return style


def filterByTableName(tableName, allTableColumns):
    """
    通过表名过滤，获取对应的列信息集合
    :param tableName: 表名
    :param allTableColumns: 多个表列信息集合
    :return: 表名的列信息集合
    """
    table_columns = []
    for column in allTableColumns:
        if column['table_name'] == tableName:
            table_columns.append(column)
    table_name_and_comment = '{}\n({})'.format(table_columns[0]['table_name'], table_columns[0]['table_comment'])
    return table_name_and_comment, table_columns


def export_table_structure(targetDbName, sheet_tables_config, headers, save_file_path):
    """
    导出表结构
    :param targetDbName: 数据库
    :param sheet_tables_config: sheet页和对应表名
    :param headers: 表头
    :param save_file_path: 保存文件的路径
    """
    # 获取数据库连接
    db_connection = get_db(targetDbName)
    dictcursor = get_dictcursor(db_connection)
    dbName = db_connection.db.decode('utf-8')
    # 创建excel
    wb = xlwt.Workbook()
    for sheetName in sheet_tables_config:
        tableNames = sheet_tables_config[sheetName]
        sheet = wb.add_sheet(sheetName)
        # 生成表头
        for i in range(len(headers)):
            sheet.col(i).width = 200 * 40
            sheet.write(0, i, headers[i], getHeaderStyle())
        # 查询表结构
        dictcursor.execute(select_table_structure_sql % (dbName, dbName, str(tableNames)))
        allTableColumns = dictcursor.fetchall()
        row_num_index = 1
        for tableName in tableNames:
            # 获取表的所有列信息
            table_name_and_comment, table_columns = filterByTableName(tableName, allTableColumns)
            for i in range(len(table_columns)):
                sheet.write(row_num_index, 1, table_columns[i]['column_name'])
                sheet.write(row_num_index, 2, table_columns[i]['data_type'])
                sheet.write(row_num_index, 3, table_columns[i]['is_nullable'])
                sheet.write(row_num_index, 4, table_columns[i]['column_key'])
                sheet.write(row_num_index, 5, table_columns[i]['column_comment'])
                # 下一行
                row_num_index += 1
            # 合并行
            sheet.write_merge(row_num_index - len(table_columns), row_num_index - 1, 0, 0, table_name_and_comment,
                              getMergeRowStyle())
            for i in range(len(headers)):
                # 空白行，和表头样式一样
                sheet.write(row_num_index, i, None, getHeaderStyle())
            # 每个表之间间隔一行
            row_num_index += 1
        wb.save(save_file_path)
    print(save_file_path)
    print("导出完成")


if __name__ == '__main__':
    sheet_tables_config = {
        "第一页": ('cfg_global', 'exception_board'),
        "第二页": ('sys_permission', 'sys_user')
    }
    headers = ['表名', '字段名', '类型', '是否可为空', '是否主键', '注释']
    save_file_path = 'C:\\Users\\huangbiao\\Desktop\\表结构_%s.xls' % datetime.date.today().strftime('%Y%m%d')
    export_table_structure('local', sheet_tables_config, headers, save_file_path)

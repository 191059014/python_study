import datetime

from GlobalUtils import DB
from generate_controller import create_controller_class
from generate_entity import create_entity_class
from generate_mapperclass import create_mapper_class
from generate_mapperxml import create_mapper_xml
from generate_service import create_service_class
from generate_serviceimpl import create_serviceimpl_class
from util import *

select_table_sql = "select table_name tableName, table_comment tableComment from information_schema.tables where table_schema = (select database()) and table_name = '%s'"
select_column_sql = "select column_name columnName, data_type dataType, column_comment columnComment,column_key columnKey, extra from information_schema.columns where table_name = '%s' and table_schema = (select database()) order by ordinal_position"


# 生成代码文件
def create_code_file(dbEnv, tableName, upperClassName, package, savePath):
    dicts = {}
    db = DB(dbEnv)
    # 查询表结构
    dbTableInfo = db.query(select_table_sql % tableName)[0]
    # 设置表信息
    dicts[TABLE_NAME] = tableName
    dicts[TABLE_COMMENT] = dbTableInfo['tableComment']
    # 查询所有列
    dbColumnList = db.query(select_column_sql % tableName)
    columnList = []
    for dbColumn in dbColumnList:
        column = {}
        column[COLUMN_NAME] = dbColumn['columnName']
        column[LOWER_PROPERTY_NAME] = to_camelcase(dbColumn['columnName'])
        column[IS_PK] = dbColumn['columnKey'] == 'PRI'
        column[PROPERTY_DATA_TYPE] = getPropertyDataType(dbColumn['dataType'])
        column[COLUMN_COMMENT] = dbColumn['columnComment']
        columnList.append(column)
    # 设置列信息
    dicts[COLUMN_LIST] = columnList
    dicts[UPPER_CLASS_NAME] = upperClassName
    dicts[LOWER_CLASS_NAME] = get_lower_class_name(upperClassName)
    dicts[AUTHOR] = 'huangbiao'
    dicts[NOW_TIME] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dicts[PACKAGE] = package
    dicts[GENERATE_FILE_PATH] = savePath
    # 准备创建
    create_mapper_xml(dicts)
    create_mapper_class(dicts)
    create_entity_class(dicts)
    create_service_class(dicts)
    create_serviceimpl_class(dicts)
    create_controller_class(dicts)


if __name__ == '__main__':
    create_code_file('dev', 'sys_audit_log', 'AuditLog', 'com.hb.test.db.codegenerate', '../temp/')

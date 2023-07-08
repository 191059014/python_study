import re
from enum import Enum

# 表信息常量
TABLE_NAME = 'tableName'
TABLE_COMMENT = 'table_comment'
# 列信息常量
COLUMN_LIST = 'columnList'
COLUMN_NAME = 'columnName'
LOWER_PROPERTY_NAME = 'lowerPropertyName'
UPPER_PROPERTY_NAME = 'upperPropertyName'
PROPERTY_DATA_TYPE = 'propertyDataType'
COLUMN_COMMENT = 'column_comment'
IS_PK = "isPk"
# 类信息常量
UPPER_CLASS_NAME = 'upperClassName'
LOWER_CLASS_NAME = 'lowerClassName'
# 其他常量
AUTHOR = 'author'
NOW_TIME = 'now_time'
PACKAGE = 'package'
# 缩进
INDENT = '    '
INDENT2 = INDENT * 2
INDENT3 = INDENT * 3
INDENT4 = INDENT * 4
# 生成文件的根路径
GENERATE_FILE_PATH = 'generateFilePath'


# 数据类型映射关系枚举
class DATA_TYPE_MAP(Enum):
    Integer = ['tinyint', 'smallint', 'mediumint', 'int', 'number', 'integer'],
    String = ['char', 'varchar', 'blob', 'text', 'mediumblob', 'mediumtext', 'longblob', 'longtext'],
    Date = ['year', 'time', 'date', 'datetime', 'timestamp'],
    Long = ['bigint'],
    Float = ['float'],
    Double = ['double'],
    BigDecimal = ['decimal'],
    Boolean = ['bit']


# 通过数据库类型获取Java字段类型
def getPropertyDataType(dbDataType):
    for d in DATA_TYPE_MAP:
        if dbDataType in d.value[0]:
            return d.name
    raise RuntimeError('匹配不到对应的Java数据类型：' + dbDataType)


# 下划线转驼峰
def to_camelcase(name: str) -> str:
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), name.lower())


# 通过大写类名获取小写类名
def get_lower_class_name(upper_class_name):
    return upper_class_name[0].lower() + upper_class_name[1:]


# 过滤主键列
def filter_id_column(column_list):
    return list(filter(lambda column: column[IS_PK], column_list))[0]


# 过滤非主键列
def filter_not_id_column(column_list):
    return list(filter(lambda column: not column[IS_PK], column_list))


if __name__ == '__main__':
    print(getPropertyDataType('bigint'))

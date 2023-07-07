import re
from enum import Enum

TABLE_NAME = 'tableName'
COLUMN_LIST = 'columnList'
COLUMN_NAME = 'columnName'
LOWER_PROPERTY_NAME = 'lowerPropertyName'
UPPER_PROPERTY_NAME = 'upperPropertyName'
IS_PK = "isPk"
UPPER_CLASS_NAME = 'upperClassName'
LOWER_CLASS_NAME = 'lowerClassName'
INDENT = '    '
INDENT2 = INDENT * 2
INDENT3 = INDENT * 3
INDENT4 = INDENT * 4
GENERATE_FILE_PATH = 'generateFilePath'
PROPERTY_DATA_TYPE = 'propertyDataType'


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
    print(DATA_TYPE_MAP.Integer.name)

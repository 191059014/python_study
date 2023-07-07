from generate_mapperxml import create_mapper_xml

from util import *

if __name__ == '__main__':
    dicts = {}
    dicts[TABLE_NAME] = 't_user'
    column1 = {COLUMN_NAME: 'user_id', LOWER_PROPERTY_NAME: to_camelcase('user_id'), IS_PK: True, PROPERTY_DATA_TYPE:DATA_TYPE_MAP.Long.name}
    column2 = {COLUMN_NAME: 'user_name', LOWER_PROPERTY_NAME: to_camelcase('user_name'), IS_PK: False, PROPERTY_DATA_TYPE:DATA_TYPE_MAP.String.name}
    column3 = {COLUMN_NAME: 'password', LOWER_PROPERTY_NAME: to_camelcase('password'), IS_PK: False, PROPERTY_DATA_TYPE:DATA_TYPE_MAP.String.name}
    columnList = [column1, column2, column3]
    dicts[COLUMN_LIST] = columnList
    dicts[UPPER_CLASS_NAME] = 'User'
    dicts[LOWER_CLASS_NAME] = get_lower_class_name('User')
    dicts[GENERATE_FILE_PATH] = '../temp/'
    create_mapper_xml(dicts)

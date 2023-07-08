from util import *


def generate_packageAndImport(dicts):
    lists = []
    lists.append('package %s;' % dicts[PACKAGE])
    lists.append('')
    lists.append('import lombok.Data;')
    propertyDataTypes = set(map(lambda column: column[PROPERTY_DATA_TYPE], dicts[COLUMN_LIST]))
    if DATA_TYPE_MAP.Date.name in propertyDataTypes:
        lists.append('import java.util.Date;')
    if DATA_TYPE_MAP.BigDecimal.name in propertyDataTypes:
        lists.append('import java.math.BigDecimal;')
    return lists


def generate_allProperty(dicts):
    lists = ['']
    for column in dicts[COLUMN_LIST]:
        lists.append(INDENT + '/**')
        lists.append(INDENT + ' * %s' % column.get(COLUMN_COMMENT))
        lists.append(INDENT + ' */')
        lists.append(INDENT + 'private %s %s;' % (column[PROPERTY_DATA_TYPE], column[LOWER_PROPERTY_NAME]))
        lists.append('')
    return lists


def create_entity_class(dicts):
    lists = []
    lists.extend(generate_packageAndImport(dicts))
    lists.append('/**')
    lists.append(' * %s数据模型' % dicts[TABLE_COMMENT])
    lists.append(' *')
    lists.append(' * @version v0.1, %s, create by %s.' % (dicts[NOW_TIME], dicts[AUTHOR]))
    lists.append(' */')
    lists.append('@Data')
    lists.append('public class %sDO {' % dicts[UPPER_CLASS_NAME])
    lists.extend(generate_allProperty(dicts))
    lists.append('}')
    content = '\n'.join(lists)
    filename = '%sDO.java' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

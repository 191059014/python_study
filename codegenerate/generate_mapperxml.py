from util import *


def _create_table_alias(dicts):
    return dicts[LOWER_CLASS_NAME][0]


def _create_column_prefix(dicts):
    return _create_table_alias(dicts) + '.'


def _create_logic_valid(dicts):
    return _create_column_prefix(dicts) + 'is_valid = 1'


def _create_logic_invalid(dicts):
    return _create_column_prefix(dicts) + 'is_valid = 0'


def _create_orderby(dicts):
    return 'order by ' + _create_column_prefix(dicts) + 'update_time desc'


def _create_getPropertyValue_sql(dicts, column):
    return '#{' + dicts[LOWER_CLASS_NAME] + '.' + column[LOWER_PROPERTY_NAME] + '}'


def _create_if_sql(dicts, column):
    lists = []
    propertyDataType = column[PROPERTY_DATA_TYPE]
    ifNull = '<if test="%s != null">'
    ifEmpty = '<if test="%s != null and %s != \'\'">'
    if DATA_TYPE_MAP.String.name == propertyDataType:
        lists.append(INDENT3 + ifEmpty % (column[LOWER_PROPERTY_NAME], column[LOWER_PROPERTY_NAME]))
    else:
        lists.append(INDENT3 + ifNull % column[LOWER_PROPERTY_NAME])
    lists.append(INDENT4 + 'and %s%s = %s' % (
        _create_column_prefix(dicts), column[COLUMN_NAME], _create_getPropertyValue_sql(dicts, column)))
    lists.append(INDENT3 + '</if>')
    return lists


def generate_resultMap(dicts):
    lists = ['']
    lists.append(INDENT + '<!--字段映射-->')
    lists.append(INDENT + '<resultMap id="%sMap" type="%sDO">' % (dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME]))
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + '<id column="%s" property="%s"/>' % (id_column[COLUMN_NAME], id_column[LOWER_PROPERTY_NAME]))
    not_id_columns = filter_not_id_column(dicts[COLUMN_LIST])
    for not_id_column in not_id_columns:
        lists.append((INDENT2 + '<result column="%s" property="%s"/>') % (
            not_id_column[COLUMN_NAME], not_id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT + '</resultMap>')
    return lists


def generate_allFields(dicts):
    lists = ['']
    lists.append(INDENT + '<!--所有列-->')
    lists.append(INDENT + '<sql id="allFields">')
    lists.extend(
        map(lambda column: INDENT2 + column[COLUMN_NAME] + ',', dicts[COLUMN_LIST][:len(dicts[COLUMN_LIST]) - 1]))
    lists.append(INDENT2 + dicts[COLUMN_LIST][-1][COLUMN_NAME])
    lists.append(INDENT + '</sql>')
    return lists


def generate_allFieldsWithPrefix(dicts):
    lists = ['']
    lists.append(INDENT + '<!--所有列，带前缀-->')
    lists.append(INDENT + '<sql id="allFieldsWithPrefix">')
    lists.extend(
        map(lambda column: INDENT2 + _create_column_prefix(dicts) + column[COLUMN_NAME] + ',',
            dicts[COLUMN_LIST][:len(dicts[COLUMN_LIST]) - 1]))
    lists.append(INDENT2 + _create_column_prefix(dicts) + dicts[COLUMN_LIST][-1][COLUMN_NAME])
    lists.append(INDENT + '</sql>')
    return lists


def generate_allPropertys(dicts):
    lists = ['']
    lists.append(INDENT + '<!--所有属性-->')
    lists.append(INDENT + '<sql id="allPropertys">')
    lists.extend(map(lambda column: INDENT2 + _create_getPropertyValue_sql(dicts, column) + ',',
                     dicts[COLUMN_LIST][:len(dicts[COLUMN_LIST]) - 1]))
    lists.append(INDENT2 + _create_getPropertyValue_sql(dicts, dicts[COLUMN_LIST][-1]))
    lists.append(INDENT + '</sql>')
    return lists


def generate_allQueryConditions(dicts):
    lists = ['']
    lists.append(INDENT + '<!--查询条件-->')
    lists.append(INDENT + '<sql id="whereCondition">')
    lists.append(INDENT2 + '<where>')
    lists.append(INDENT3 + _create_logic_valid(dicts))
    for column in dicts[COLUMN_LIST]:
        lists.extend(_create_if_sql(dicts, column))
    lists.append(INDENT2 + '</where>')
    lists.append(INDENT + '</sql>')
    return lists


def generate_allUpdateFields(dicts):
    lists = ['']
    lists.append(INDENT + '<!--更新字段sql-->')
    lists.append(INDENT + '<sql id="updateFields">')
    lists.append(INDENT2 + '<set>')
    for column in dicts[COLUMN_LIST]:
        lists.extend(_create_if_sql(dicts, column))
    lists.append(INDENT2 + '</set>')
    lists.append(INDENT + '</sql>')
    return lists


def generate_insert(dicts):
    lists = ['']
    lists.append(INDENT + '<!--新增-->')
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '<insert id="insert" useGeneratedKeys="true" keyProperty="%s" keyColumn="%s">' % (
        id_column[LOWER_PROPERTY_NAME], id_column[COLUMN_NAME]))
    lists.append(INDENT2 + 'insert into %s' % dicts[TABLE_NAME])
    lists.append(INDENT2 + '(<include refid="allFields"/>)')
    lists.append(INDENT2 + 'values')
    lists.append(INDENT2 + '(<include refid="allPropertys"/>)')
    lists.append(INDENT + '</insert>')
    return lists


def generate_insertBatch(dicts):
    lists = ['']
    lists.append(INDENT + '<!--批量新增-->')
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '<insert id="insertBatch" useGeneratedKeys="true" keyProperty="%s" keyColumn="%s">' % (
        id_column[LOWER_PROPERTY_NAME], id_column[COLUMN_NAME]))
    lists.append(INDENT2 + 'insert into %s' % dicts[TABLE_NAME])
    lists.append(INDENT2 + '(<include refid="allFields"/>)')
    lists.append(INDENT2 + 'values')
    lists.append(INDENT2 + '<foreach collection="%sList" item="%s" open="(" close=")" separator="," >' % (
        dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT3 + '<include refid="allPropertys"/>')
    lists.append(INDENT2 + '</foreach>')
    lists.append(INDENT + '</insert>')
    return lists


def generate_updateById(dicts):
    lists = ['']
    lists.append(INDENT + '<!--通过id修改-->')
    lists.append(INDENT + '<update id="updateById">')
    lists.append(INDENT2 + 'update %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + '<include refid="updateFields"/>')
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + 'where %s = %s and %s' % (
        _create_column_prefix(dicts) + id_column[COLUMN_NAME], _create_getPropertyValue_sql(dicts, id_column),
        _create_logic_valid(dicts)))
    lists.append(INDENT + '</update>')
    return lists


def generate_deleteById(dicts):
    lists = ['']
    lists.append(INDENT + '<!--通过id逻辑删除-->')
    lists.append(INDENT + '<update id="deleteById">')
    lists.append(INDENT2 + 'update %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + 'set %s' % _create_logic_invalid(dicts))
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + 'where %s = %s and %s' % (
        _create_column_prefix(dicts) + id_column[COLUMN_NAME], _create_getPropertyValue_sql(dicts, id_column),
        _create_logic_valid(dicts)))
    lists.append(INDENT + '</update>')
    return lists


def generate_deleteByIds(dicts):
    lists = ['']
    lists.append(INDENT + '<!--通过id集合逻辑删除-->')
    lists.append(INDENT + '<update id="deleteByIds">')
    lists.append(INDENT2 + 'update %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + 'set %s' % _create_logic_invalid(dicts))
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + 'where %s and %s%s in' % (
        _create_logic_valid(dicts), _create_column_prefix(dicts), id_column[COLUMN_NAME]))
    lists.append(INDENT2 + '<foreach collection="%s" item="%s" open="(" close=")" separator="," >' % (
        id_column[LOWER_PROPERTY_NAME] + 's', id_column[COLUMN_NAME]))
    lists.append(INDENT3 + '#{%s}' % id_column[COLUMN_NAME])
    lists.append(INDENT2 + '</foreach>')
    lists.append(INDENT + '</update>')
    return lists


def generate_selectById(dicts):
    lists = ['']
    lists.append(INDENT + '<!--根据id查询-->')
    lists.append(INDENT + '<select id="selectById" resultMap="%sMap">' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT2 + 'select')
    lists.append(INDENT2 + '<include refid="allFieldsWithPrefix"/>')
    lists.append(INDENT2 + 'from %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + 'where %s%s = %s and %s' % (
        _create_column_prefix(dicts), id_column[COLUMN_NAME], _create_getPropertyValue_sql(dicts, id_column),
        _create_logic_valid(dicts)))
    lists.append(INDENT + '</select>')
    return lists


def generate_selectByIds(dicts):
    lists = ['']
    lists.append(INDENT + '<!--根据id集合查询-->')
    lists.append(INDENT + '<select id="selectByIds" resultMap="%sMap">' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT2 + 'select')
    lists.append(INDENT2 + '<include refid="allFieldsWithPrefix"/>')
    lists.append(INDENT2 + 'from %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT2 + 'where %s and %s%s in' % (
        _create_logic_valid(dicts), _create_column_prefix(dicts), id_column[COLUMN_NAME]))
    lists.append(INDENT2 + '<foreach collection="%s" item="%s" open="(" close=")" separator="," >' % (
        id_column[LOWER_PROPERTY_NAME] + 's', id_column[COLUMN_NAME]))
    lists.append(INDENT3 + '#{%s}' % id_column[COLUMN_NAME])
    lists.append(INDENT2 + '</foreach>')
    lists.append(INDENT2 + _create_orderby(dicts))
    lists.append(INDENT + '</select>')
    return lists


def generate_selectList(dicts):
    lists = ['']
    lists.append(INDENT + '<!--根据条件查询-->')
    lists.append(INDENT + '<select id="selectList" resultMap="%sMap">' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT2 + 'select')
    lists.append(INDENT2 + '<include refid="allFieldsWithPrefix"/>')
    lists.append(INDENT2 + 'from %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + '<include refid="whereCondition"/>')
    lists.append(INDENT2 + _create_orderby(dicts))
    lists.append(INDENT + '</select>')
    return lists


def generate_selectCount(dicts):
    lists = ['']
    lists.append(INDENT + '<!--查询总条数-->')
    lists.append(INDENT + '<select id="selectCount" resultType="java.lang.Long">')
    lists.append(INDENT2 + 'select count(1) from %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + '<include refid="whereCondition"/>')
    lists.append(INDENT + '</select>')
    return lists


def generate_selectPages(dicts):
    lists = ['']
    lists.append(INDENT + '<!--分页条件查询-->')
    lists.append(INDENT + '<select id="selectPages" resultMap="%sMap">' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT2 + 'select')
    lists.append(INDENT2 + '<include refid="allFieldsWithPrefix"/>')
    lists.append(INDENT2 + 'from %s %s' % (dicts[TABLE_NAME], _create_table_alias(dicts)))
    lists.append(INDENT2 + '<include refid="whereCondition"/>')
    lists.append(INDENT2 + _create_orderby(dicts))
    lists.append(INDENT2 + 'limit #{startIndex}, #{pageSize}')
    lists.append(INDENT + '</select>')
    return lists


def create_mapper_xml(dicts):
    lists = []
    lists.append('<?xml version="1.0" encoding="UTF-8"?>')
    lists.append(
        '<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">')
    lists.append('<mapper namespace="${package}.I%sMapper">' % dicts[UPPER_CLASS_NAME])
    lists.extend(generate_resultMap(dicts))
    lists.extend(generate_allFields(dicts))
    lists.extend(generate_allFieldsWithPrefix(dicts))
    lists.extend(generate_allPropertys(dicts))
    lists.extend(generate_allQueryConditions(dicts))
    lists.extend(generate_allUpdateFields(dicts))
    lists.extend(generate_insert(dicts))
    lists.extend(generate_insertBatch(dicts))
    lists.extend(generate_updateById(dicts))
    lists.extend(generate_deleteById(dicts))
    lists.extend(generate_deleteByIds(dicts))
    lists.extend(generate_selectById(dicts))
    lists.extend(generate_selectByIds(dicts))
    lists.extend(generate_selectList(dicts))
    lists.extend(generate_selectCount(dicts))
    lists.extend(generate_selectPages(dicts))
    lists.append('')
    lists.append('</mapper>')
    content = '\n'.join(lists)
    filename = '%sMapper.xml' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

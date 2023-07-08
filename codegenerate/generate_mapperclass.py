from util import *


def generate_insert(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 插入的实体对象' % (dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int insert(@Param("%s") %sDO %s);' % (
        dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_insertBatch(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 批量插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %sList 插入的实体对象列表' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int insertBatch(@Param("%sList") List<%sDO> %sList);' % (
        dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_updateById(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键更新')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 更新的实体对象' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int updateById(@Param("%s") %sDO %s);' % (
        dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_deleteByIds(dicts):
    lists = ['']
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键集合批量删除')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %ss 主键集合' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int deleteByIds(@Param("%ss") Set<%s> %ss);' % (
        id_column[LOWER_PROPERTY_NAME], id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    return lists


def generate_selectByIds(dicts):
    lists = ['']
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键集合批量查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %ss 主键集合' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'List<%sDO> selectByIds(@Param("%ss") Set<%s> %ss);' % (
        dicts[UPPER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME], id_column[PROPERTY_DATA_TYPE],
        id_column[LOWER_PROPERTY_NAME]))
    return lists


def generate_selectList(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据条件查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'List<%sDO> selectList(@Param("%s") %sDO %s);' % (
        dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
        dicts[LOWER_CLASS_NAME]))
    return lists


def generate_selectCount(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 查询总条数')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 总条数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'long selectCount(@Param("%s") %sDO %s);' % (dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
                                                                       dicts[LOWER_CLASS_NAME]))
    return lists


def generate_selectPages(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 分页条件查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(
        INDENT + 'List<%sDO> selectPages(@Param("%s") %sDO %s, @Param("startIndex") int startIndex, @Param("pageSize") int pageSize);' % (
            dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
            dicts[LOWER_CLASS_NAME]))
    return lists


def create_mapper_class(dicts):
    lists = []
    lists.append('package %s;' % dicts[PACKAGE])
    lists.append('')
    lists.append('import java.util.List;')
    lists.append('import java.util.Set;')
    lists.append('')
    lists.append('import org.apache.ibatis.annotations.Param;')
    lists.append('')
    lists.append('/**')
    lists.append(' * %s数据库交互层' % dicts[TABLE_COMMENT])
    lists.append(' *')
    lists.append(' * @version v0.1, %s, create by %s.' % (dicts[NOW_TIME], dicts[AUTHOR]))
    lists.append(' */')
    lists.append('public interface I%sMapper {' % dicts[UPPER_CLASS_NAME])
    lists.extend(generate_insert(dicts))
    lists.extend(generate_insertBatch(dicts))
    lists.extend(generate_updateById(dicts))
    lists.extend(generate_deleteByIds(dicts))
    lists.extend(generate_selectByIds(dicts))
    lists.extend(generate_selectList(dicts))
    lists.extend(generate_selectCount(dicts))
    lists.extend(generate_selectPages(dicts))
    lists.append('}')
    content = '\n'.join(lists)
    filename = 'I%sMapper.java' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

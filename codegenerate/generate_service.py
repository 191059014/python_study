from util import *


def generate_insert(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 插入的实体对象' % (dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int insert(%sDO %s);' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_insertBatch(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 批量插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %sList 插入的实体对象列表' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int insertBatch(List<%sDO> %sList);' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_updateById(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键更新')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 更新的实体对象' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int updateById(%sDO %s);' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def generate_deleteById(dicts):
    lists = ['']
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键删除')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 主键' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + 'int deleteById(%s %s);' % (id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
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
    lists.append(
        INDENT + 'int deleteByIds(Set<%s> %ss);' % (id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    return lists


def generate_selectById(dicts):
    lists = ['']
    id_column = filter_id_column(dicts[COLUMN_LIST])
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 主键' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT + ' * @return 结果')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '%sDO selectById(%s %s);' % (
        dicts[UPPER_CLASS_NAME], id_column[PROPERTY_DATA_TYPE],
        id_column[LOWER_PROPERTY_NAME]))
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
    lists.append(INDENT + 'List<%sDO> selectByIds(Set<%s> %ss);' % (
        dicts[UPPER_CLASS_NAME], id_column[PROPERTY_DATA_TYPE],
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
    lists.append(INDENT + 'List<%sDO> selectList(%sDO %s);' % (
        dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
        dicts[LOWER_CLASS_NAME]))
    return lists


def generate_selectPages(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 分页条件查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @param pageParameter 分页参数')
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(
        INDENT + 'PageResult<%sDO> selectPages(%sDO %s, PageParameter pageParameter);' % (
            dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    return lists


def create_service_class(dicts):
    lists = []
    lists.append('package %s;' % dicts[PACKAGE])
    lists.append('')
    lists.append('import java.util.List;')
    lists.append('import java.util.Set;')
    lists.append('')
    lists.append('import com.hb.unic.base.web.PageResult;')
    lists.append('import com.hb.unic.base.web.PageParameter;')
    lists.append('')
    lists.append('/**')
    lists.append(' * %s服务层' % dicts[TABLE_COMMENT])
    lists.append(' *')
    lists.append(' * @version v0.1, %s, create by %s.' % (dicts[NOW_TIME], dicts[AUTHOR]))
    lists.append(' */')
    lists.append('public interface I%sService {' % dicts[UPPER_CLASS_NAME])
    lists.extend(generate_insert(dicts))
    lists.extend(generate_insertBatch(dicts))
    lists.extend(generate_updateById(dicts))
    lists.extend(generate_deleteById(dicts))
    lists.extend(generate_deleteByIds(dicts))
    lists.extend(generate_selectById(dicts))
    lists.extend(generate_selectByIds(dicts))
    lists.extend(generate_selectList(dicts))
    lists.extend(generate_selectPages(dicts))
    lists.append('}')
    content = '\n'.join(lists)
    filename = 'I%sService.java' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

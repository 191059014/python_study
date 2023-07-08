from util import *


def generate_insert(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 插入的实体对象' % (dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Override')
    lists.append(INDENT + 'public int insert(%sDO %s) {' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return %sMapper.insert(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
    return lists


def generate_insertBatch(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 批量插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %sList 插入的实体对象列表' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Override')
    lists.append(
        INDENT + 'public int insertBatch(List<%sDO> %sList) {' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return %sMapper.insertBatch(%sList);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
    return lists


def generate_updateById(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据主键更新')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 更新的实体对象' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Override')
    lists.append(INDENT + 'public int updateById(%sDO %s) {' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return %sMapper.updateById(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
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
    lists.append(INDENT + '@Override')
    lists.append(
        INDENT + 'public int deleteById(%s %s) {' % (id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    lists.append(
        INDENT2 + 'Set<%s> %ss = new HashSet<>();' % (id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + '%ss.add(%s);' % (id_column[LOWER_PROPERTY_NAME], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + 'return this.deleteByIds(%ss);' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT + '}')
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
    lists.append(INDENT + '@Override')
    lists.append(
        INDENT + 'public int deleteByIds(Set<%s> %ss) {' % (
            id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + 'if (CollectionUtils.isEmpty(%ss)) {' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT3 + 'return 0;')
    lists.append(INDENT2 + '}')
    lists.append(
        INDENT2 + 'return %sMapper.deleteByIds(%ss);' % (dicts[LOWER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT + '}')
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
    lists.append(INDENT + '@Override')
    lists.append(INDENT + 'public %sDO selectById(%s %s) {' % (
        dicts[UPPER_CLASS_NAME], id_column[PROPERTY_DATA_TYPE],
        id_column[LOWER_PROPERTY_NAME]))
    lists.append(
        INDENT2 + 'Set<%s> %ss = new HashSet<>();' % (id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + '%ss.add(%s);' % (id_column[LOWER_PROPERTY_NAME], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + 'List<%sDO> %sList = this.selectByIds(%ss);' % (
        dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + 'return CollectionUtils.isEmpty(%sList) ? null : %sList.get(0);' % (
        dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
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
    lists.append(INDENT + '@Override')
    lists.append(INDENT + 'public List<%sDO> selectByIds(Set<%s> %ss) {' % (
        dicts[UPPER_CLASS_NAME], id_column[PROPERTY_DATA_TYPE],
        id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT2 + 'if (CollectionUtils.isEmpty(%ss)) {' % id_column[LOWER_PROPERTY_NAME])
    lists.append(INDENT3 + 'return new ArrayList<>();')
    lists.append(INDENT2 + '}')
    lists.append(
        INDENT2 + 'return %sMapper.selectByIds(%ss);' % (dicts[LOWER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME]))
    lists.append(INDENT + '}')
    return lists


def generate_selectList(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 根据条件查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Override')
    lists.append(INDENT + 'public List<%sDO> selectList(%sDO %s) {' % (
        dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
        dicts[LOWER_CLASS_NAME]))
    lists.append(
        INDENT2 + 'return %sMapper.selectList(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
    return lists


def generate_selectPages(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 分页条件查询')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 查询条件' % dicts[LOWER_CLASS_NAME])
    lists.append(INDENT + ' * @return 结果列表')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Override')
    lists.append(
        INDENT + 'public Page<%sDO> selectPages(%sDO %s, int startIndex, int pageSize) {' % (
            dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return null;')
    lists.append(INDENT + '}')
    return lists


def create_serviceimpl_class(dicts):
    lists = []
    lists.append('package %s;' % dicts[PACKAGE])
    lists.append('import java.util.ArrayList;')
    lists.append('import java.util.List;')
    lists.append('import java.util.Set;')
    lists.append('import java.util.HashSet;')
    lists.append('import org.springframework.util.CollectionUtils;')
    lists.append('import javax.annotation.Resource;')
    lists.append('import com.hb.unic.common.standard.Page;')
    lists.append('/**')
    lists.append(' * %s服务层' % dicts[TABLE_COMMENT])
    lists.append(' *')
    lists.append(' * @version v0.1, %s, create by %s.' % (dicts[NOW_TIME], dicts[AUTHOR]))
    lists.append(' */')
    lists.append('public class %sServiceImpl implements IUserDetailService {' % dicts[UPPER_CLASS_NAME])
    lists.append('')
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * %s数据库交互层' % dicts[TABLE_COMMENT])
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Resource')
    lists.append(INDENT + 'private I%sMapper %sMapper;' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
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
    filename = '%sServiceImpl.java' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

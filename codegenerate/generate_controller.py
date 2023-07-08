from util import *


def generate_insert(dicts):
    lists = ['']
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * 插入')
    lists.append(INDENT + ' *')
    lists.append(INDENT + ' * @param %s 插入的实体对象' % (dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + ' * @return 影响的行数')
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@PostMapping("/insert")')
    lists.append(
        INDENT + 'public int insert(@RequestBody %sDO %s) {' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return %sService.insert(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
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
    lists.append(INDENT + '@PostMapping("/updateById")')
    lists.append(
        INDENT + 'public int updateById(@RequestBody %sDO %s) {' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT2 + 'return %sService.updateById(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
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
    lists.append(INDENT + '@GetMapping("/deleteById")')
    lists.append(
        INDENT + 'public int deleteById(@RequestParam("%s") %s %s) {' % (
            id_column[LOWER_PROPERTY_NAME], id_column[PROPERTY_DATA_TYPE], id_column[LOWER_PROPERTY_NAME]))
    lists.append(
        INDENT2 + 'return %sService.deleteById(%s);' % (dicts[LOWER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME]))
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
    lists.append(INDENT + '@GetMapping("/selectById")')
    lists.append(INDENT + 'public %sDO selectById(@RequestParam("%s") %s %s) {' % (
        dicts[UPPER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME], id_column[PROPERTY_DATA_TYPE],
        id_column[LOWER_PROPERTY_NAME]))
    lists.append(
        INDENT2 + 'return %sService.selectById(%s);' % (dicts[LOWER_CLASS_NAME], id_column[LOWER_PROPERTY_NAME]))
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
    lists.append(INDENT + '@PostMapping("/selectList")')
    lists.append(INDENT + 'public List<%sDO> selectList(@RequestBody %sDO %s) {' % (
        dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME],
        dicts[LOWER_CLASS_NAME]))
    lists.append(
        INDENT2 + 'return %sService.selectList(%s);' % (dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
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
    lists.append(INDENT + '@PostMapping("/selectList")')
    lists.append(
        INDENT + 'public Page<%sDO> selectPages(@RequestBody %sDO %s, @RequestParam("pageNum") Integer pageNum, @RequestParam("pageSize") Integer pageSize) {' % (
            dicts[UPPER_CLASS_NAME], dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(
        INDENT2 + 'return %sService.selectPages(%s, (pageNum - 1) * pageSize, pageSize);' % (
            dicts[LOWER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.append(INDENT + '}')
    return lists


def create_controller_class(dicts):
    lists = []
    lists.append('package %s;' % dicts[PACKAGE])
    lists.append('import lombok.extern.slf4j.Slf4j;')
    lists.append('import org.springframework.web.bind.annotation.RestController;')
    lists.append('import org.springframework.web.bind.annotation.RequestMapping;')
    lists.append('import org.springframework.web.bind.annotation.GetMapping;')
    lists.append('import org.springframework.web.bind.annotation.PostMapping;')
    lists.append('import org.springframework.web.bind.annotation.RequestBody;')
    lists.append('import org.springframework.web.bind.annotation.RequestParam;')
    lists.append('import java.util.List;')
    lists.append('import javax.annotation.Resource;')
    lists.append('import com.hb.unic.common.standard.Page;')
    lists.append('/**')
    lists.append(' * %s控制层' % dicts[TABLE_COMMENT])
    lists.append(' *')
    lists.append(' * @version v0.1, %s, create by %s.' % (dicts[NOW_TIME], dicts[AUTHOR]))
    lists.append(' */')
    lists.append('@Slf4j')
    lists.append('@RestController')
    lists.append('@RequestMapping("/%s")' % dicts[LOWER_CLASS_NAME])
    lists.append('public class %sController {' % dicts[UPPER_CLASS_NAME])
    lists.append('')
    lists.append(INDENT + '/**')
    lists.append(INDENT + ' * %s服务层' % dicts[TABLE_COMMENT])
    lists.append(INDENT + ' */')
    lists.append(INDENT + '@Resource')
    lists.append(INDENT + 'private I%sService %sService;' % (dicts[UPPER_CLASS_NAME], dicts[LOWER_CLASS_NAME]))
    lists.extend(generate_insert(dicts))
    lists.extend(generate_updateById(dicts))
    lists.extend(generate_deleteById(dicts))
    lists.extend(generate_selectById(dicts))
    lists.extend(generate_selectList(dicts))
    lists.extend(generate_selectPages(dicts))
    lists.append('}')
    content = '\n'.join(lists)
    filename = '%sController.java' % dicts[UPPER_CLASS_NAME]
    with open(dicts[GENERATE_FILE_PATH] + filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(filename, '创建完成')

"""
表或者数据迁移
"""

from mysql_utils import *


class MigrateTask:
    """
    迁移任务，封装数据迁移时候的参数
    """

    def __init__(self, table_name: str, where_sql: str, *exclude_columns) -> None:
        # 需要迁移的表名
        self.table_name = table_name
        # 需要迁移的数据的where查询条件
        self.where_sql = where_sql
        # 不需要迁移的列，这里统一转小写
        exclude_columns = [column_name.lower() for column_name in exclude_columns]
        self.exclude_columns = exclude_columns


def do_table_structure_migrate(*tablenames, originDbName: str, targetDbName: str, includeDatas: bool = False):
    """
    迁移表结构
    :param tablenames 表名，可以接受多个表
    :param originDbName 原始库
    :param targetDbName 目标库
    """
    originDb = get_db(originDbName)
    originCursor = get_dictcursor(originDb)
    targetDb = get_db(targetDbName)
    targetCursor = get_dictcursor(targetDb)
    print('============================ %s => %s ============================' % (originDbName, targetDbName))
    try:
        for table_name in tablenames:
            originCursor.execute("show create table %s" % table_name)
            result = originCursor.fetchone()
            create_table_sql = result['Create Table']
            drop_table_sql = "drop table if exists %s;" % table_name
            print(drop_table_sql)
            targetCursor.execute(drop_table_sql)
            print(create_table_sql)
            targetCursor.execute(create_table_sql)
            print('\n表%s结构迁移完成' % table_name)
            if includeDatas:
                _do_one_table_data_migrate(originCursor, targetCursor, table_name, "")
            print('============================ %s => %s ============================' % (originDbName, targetDbName))
    except BaseException as e:
        targetDb.rollback()
        print("发生异常，数据回滚完成，异常信息：%s" % e)
    else:
        targetDb.commit()
        print("事务提交完成")
    finally:
        originCursor.close()
        originDb.close()
        targetCursor.close()
        targetDb.close()
        print("关闭数据库连接完成")


def do_table_data_migrate(*tasks, originDbName: str, targetDbName: str):
    """
    数据迁移
    :param tasks 每个表一个task，可以接受多个表
    :param originDbName 原始库
    :param targetDbName 目标库
    """
    originDb = get_db(originDbName)
    originCursor = get_dictcursor(originDb)
    targetDb = get_db(targetDbName)
    targetCursor = get_dictcursor(targetDb)
    print('============================ %s => %s ============================' % (originDbName, targetDbName))
    try:
        for task in tasks:
            table_name = task.table_name
            where_sql = task.where_sql
            exclude_columns = task.exclude_columns
            _do_one_table_data_migrate(originCursor, targetCursor, table_name, where_sql, *exclude_columns)
            print('============================ %s => %s ============================' % (originDbName, targetDbName))
    except BaseException as e:
        targetDb.rollback()
        print("发生异常，数据回滚完成，异常信息：%s" % e)
    else:
        targetDb.commit()
        print("事务提交完成")
    finally:
        originCursor.close()
        originDb.close()
        targetCursor.close()
        targetDb.close()
        print("关闭数据库连接完成")


def _do_one_table_data_migrate(originCursor, targetCursor, table_name, where_sql, *exclude_columns):
    """
    单表数据迁移
    :param originCursor: 原始库游标
    :param targetCursor: 目标库游标
    :param table_name: 表名
    :param where_sql: 需要迁移的数据的过滤条件
    :param exclude_columns: 不需要迁移到目标表的列
    """
    print('开始迁移%s表数据，查询条件：%s，不需要迁移的列：%s' % (table_name, where_sql, list(exclude_columns)))
    # 查询原始库表的数据
    select_sql = 'select * from %s %s' % (table_name, where_sql)
    originCursor.execute(select_sql)
    origin_table_row_datas = originCursor.fetchall()
    if not origin_table_row_datas:
        print('原始库表无数据，不需要迁移')
        return None
    # 得到所有的列名，排除不需要迁移的列
    all_column_name = []
    for column_name in origin_table_row_datas[0].keys():
        if column_name.lower() not in exclude_columns:
            all_column_name.append(column_name)
    # 得到所有的待迁移的数据
    all_row_data = []
    for row in origin_table_row_datas:
        row_data = [row[column_name] for column_name in all_column_name]
        all_row_data.append(tuple(row_data))
    # 先删除目标库对应表，对应查询条件下的数据
    targetCursor.execute(select_sql)
    target_table_old_row_datas = targetCursor.fetchall()
    if target_table_old_row_datas:
        delete_sql = 'delete from %s %s' % (table_name, where_sql)
        delete_num = targetCursor.execute(delete_sql)
        print('目标库表数据对应查询条件下的数据不为空，先删除共%s条' % delete_num)
    # 把原始库表数据插入到目标库表
    insert_columns_sql = ','.join(all_column_name)
    placeholder_sql = ','.join(['%s' for i in range(len(all_column_name))])
    insert_sql = 'insert into %s (%s) values (%s)' % (table_name, insert_columns_sql, placeholder_sql)
    insert_num = targetCursor.executemany(insert_sql, all_row_data)
    print('表%s数据迁移完成，总共插入：%s条' % (table_name, insert_num))


if __name__ == '__main__':
    exclude_columns = 'id', 'create_by', 'create_time', 'update_by', 'update_time', 'is_valid'
    task1 = MigrateTask('cfg_global', 'where 1=1', *exclude_columns)
    task2 = MigrateTask('exception_board', 'where 1=1', *exclude_columns)
    do_table_data_migrate(task1, task2, originDbName='dev', targetDbName='local')
    # do_table_structure_migrate("cfg_global", "exception_board", originDbName='dev', targetDbName='local',
    #                            includeDatas=True)

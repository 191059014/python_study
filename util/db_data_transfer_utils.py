from mysql_utils import *

db_dev = get_db('dev')
db_sit = get_db('sit')
print("===============================================================")


def do_sync(*tasks):
    """
    同步表数据，支持多个
    :param tasks:表迁移所需要的参数
    """
    try:
        for task in tasks:
            _do_data_transfer(task.table_name, task.where_sql, task.exclude_columns)
            print("===============================================================")
    except BaseException as e:
        db_sit.rollback()
        print("发生异常，数据回滚完成，异常信息：%s" % e)
    else:
        db_sit.commit()
        print("事务提交完成")
    finally:
        db_dev.close()
        db_sit.close()
        print("关闭数据库连接完成")


class Task:
    """
    任务信息，封装数据迁移时候的参数
    """

    def __init__(self, table_name: str, where_sql: str, *exclude_columns) -> None:
        self.table_name = table_name
        self.where_sql = where_sql
        exclude_columns = [column_name.lower() for column_name in exclude_columns]
        self.exclude_columns = exclude_columns


def _do_data_transfer(table_name: str, where_sql: str, exclude_columns: list):
    """
    数据迁移
    :param table_name:表名
    :param where_sql: where条件语句
    :param exclude_columns: 排除的列
    """
    print('开始数据迁移，表：%s，查询条件：%s' % (table_name, where_sql))
    if not where_sql:
        print('条件语句不能为空')
        return None
    # 查询dev数据库的数据
    cursor_dev = get_dictcursor(db_dev)
    select_sql = 'select * from %s %s' % (table_name, where_sql)
    cursor_dev.execute(select_sql)
    dev_rows = cursor_dev.fetchall()
    if not dev_rows:
        print('dev无数据')
        return None
    # 得到所有的列名
    all_column_name = []
    for column_name in dev_rows[0].keys():
        if column_name.lower() not in exclude_columns:
            all_column_name.append(column_name)
    # 得到所有的数据
    all_row_data = []
    for row in dev_rows:
        row_data = [row[column_name] for column_name in all_column_name]
        all_row_data.append(tuple(row_data))
    # 先删除sit的原数据
    cursor_sit = get_cursor(db_sit)
    cursor_sit.execute(select_sql)
    sit_old_rows = cursor_sit.fetchall()
    if sit_old_rows:
        delete_sql = 'delete from %s %s' % (table_name, where_sql)
        delete_num = cursor_sit.execute(delete_sql)
        print('sit原表数据不为空，先删除共%s条' % delete_num)
    # 把dev的数据插入到sit
    insert_columns_sql = ','.join(all_column_name)
    placeholder_sql = ','.join(['%s' for i in range(len(all_column_name))])
    insert_sql = 'insert into %s (%s) values (%s)' % (table_name, insert_columns_sql, placeholder_sql)
    insert_num = cursor_sit.executemany(insert_sql, all_row_data)
    print('dev => sit 数据迁移完成，总共插入：%s条' % insert_num)


if __name__ == '__main__':
    task1 = Task('sys_user', 'where 1=1', 'id', 'create_time')
    task2 = Task('sys_permission', 'where 1=1', 'id', 'create_time')
    do_sync(task1, task2)

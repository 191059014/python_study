import pymysql


def get_db(env='dev'):
    """
    获取数据库连接
    :param env: 环境变量
    :return: 数据库连接
    """
    db_connect = None
    if env == 'dev':
        db_connect = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    elif env == 'test':
        db_connect = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    elif env == 'prod':
        db_connect = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    else:
        pass
    print("获取连接成功：%s" % db_connect.get_host_info())
    return db_connect


if __name__ == '__main__':
    db = get_db()
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute('select * from sys_user')
    for row in cursor.fetchall():
        print(row)
    try:
        sql_str = "INSERT INTO test.sys_user (user_name, password) VALUES (%s, %s)"
        records = [('zhangsan', '123456'), ('lisi', '123456'), ('wangwu', '123456')]
        r1 = cursor.executemany(sql_str, records)
        print("插入行数：%s" % r1)
    except BaseException as e:
        print("发生异常了：%s" % e)
        db.rollback()
        print("回滚事务完成")
    else:
        db.commit()
        print("提交事务完成")
    finally:
        cursor.close()
        db.close()
        print("关闭连接完成")

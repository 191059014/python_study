import pymysql


def get_db(env='local') -> pymysql.Connection:
    """
    获取数据库连接
    :param env: 环境变量
    :return: 数据库连接
    """
    db_connection = None
    if env == 'local':
        db_connection = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    elif env == 'dev':
        db_connection = pymysql.connect(host="localhost", database="platform", user="root", password="root3306")
    elif env == 'sit':
        db_connection = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    elif env == 'prod':
        db_connection = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    else:
        pass
    if db_connection:
        print("获取数据库连接成功：%s" % db_connection.get_host_info())
    else:
        print("获取数据库连接失败：%s" % env)
    return db_connection


def get_dictcursor(db_connect: pymysql.Connection) -> pymysql.cursors.DictCursor:
    """
    获取字典类型的游标
    :param db_connect: 数据库连接
    :return: 游标对象
    """
    return db_connect.cursor(cursor=pymysql.cursors.DictCursor)


def get_cursor(db_connect: pymysql.Connection) -> pymysql.cursors.Cursor:
    """
    获取元祖类型的游标
    :param db_connect: 数据库连接
    :return: 游标对象
    """
    return db_connect.cursor()


if __name__ == '__main__':
    pass

import pymysql


def get_dictcursor(db: pymysql.Connection):
    """
    字典型游标
    :param db:数据库连接
    :return: 游标对象
    """
    return db.cursor(cursor=pymysql.cursors.DictCursor)


def get_cursor(db: pymysql.Connection):
    """
    普通游标
    :param db:数据库连接
    :return: 游标对象
    """
    return db.cursor()


def get_db(env='dev'):
    """
    获取数据库连接
    :param env: 环境变量
    :return: 数据库连接
    """
    db_connect = None
    if env == 'dev':
        db_connect = pymysql.connect(host="localhost", database="platform", user="root", password="root3306")
    elif env == 'sit':
        db_connect = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    elif env == 'prod':
        db_connect = pymysql.connect(host="localhost", database="test", user="root", password="root3306")
    else:
        pass
    print("获取连接成功：%s" % db_connect.get_host_info())
    return db_connect

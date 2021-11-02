from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.engine import CursorResult, Engine
from sqlalchemy.orm import Session


class MysqlUtil():
    """
    mysql工具类
    """
    __instance = None
    __engine = None

    def __new__(cls) -> Any:
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        if not self.__engine:
            host = 'localhost'
            port = 3306
            database = 'test'
            username = 'root'
            password = 'root3306'
            db_connection = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(username, password, host, port, database)
            self.__engine = create_engine(db_connection, pool_size=100)
        self.db_session = Session(bind=self.__engine)

    def get_engine(self) -> Engine:
        """
        获取engine
        :return: engine
        """
        return self.__engine

    def execute(self, sql: str, params: tuple = None) -> CursorResult:
        """
        执行原生sql语句
        :param sql: sql语句
        :param params: 参数
        :return: 结果
        """
        session = self.db_session
        try:
            result = session.execute(sql, params)
            session.commit()
            print('db execute success')
            return result
        except Exception as e:
            session.rollback()
            print('db execute error, sql=%s, params=%s, rollback complete, error=%s' % (sql, params, e))
        finally:
            session.close()

    def insert(self, obj):
        session = self.db_session
        try:
            result = session.add(obj)
            session.commit()
            print('db insert success')
            return result
        except Exception as e:
            session.rollback()
            print('db insert error, obj=%s, rollback complete, error=%s' % (obj, e))
        finally:
            session.close()

from typing import Any

from sqlalchemy import create_engine
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
            self.__engine = create_engine(db_connection, pool_size=100, echo=True)
        self.db_session = Session(bind=self.__engine)

    def insert(self, obj) -> None:
        """
        插入
        :param obj:对象
        :return:
        """
        session = self.db_session
        try:
            session.add(obj)
            session.commit()
            print('db insert success')
        except Exception as e:
            session.rollback()
            print('db insert error, error=%s' % e)
        finally:
            session.close()

    def batch_insert(self, objs: list) -> None:
        """
        批量插入
        :param objs:对象列表
        """
        session = self.db_session
        try:
            session.add_all(objs)
            session.commit()
            print('db batch insert success')
        except Exception as e:
            session.rollback()
            print('db batch insert error, error=%s' % e)
        finally:
            session.close()

    def merge(self, obj) -> None:
        """
        更新或插入，取决于primary key
        :param obj: 对象
        """
        session = self.db_session
        try:
            result = session.merge(obj)
            session.commit()
            print('db merge success')
            return result
        except Exception as e:
            session.rollback()
            print('db merge error, error=%s' % e)
        finally:
            session.close()

    def delete_by_ids(self, cls, *ids) -> None:
        """
        通过id批量删除
        :param cls: 类
        :param ids: id元祖
        """
        session = self.db_session
        try:
            session.query(cls).filter(cls.id.in_(ids)).delete()
            session.commit()
            print('db delete success')
        except Exception as e:
            session.rollback()
            print('db delete error, error=%s' % e)
        finally:
            session.close()

    def query_first(self, cls, **conditions):
        """
        根据条件查询单条记录
        :param cls: 类，例如：User
        :param conditions集合，例如：user_name='zhangsan'
        :return 对象列表
        """
        session = self.db_session
        try:
            return session.query(cls).filter_by(**conditions).first()
        except Exception as e:
            print('db query first error, error=%s' % e)
        finally:
            session.close()

    def query_by_obj(self, cls, obj, orderBy=None, offset=None, limit=None):
        """
        根据对象查询
        :param cls: 类，例如：User
        :param obj: 查询条件对象
        :param orderBy: 排序，例如：User.create_by.desc()
        :param offset 查询起始位置，从0开始
        :param limit 查询条数
        :return 对象列表
        """
        obj_dict = obj.__dict__
        obj_dict.pop('_sa_instance_state')
        return self.query_by_condition(cls, orderBy=orderBy, offset=offset, limit=limit, **obj_dict)

    def query_by_condition(self, cls, orderBy=None, offset=None, limit=None, **conditions):
        """
        根据条件查询
        :param cls: 类，例如：User
        :param orderBy: 排序，例如：User.create_by.desc()
        :param offset 查询起始位置，从0开始
        :param limit 查询条数
        :param conditions集合，例如：user_name='zhangsan'
        :return 对象列表
        """
        session = self.db_session
        try:
            return session.query(cls).filter_by(**conditions).order_by(orderBy).offset(offset).limit(limit)
        except Exception as e:
            print('db query by condition error, error=%s' % e)
        finally:
            session.close()

    def query_by_criterion(self, cls, *criterion, orderBy=None, offset=None, limit=None):
        """
        根据条件查询
        :param cls: 类，例如：User
        :param orderBy: 排序，例如：User.create_by.desc()
        :param offset 查询起始位置，从0开始
        :param limit 查询条数
        :param criterion: 条件集合，例如：User.id.in_(7, 8)、User.name.like("user%")、User.age == 20
        :return 对象列表
        """
        session = self.db_session
        try:
            return session.query(cls).filter(*criterion).order_by(orderBy).offset(offset).limit(limit)
        except Exception as e:
            print('db query by criterion error, error=%s' % e)
        finally:
            session.close()

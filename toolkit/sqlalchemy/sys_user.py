from operator import and_

from sqlalchemy import Column, String

from toolkit.sqlalchemy.base import BaseDO
from toolkit.sqlalchemy.db import MysqlUtil


class SysUser(BaseDO):
    __tablename__ = 'sys_user'
    user_name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return repr(self.__dict__)


def insert(dbutils: MysqlUtil):
    user = SysUser()
    user.user_name = 'zhangsan123111'
    user.password = '12321'
    user.create_by = 'zhangsan'
    user.update_by = 'zhangsan11'
    dbutils.insert(user)


def query_by_condition_1(dbutils: MysqlUtil):
    res = dbutils.query_by_condition(SysUser, id=7)
    if res:
        for user in res:
            print(user)


def query_by_condition_2(dbutils: MysqlUtil):
    res = dbutils.query_by_condition(SysUser, orderBy=SysUser.create_by.desc(), offset=2, limit=3, create_by='zhangsan')
    if res:
        for user in res:
            print(user)


def query_first(dbutils: MysqlUtil):
    user = dbutils.query_first(SysUser, create_by='zhangsan')
    print(user)


def query_by_criterion_1(dbutils: MysqlUtil):
    res = dbutils.query_by_criterion(SysUser, SysUser.id.in_([7, 8, 19]), SysUser.create_by.like('zhang123%'),
                                     orderBy=SysUser.create_by.desc(), offset=0, limit=10)
    if res:
        for user in res:
            print(user)


def query_by_criterion_2(dbutils: MysqlUtil):
    res = dbutils.query_by_criterion(SysUser, and_(SysUser.id.in_([7, 8, 19]), SysUser.create_by.like('zhang123%')),
                                     orderBy=SysUser.create_by.desc(), offset=0, limit=10)
    if res:
        for user in res:
            print(user)


if __name__ == '__main__':
    db_utils = MysqlUtil()
    query_by_criterion_2(db_utils)

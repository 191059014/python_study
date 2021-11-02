from sqlalchemy import Column, String, Integer

from toolkit.sqlalchemy_demo.base import BaseDO, Base
from toolkit.sqlalchemy_demo.db import MysqlUtil


class SysUser(BaseDO):
    __tablename__ = 'sys_user'
    user_name = Column(String(32), nullable=False, comment='用户名')
    password = Column(String(64), nullable=False, comment='用户名')
    tenant_id = Column(Integer, nullable=False, comment='用户名')


if __name__ == '__main__':
    db_utils = MysqlUtil()
    # user = SysUser()
    # user.user_name = 'zhangsan123'
    # user.password = '123'
    # user.tenant_id = 1
    # user.create_by = 'huangbiao'
    # user.update_by = 'huangbiao'
    # res = db_utils.insert(user)
    # print(res)
    Base.metadata.create_all(db_utils.get_engine())

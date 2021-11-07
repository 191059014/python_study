from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseDO(Base):
    """
    基础数据模型字段
    """
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='主键自增ID')
    create_by = Column(String(32), comment='创建人')
    create_time = Column(DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_by = Column(String(32), comment='修改人')
    update_time = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now(), comment='修改时间')
    is_valid = Column(Integer, default=1, comment='记录有效状态')

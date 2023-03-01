from sqlalchemy import Column, String, create_engine, Integer, DateTime,Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  relationship
from sqlalchemy import ForeignKey
# 创建对象的基类:
Base = declarative_base()

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')

Base = declarative_base((engine))
Session = sessionmaker(engine)
session = Session()



# 定义User对象:
class CUSTOMER(Base):
    # 表的名字:
    __tablename__ = 'Customer'
    # 表的结构:
    CID = Column(String(256),primary_key=True)
    Cname  = Column(String(256))
    passwd = Column(String(256))
    crank = Column(Float)
    imagestr = Column(String(256))
    flag = Column(Integer)
    
class MODULE(Base):
    __tablename__ = 'module'
    # 表的结构:
    MOID = Column((Integer),primary_key=True)
    MOname  = Column(String(256))
class FORUM(Base):
    # 表的名字:
    __tablename__ = 'forum'
    # 表的结构:
    FID = Column(String(256),primary_key=True)
    Finf  = Column(String())
    good =  Column(Integer)
    CID = Column(String(256))
    Frank = Column(String(256))
    title = Column(String(256))
    MOID = Column(Integer)
    cnumber = Column(Integer)
    date = Column(DateTime)
    lastestUID = Column(String(256))
    lastestTime = Column(DateTime)
    views = Column(Integer)
class COMMENT(Base):
    # 表的名字:
    __tablename__ = 'Comment'
    # 表的结构:
    COID = Column(String(256),primary_key=True)
    COinf  = Column(String())
    FID = Column(String(256))
    CID = Column(String(256))
    date = Column(DateTime)
class ADMINISTRATOR(Base):
    # 表的名字:
    __tablename__ = 'Administrator'
    # 表的结构:
    AdID = Column(String(256),primary_key=True)
    Adname  = Column(String(256))
    Adpasswd = Column(String(256))


class SESSION(Base):
    # 表的名字:
    __tablename__ = 'session'
    # 表的结构:
    sid = Column(String(256),primary_key=True)
    Cname  = Column(String(256))
    dt = Column(DateTime)

class BAN(Base):
    # 表的名字:
    __tablename__ = 'ban'
    # 表的结构:
    Cname = Column(String(256),primary_key=True)
    bt = Column(DateTime)

class COLLECTION(Base):
    __tablename__ = 'collection'
    # 表的结构:
    ctid = Column(Integer,primary_key=True)
    Cname = Column(String(256))
    FID = Column(String(245))
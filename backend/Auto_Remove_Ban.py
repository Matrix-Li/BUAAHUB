from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION
from SQLA import ADMINISTRATOR,BAN
from flask import request
from JsonWrap import jsonwrap
import datetime ,time
import pymysql
from Login import generate_random_str

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def auto_remove_ban():
    try:
        records=dataforum.query(BAN).filter(BAN.Cname!=None).all()
        Len = len(records)
        for i in range(0,Len):
            record=records[i]
            thisbt=record.bt
            nowbt=datetime.datetime.now()
            subdt = (nowbt - thisbt).days
            if(subdt>=1):
                cname = record.Cname
                user = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==cname).first()       
                dataforum.query(BAN).filter(BAN.Cname==cname).delete()
                user.flag=1
                dataforum.commit()
        dataforum.close()
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
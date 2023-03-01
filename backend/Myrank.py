from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION,COMMENT,MODULE
from flask import request
from JsonWrap import jsonwrap
import datetime ,time
import pymysql
from Login import generate_random_str


engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time

def myrank(SID):
    try:
        answer=[]
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again222222.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        personq = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(personq)==0)):
            dataforum.close()
            return jsonwrap(1, "Pelease check again11111.", res)
        person = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        cname = person.Cname
        
        res['rank'] = str(int(person.crank))    #用户的级别

        
        return jsonwrap(0, "success.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)     
    finally:
        dataforum.commit()
        dataforum.close()   

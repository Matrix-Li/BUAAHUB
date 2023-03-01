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
from Forum_Show import time_change

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def customer_show(SID):
    try:
        res=[]
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').all()
        if ((len(ans)==0)):
            return jsonwrap(1, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').first()
        if(ans == None):
            return jsonwrap(1,"sid不存在",res)    
        Aname = ans.Adname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname=="root",SESSION.sid==SID).first()
        if  (thissession == None):
            return jsonwrap(2, "Pelease Login again", res)
        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            dataforum.commit()
            return jsonwrap(3, "Pelease Login again.", res)
        thissession.dt = nowdt
        dataforum.commit()

        not_ban_customer=dataforum.query(CUSTOMER).filter(CUSTOMER.CID!='0',CUSTOMER.flag==1).all()
        not_ban=[]
        ban=[]
        Len=len(not_ban_customer)
        for i in range(0,Len):
            customer=not_ban_customer[i]
            thread = {"ID": customer.CID, "Cname": customer.Cname, "rank": customer.crank, "flag":customer.flag,"lastTime":time_change(thisdt)}
            not_ban.append(thread)
        ban_customer=dataforum.query(CUSTOMER).filter(CUSTOMER.CID!='0',CUSTOMER.flag==0).all()
        Len=len(ban_customer)
        for i in range(0,Len):
            customer=ban_customer[i]
            thread = {"ID": customer.CID, "Cname": customer.Cname, "rank": customer.crank, "flag":customer.flag,"lastTime":time_change(thisdt)}
            ban.append(thread)
        res.append(not_ban)
        res.append(ban)
        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
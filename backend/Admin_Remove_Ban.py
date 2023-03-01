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

def admin_remove_ban(CID_C,SID):
    try:
        res={}
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').all()
        if ((len(ans)==0)):
            return jsonwrap(1, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').first()
        if(ans == None):
            return jsonwrap(1,"sid不存在",res)
        Aname = ans.Adname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname==Aname,SESSION.sid==SID).first()
        if  (thissession==None):
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


        user = dataforum.query(CUSTOMER).filter(CUSTOMER.CID == CID_C).first()
        if(user.flag==1):
            return jsonwrap(4,"The user was not banned",res)
        user.flag = 1
        cname=user.Cname
        dataforum.query(BAN).filter(BAN.Cname==cname).delete()
        dataforum.commit()
        dataforum.close()

        res['CID'] = CID_C
        res['Cname'] = cname
        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
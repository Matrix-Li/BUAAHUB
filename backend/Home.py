from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,MODULE,SESSION
from flask import request
from JsonWrap import jsonwrap
import pymysql
import datetime ,time

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time

def home(SID):
    try:
        res=[]

        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        
        ansp = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(ansp)==0)):
            dataforum.close()
            return jsonwrap(1, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        cname = ans.Cname

        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            dataforum.commit()
            dataforum.close()
            return jsonwrap(3, "Pelease Login again.", res)
        thissession.dt = nowdt
        dataforum.commit()


        sum = dataforum.query(FORUM).filter(FORUM.FID != "0000").count()
        allforum = dataforum.query(FORUM).filter(FORUM.FID != "0000").all()
        if (sum==0):
            return jsonwrap(8, "empty.", res)
        for i in range (0,sum):
            help = allforum[i]

            moid = help.MOID
            temp = dataforum.query(MODULE).filter(MODULE.MOID == moid).first()
            Author = dataforum.query(CUSTOMER).filter(CUSTOMER.CID == help.CID).first()
            mona = temp.MOname
            temp_res = {}
            
            temp_res["module_name"] = mona                          #论贴所属的板块名称
            temp_res["module_id"] = temp.MOID                       #论贴所属的板块ID                
            temp_res["title"] = help.title                          #论贴的标题
            temp_res["FID"] = help.FID                              #论贴的标题
            temp_res["date"] = time_change(help.date)               #论贴发布的日期
            
            
            res.append(temp_res)
        dataforum.close()
        return jsonwrap(0, "success.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()

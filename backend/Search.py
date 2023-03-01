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
import pymysql
from Forum_Show import time_change

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def search(SID):
    try:
        res=[]
        tmp = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if(tmp == None):
            res={'sid':SID}
            return jsonwrap(1,"sid不存在",res)
        tmpname = tmp.Cname
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==tmpname).all()
        if ((len(ans)==0)):
            return jsonwrap(1, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==tmpname).first()
        cname = ans.Cname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname==cname,SESSION.sid==SID).first()
        if  (thissession==None):
            return jsonwrap(2, "Pelease Login again.", res)
        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            dataforum.commit()
            return jsonwrap(3, "Pelease Login again.", res)
        thissession.dt = nowdt
        dataforum.commit()

        content = request.args.get('con')
        if(content==None):
            return jsonwrap(8,"empty",res)
        forums=dataforum.query(FORUM).filter(FORUM.Finf.like("%"+content+"%") | FORUM.title.like("%"+content+"%")).all()
        Len = len(forums)
        msg={"Cname":cname}
        res.append(msg)
        inf = []
        for i in range(0,Len):
            forum=forums[i]
            tmpcid=forum.CID
            tmpcustomer = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==tmpcid).first()
            if(tmpcustomer == None):
                return jsonwrap(8,"empty",res)
            lastestID = forum.lastestUID
            lastcustomer = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==lastestID).first()
            if(lastcustomer == None):
                thread = {"ID": forum.FID, 
                        "info": forum.Finf, 
                        "likeCnt": forum.good, 
                        "time": time_change(forum.date),
                        "MOID":forum.MOID,"title":forum.title,
                        "commentnumber":forum.cnumber,
                        "author":tmpcustomer.Cname,
                        "views":forum.views,
                        "lastestname":tmpcustomer.Cname,
                        "lastestTime":time_change(forum.date),
                        }
            else:
                thread = {"ID": forum.FID, 
                        "info": forum.Finf, 
                        "likeCnt": forum.good, 
                        "time": time_change(forum.date),
                        "MOID":forum.MOID,
                        "title":forum.title,
                        "commentnumber":forum.cnumber,
                        "lastestname":lastcustomer.Cname,
                        "lastestTime":time_change(forum.lastestTime),
                        "author":tmpcustomer.Cname,
                        "views":forum.views}    
            inf.append(thread)
        res.append(inf)
        dataforum.close()
        return jsonwrap(0, "ok", res)
    except Exception as e:
        error={}
        dataforum.commit()
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
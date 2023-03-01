#显示这个模块里的所有论贴
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

def mycomment(SID):
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

        mod = dataforum.query(FORUM).filter(FORUM.CID==CID_C).first()

        allforum = dataforum.query(COMMENT).filter(COMMENT.CID==CID_C).all()

        Len = len(allforum)

        
        for i in range(Len):
            tempfroum = allforum[i]

            temp_post = dataforum.query(FORUM).filter(FORUM.FID==tempfroum.FID).first()
            temp_res={}  
            temp_res["information"] = tempfroum.COinf               #评论内容  
            temp_res["title"] = temp_post.title                     #论贴的标题
            temp_res["FID"] = temp_post.FID                         #论贴的标题
            temp_res["date"] = time_change(tempfroum.date)          #评论创建的时间
            res.append(temp_res)

        dataforum.close()
        return jsonwrap(0, "success.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
        
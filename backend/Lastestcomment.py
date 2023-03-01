from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION,COMMENT
from flask import request
from JsonWrap import jsonwrap
import datetime ,time
import pymysql
from Login import generate_random_str
from functools import cmp_to_key

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def return_int(s):
    Len=len(s)
    a = 0
    for i in range(Len):
        a=a*10+ord(s[i])-ord('0')
    return a

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time
def cmpp(x,y):
    return time_change(y.COID-x.COID)
def lastestcomment(SID,FID):
    try:
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(ans)==0)):
            dataforum.close()
            return jsonwrap(1, "Pelease check again.", res)

        
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        cname = ans.Cname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname==cname,SESSION.sid==SID).first()
        
        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            dataforum.commit()
            dataforum.close()
            return jsonwrap(3, "Pelease Login again.", res)
        newstr = generate_random_str()
        thissession.dt = nowdt
        dataforum.commit()


        comment_arry = dataforum.query(COMMENT).filter(COMMENT.FID==FID).all()
        if(comment_arry==None):
            dataforum.close()
            return jsonwrap(4, "no comment.", res)
        comment = comment_arry[0]
        Lenn = len(comment_arry)
        for i in range(1,Lenn):
            if(return_int(comment.COID)<return_int(comment_arry[i].COID)):
                comment=comment_arry[i]
        Author = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==comment.CID).first()
        res["COID"] = comment.COID              #评论ID
        res["COinf"] = comment.COinf            #评论信息
        res["CID"] = comment.CID                #创建评论的用户ID
        res["Author"] = Author.Cname            #创建评论的用户名字
        res["date"] = time_change(comment.date) #创建评论的日期
        dataforum.close()

        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
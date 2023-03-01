from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION
from flask import request
from JsonWrap import jsonwrap
import datetime ,time
import pymysql
from Login import generate_random_str

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

def create(CID_C,SID):
    try:
        res={}
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(ans)==0)):
            return jsonwrap(1, "Pelease check again.", res)
        note = request.args.get('note')      #论贴信息
        title = request.args.get('title')    #论贴级别
        temprank = request.args.get('rank')  #
        rank = return_int(temprank)
        if (note==None):
            return jsonwrap(2, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        cname = ans.Cname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname==cname,SESSION.sid==SID).first()
        if  (thissession==None):
            return jsonwrap(3, "Pelease Login again.", res)
        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            return jsonwrap(4, "Pelease Login again.", res)
        if(ans.flag == 0):
            return (5,"You have been limited.",res)
        if(ans.crank<rank):
            return (6,"rank wrong",res)
        
        newstr = generate_random_str()
        thissession.sid = newstr
        thissession.dt = nowdt
        dataforum.commit()
        

        a = dataforum.query(func.count('*')).select_from(FORUM).scalar()
        a = a + 1
        Forum_cid = str(a)
        newone = FORUM(FID=str(Forum_cid), Finf=note ,  good = 0, CID = CID_C, Frank = 1, MOID = 0,title = title,cnumber = 0,date = nowdt)
        dataforum.add(newone)
        dataforum.commit()
        ans.crank=ans.crank+0.1
        dataforum.commit()

        res['FID'] = Forum_cid                  #论贴的ID
        res['Finf'] = note                      #论贴的内容
        res['good'] = "0"                       #论贴的点赞数量
        res['CID'] = CID_C                      #创建论贴的用户ID
        res['Frank'] = temprank                 #论贴的级别
        res["MOID"] = "0"                       #论贴所属的模块ID
        res['SID'] = newstr                     #更新SID
        res['Crank'] = str(int(ans.crank))      #创建论贴的用户级别
        res['title'] = title                    #论贴的标题
        res['cname'] = ans.Cname                #创建论贴的用户ID
        res['cnumber'] = "0"                    #论贴的评论数目
        res['date'] = time_change(nowdt)        #论贴的创建时间
        dataforum.close()

        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
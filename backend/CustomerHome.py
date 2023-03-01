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

def customerhome(SID):
    try:
        answer=[]
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        personq = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(personq)==0)):
            dataforum.close()
            return jsonwrap(1, "Pelease check again.", res)
        person = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        cname = person.Cname
        
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

        res['cname'] = person.Cname             #用户的姓名
        res['password'] = person.passwd         #用户的密码
        res['rank'] = str(int(person.crank))    #用户的级别

        allforum = dataforum.query(FORUM).filter(FORUM.CID==person.CID).all()

        Len = len(allforum)
        if(Len == 0):
            answer.append(res)
            dataforum.close()
            return jsonwrap(0, "success.", answer)
            
        post = []
        for i in range(0,Len):
            tempfroum = allforum[i]
            temp = dataforum.query(MODULE).filter(MODULE.MOID == tempfroum.MOID).first()
            temp_people = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==tempfroum.lastestUID).first()
            mona = temp.MOname
            temp_res = {}
            temp_res["FID"] = tempfroum.FID                             #论贴的ID
            temp_res["Finf"] = tempfroum.Finf                           #论贴的内容
            temp_res["Fgood"] = str(tempfroum.good)                     #论贴的点赞数目
            temp_res["module_name"] = mona                              #论贴所属的板块名称
            temp_res["title"] = tempfroum.title                         #论贴的标题
            temp_res["cnumber"] = tempfroum.cnumber                     #论贴的评论数目
            temp_res["date"] = time_change(tempfroum.date)              #论贴发布的日期
            temp_res["create_time"] = tempfroum.date                    #论贴创建的时间
            temp_res["views"] = tempfroum.views                         #论贴浏览的次数
            temp_res['lastestUID'] = tempfroum.lastestUID                    #最后一次评论的用户ID
            temp_res['lastestTime'] = time_change(tempfroum.date)            #最后一次评论的时间
            temp_res['lastestname'] = person.Cname                      #最后一次评论的人名
            if(temp_people!=None):                                           #判断是否存在评论
                temp_res['lastestUID'] = tempfroum.lastestUID                     #最后一次评论的用户ID
                temp_res['lastestname'] = temp_people.Cname                  #最后一次评论的人名
                temp_res['lastestTime'] = time_change(tempfroum.lastestTime)      #最后一次评论的时间
            
            post.append(temp_res)

        answer.append(res)
        answer.append(post)
        dataforum.close()
        return jsonwrap(0, "success.", answer)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)     
    finally:
        dataforum.commit()
        dataforum.close()   

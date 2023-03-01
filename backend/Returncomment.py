#查看一个具体的论贴
from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION,COMMENT,MODULE,COLLECTION
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

def returncomment(SID):
    try:
        answer=[]
        res={}
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

        allforum = dataforum.query(COMMENT).filter(COMMENT.CID==CID_C).all()
        Len = len(allforum)

        if Len==0:
            dataforum.close()
            return jsonwrap(4, "nothing.", answer)

        for i in range(Len):
            tempcus = allforum[i]
            tempfroum = dataforum.query(FORUM).filter(FORUM.FID==tempcus.FID).first()
            mod = dataforum.query(MODULE).filter(MODULE.MOID==tempfroum.MOID).first()
            thiscustomer = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==tempfroum.CID).first()
            temp_people = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==tempfroum.lastestUID).first()
            temp_res={}
            temp_com={}
            temp_help=[]
            temp_com['coinf'] = tempcus.COinf                       #评论的信息
            temp_com['date'] = time_change(tempcus.date)            #评论的时间

            temp_res["FID"] = tempfroum.FID                         #论贴ID
            temp_res["Finf"] = tempfroum.Finf                       #论贴内的信息
            temp_res["CID"] = tempfroum.CID                         #论贴创建者的ID
            temp_res["good"] = str(tempfroum.good)                  #点赞的数目
            temp_res["module_name"] = mod.MOname                    #论贴所属板块的名称
            temp_res["module_id"] = mod.MOID                        #论贴所属的板块ID   
            temp_res["title"] = tempfroum.title                     #论贴的标题
            temp_res["author"] = thiscustomer.Cname                 #论贴的创建者的名字
            temp_res["views"] = tempfroum.views                     #论贴的创建者的名字
            temp_res["cnumber"] = tempfroum.cnumber                 #论贴被评价的次数
            temp_res["date"] = time_change(tempfroum.date)          #论贴创建的时间
            temp_res['lastestUID'] = tempfroum.lastestUID           #最后一次评论的用户ID
            temp_res['lastestTime'] = time_change(tempfroum.date)   #最后一次评论的时间
            temp_res['lastestname'] = thiscustomer.Cname            #最后一次评论的人名
            temp_res['lastestUID'] = tempfroum.lastestUID           #最后一次评论的用户ID
            temp_res['lastestTime'] = time_change(tempfroum.date)   #最后一次评论的时间
            temp_res['lastestname'] = thiscustomer.Cname            #最后一次评论的人名
            if(temp_people!=None):                                              #判断是否存在评论
                temp_res['lastestUID'] = tempfroum.lastestUID                   #最后一次评论的用户ID
                temp_res['lastestname'] = temp_people.Cname                     #最后一次评论的人名
                temp_res['lastestTime'] = time_change(tempfroum.lastestTime)    #最后一次评论的时间
            temp_help.append(temp_res)
            temp_help.append(temp_com)
            answer.append(temp_help)

        dataforum.close()
        return jsonwrap(0, "succes.", answer)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
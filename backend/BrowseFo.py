#查看一个具体的论贴
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

def browsefo(SID,FID):
    try:
        answer=[]
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        ansq = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(ansq)==0)):
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
        

        thisfo = dataforum.query(FORUM).filter(FORUM.FID==FID).first()
        if(ans.crank<thisfo.Frank):
            dataforum.close()
            return jsonwrap(4, "您的等级不足,阅读此贴需要等级达到"+str(thisfo.Frank)+",您的当前等级为"+str(int(ans.crank)), res)

        review=[]
        allcomment = dataforum.query(COMMENT).filter(COMMENT.FID==FID).all()
        Len = len(allcomment)
        for i in range(Len):
            comment_man = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==allcomment[i].CID).first()
            temp_res={}
            temp_res['COID'] = allcomment[i].COID                           #评论ID
            temp_res['Coinf'] = allcomment[i].COinf                         #评论信息
            temp_res['comment_man_name'] = comment_man.Cname                #评论者的名字
            temp_res['comment_man_ID'] = comment_man.CID                    #评论者的ID
            temp_res['comment_date'] = time_change(allcomment[i].date)      #评论的时间
            review.append(temp_res)

        
        Author = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==thisfo.CID).first()
        mod = dataforum.query(MODULE).filter(MODULE.MOID==thisfo.MOID).first()
        
        thisfo.views = thisfo.views + 1
        dataforum.commit()
        temp_people = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==thisfo.lastestUID).first()
        res['FID'] = thisfo.FID                                 #论贴ID
        res['Finf'] = thisfo.Finf                               #论贴内容
        res['good'] = str(thisfo.good)                          #点赞数量
        res['CID'] = thisfo.CID                                 #创建论贴的用户ID
        res['Frank'] = str(thisfo.Frank)                        #该论贴的级别
        res["module_id"] = str(thisfo.MOID)                     #该论贴的所属模块ID
        res["title"] = thisfo.title                             #论贴标题
        res['author'] = Author.Cname                            #论贴的作者名字
        res['module_name'] = mod.MOname                         #论贴所属的模块名字
        res['date'] = time_change(thisfo.date)                  #论贴的创建时间
        res['views'] = thisfo.views                             #论贴的浏览次数
        res['lastestUID'] = thisfo.lastestUID                   #最后一次评论的用户ID
        res['lastestTime'] = time_change(thisfo.date)           #最后一次评论的时间
        res['lastestname'] = Author.Cname                       #最后一次评论的人名
        if(temp_people!=None):                                  #判断是否存在评论
            res['lastestUID'] = thisfo.lastestUID                   #最后一次评论的用户ID
            res['lastestname'] = temp_people.Cname                  #最后一次评论的人名
            res['lastestTime'] = time_change(thisfo.lastestTime)    #最后一次评论的时间

        answer.append(res)
        answer.append(review)
        dataforum.close()
        return jsonwrap(0,"success",answer)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
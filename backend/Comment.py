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
import datetime ,time

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time
def return_int(s):
    Len=len(s)
    a = 0
    for i in range(Len):
        a=a*10+ord(s[i])-ord('0')
    return a

def comment(SID,FID):
    try:
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        person = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        note= request.args.get('comment')
        if(note=='' or note==None):
            dataforum.close()
            return jsonwrap(8,"empty.",res)
        if ((len(person)==0)):
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
        if(person.flag == 0):
            dataforum.close()
            return jsonwrap(4,"You are not allow to post.",res)


        ast = dataforum.query(COMMENT).all()
        sum = 1
        ast_sum = len(ast)
        if(ast==None):
            a=1
        else:
            for i in range(ast_sum):
                if(sum <= return_int(ast[i].COID)):
                    sum = return_int(ast[i].COID) + 1 

        newcomment = COMMENT(COID=str(sum),COinf=note,FID=FID,CID=CID_C,date=nowdt)
        dataforum.add(newcomment)
        dataforum.commit()
        person.crank=person.crank+0.5
        dataforum.commit()

        thisfo = dataforum.query(FORUM).filter(FORUM.FID==FID).first()
        thismo = dataforum.query(MODULE).filter(MODULE.MOID==thisfo.MOID).first()
        thisfo.cnumber = thisfo.cnumber + 1
        thisfo.lastestUID = CID_C
        thisfo.lastestTime = nowdt
        dataforum.commit()

        res['COID']=str(sum)                    #评论的ID
        res['COinf']=note                       #评论的信息
        res['FID']=FID                          #评论的论贴ID
        res['CID']=CID_C                        #评论者的ID
        res['Crank'] = str(int(person.crank))   #用户级别
        res['Finf'] = thisfo.Finf               #论贴信息
        res['good'] = thisfo.good               #论贴点赞数量
        res['title'] = thisfo.title             #论贴标题
        res['Frank'] = thisfo.Frank             #论贴级别
        res['MOID'] = thismo.MOname             #论贴所属模块的名字

        dataforum.close()
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(10,str(e),error)
    finally:
        dataforum.commit()
        dataforum.close()


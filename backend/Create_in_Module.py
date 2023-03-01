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

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time

def return_int(s):
    Len=len(s)
    a = 0
    for i in range(Len):
        a=a*10+ord(s[i])-ord('0')
    return a

def create_in_module(SID,MOID):
    try:
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(3, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID
        if(return_int(CID_C)!=0 and return_int(MOID)==5):
            dataforum.close()
            return jsonwrap(9, "You are not Admin.", res)
        ans = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        if (ans==None):
            dataforum.close()
            return jsonwrap(1, "Pelease check again.", res)

        note = request.args.get('note')
        title = request.args.get('title')
        temprank = request.args.get('rank')
        if(note==None or title==None or temprank==None or note=='' or title=='' ):
            dataforum.close()
            return jsonwrap(8, "empty.", res)

        rank = return_int(temprank)
        if (note==None):
            dataforum.close()
            return jsonwrap(2, "Pelease check again.", res)

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
            return jsonwrap(4, "Pelease Login again.", res)
        if(ans.flag == 0):
            dataforum.close()
            return jsonwrap(5,"You are not allow to post.",res)
        
        if(ans.crank<rank):
            dataforum.close()
            return jsonwrap(6,"rank wrong",res)

        thissession.dt = nowdt
        dataforum.commit()
        

        ast = dataforum.query(FORUM).all()
        a = 1
        ast_sum = len(ast)
        if(ast==None):
            a=1
        else:
            for i in range(ast_sum):
                if(a <= return_int(ast[i].FID)):
                    a = return_int(ast[i].FID) + 1 
        
        Forum_cid = str(a)
        newone = FORUM(FID=str(Forum_cid), Finf=note ,  good = 0, CID = CID_C, Frank = rank, MOID = MOID, title=title , cnumber = 0, date = nowdt, views = 0,lastestUID = CID_C,lastestTime = nowdt)
        dataforum.add(newone)
        dataforum.commit()
        ans.crank=ans.crank+0.5
        dataforum.commit()

        res['FID'] = Forum_cid                  #论贴的ID
        res['Finf'] = note                      #论贴的内容
        res['good'] = "0"                       #论贴的点赞数量
        res['CID'] = CID_C                      #创建论贴的用户ID
        res['Frank'] = temprank                 #论贴的级别
        res["MOID"] = MOID                      #论贴所属的模块ID
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
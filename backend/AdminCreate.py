from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION
from SQLA import ADMINISTRATOR
from flask import request
from JsonWrap import jsonwrap
import datetime ,time
import pymysql
from Login import generate_random_str
from Forum_Show import time_change

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

def admincreate(SID):
    try:
        res={}
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').all()
        if ((len(ans)==0)):
            return jsonwrap(1, "Pelease check again.", res)
        note = request.args.get('note')
        title = request.args.get('title')
        if (note==None or title==None):
            return jsonwrap(4, "Pelease check again.", res)

        #===========================================================================
        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.AdID=='0').first()
        if(ans == None):
            return jsonwrap(1,"sid不存在",res)    
        Aname = ans.Adname
        thissession = dataforum.query(SESSION).filter(SESSION.Cname==Aname,SESSION.sid==SID).first()
        if  (thissession==None):
            return jsonwrap(2, "Pelease Login again", res)
        thisdt = thissession.dt
        nowdt = datetime.datetime.now()
        subdt = (nowdt - thisdt).seconds
        if(subdt>3600):
            dataforum.delete(thissession)
            dataforum.commit()            
            return jsonwrap(3, "Pelease Login again.", res)
        thissession.dt = nowdt
        dataforum.commit()

        ast = dataforum.query(FORUM).all()
        a = return_int(ast[-1].FID) + 1
        Forum_cid = str(a)
        newone = FORUM(FID=str(Forum_cid), Finf=note ,  good = 0, CID = '0', Frank = 1, MOID = 5, title=title , cnumber = 0, date = nowdt,views=0,lastestUID="0",lastestTime=nowdt)
        dataforum.add(newone)
        dataforum.commit()
        dataforum.close()

        res['FID'] = Forum_cid
        res['Finf'] = note
        res['good'] = "0"
        res['AdID'] = '0'
        res['Adname'] = 'root'
        res['Frank'] = "1"
        res['MOID'] = "5"
        res['Title']=title
        res['date'] =time_change(nowdt)
        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()    
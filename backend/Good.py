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

def good(SID,FID):
    try:
        res={}
        thissession = dataforum.query(SESSION).filter(SESSION.sid==SID).first()
        if  (thissession==None):
            dataforum.close()
            return jsonwrap(2, "Pelease Login again.", res)
        CNAME = thissession.Cname
        CID_C = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname==CNAME).first().CID

        ansq = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).all()
        if ((len(ansq)==0)):
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

        #thiscu =  dataforum.query(CUSTOMER).filter(CUSTOMER.CID==CID_C).first()
        #thisna = thiscu.Cname

        thisforum =  dataforum.query(FORUM).filter(FORUM.FID==FID).first()
    
        ans2 = dataforum.query(CUSTOMER).filter(CUSTOMER.CID==thisforum.CID).first()
        a = thisforum.good
        thisforum.good = thisforum.good + 1
        dataforum.commit()
        ans2.crank = ans2.crank+0.5
        dataforum.commit()
        
        res['FID'] = thisforum.FID                  #论贴的ID
        res['Finf'] = thisforum.Finf                #论贴的内容
        res['good'] = str(thisforum.good)           #论贴的点赞数
        res['CID'] = thisforum.CID                  #创建论贴的用户ID
        res['Frank'] = str(int(thisforum.Frank))    #论贴的级别
        res["module_id"] = thisforum.MOID           #论贴的模块ID
        res['crank'] = ans.crank                    #用户的级别

        dataforum.close()
        return jsonwrap(0, "success", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
        
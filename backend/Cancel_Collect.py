from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,SESSION,COLLECTION
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

def cancel_collect(SID,FID):
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
        
        tmptest = dataforum.query(FORUM).filter(FORUM.FID==FID).first()
        if(tmptest==None):
            return jsonwrap(4,"该帖子不存在",res)
        test = dataforum.query(COLLECTION).filter(COLLECTION.Cname ==cname, COLLECTION.FID ==FID).first()
        if(test==None):
            return jsonwrap(5,"The forum has not been collected",res)
        dataforum.query(COLLECTION).filter(COLLECTION.Cname == cname,COLLECTION.FID == FID).delete()
        dataforum.commit()

        
        res['Cname'] = cname
        res['FID'] = FID                  #论贴的ID
        dataforum.close()
        return jsonwrap(0, "success", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,str(e),error)
    finally:
        dataforum.commit()
        dataforum.close()
        
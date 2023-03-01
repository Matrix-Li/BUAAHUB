from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM,MODULE
from flask import request
from JsonWrap import jsonwrap
import pymysql
import datetime ,time

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def time_change(dtime):
    un_time = time.mktime(dtime.timetuple())
    return un_time

def cidhome(CID_C):
    try:
        res=[]
        sum = dataforum.query(FORUM).filter(FORUM.FID != "0000").count()


        for i in range (1,sum+1):
            help = dataforum.query(FORUM).filter(FORUM.FID == str(i)).first()
            moid = help.MOID
            temp = dataforum.query(MODULE).filter(MODULE.MOID == moid).first()
            Author = dataforum.query(CUSTOMER).filter(CUSTOMER.CID == help.CID).first()
            mona = temp.MOname
            temp_res={}
            temp_res["FID"] = help.FID                                  #论贴的ID
            temp_res["Finf"] = help.Finf                                #论贴的内容
            temp_res["CID"] = help.CID                                  #论贴传作者的ID
            temp_res["good"] = str(help.good)                           #点赞的数目
            temp_res["module_name"] = mona                              #论贴所属的模块名字
            temp_res["title"] = help.title                              #论贴的标题
            temp_res["module_id"] = help.MOID                           #论贴的模块ID
            temp_res["author"] = Author.Cname                           #创建论贴的用户名字
            
            res.append(temp_res)
            
        return jsonwrap(0, "success.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()

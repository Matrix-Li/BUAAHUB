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
from functools import cmp_to_key

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

def cmpp(x,y):
    return return_int(y.FID)-return_int(x.FID)


def forum_show(MOID_M):
    try:
        res=[]
        forums=dataforum.query(FORUM).filter(FORUM.MOID==MOID_M).all()
        Len = len(forums)
        tmp={"total":Len,"MOID":MOID_M}
        res.append(tmp)
        forums=sorted(forums,key=cmp_to_key(cmpp),reverse=1)
        flag=0
        allforums=[]
        for i in range(Len-1,-1,-1):
            if(flag==3):
                break
            forum=forums[i]
            thread = {"ID": forum.FID, "title":forum.title,"date":time_change(forum.date)}
            allforums.append(thread)
            flag=flag+1
        dataforum.close()
        res.append(allforums)
        return jsonwrap(0,"success",res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()
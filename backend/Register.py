from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import random
from SQLA import  CUSTOMER,FORUM
from flask import request
from JsonWrap import jsonwrap

import pymysql
engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()

def regist():
    try:
        res={}
        user = request.args.get('nm')
        password = request.args.get('ps')
        if (user==None or password==None or user=='' or password==''):
            dataforum.close()
            return jsonwrap(8, "empty.", res)

        if (dataforum.query(CUSTOMER).filter(CUSTOMER.Cname == user).all() or user==None):
            dataforum.close()
            return jsonwrap(1, "Username already exists.", res)

        #=====================================================================
        a = dataforum.query(func.count('*')).select_from(CUSTOMER).scalar()
        a = a + 1
        table_cid = str(a)
        image_location = "./"+table_cid 
        newcustomer = CUSTOMER(CID=table_cid, Cname=user, passwd=password, crank=1, imagestr=image_location ,flag = 1)
        dataforum.add(newcustomer)
        dataforum.commit()

        #===========================================================

        res['CID'] = table_cid              #用户ID
        res['Cname'] = user                 #用户名字
        res['passwd'] = password            #用户密码
        res['crank'] = "1"                  #用户级别
        res['imagestr'] = image_location    #照片路径
        dataforum.close()
        return jsonwrap(0, "ok", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()

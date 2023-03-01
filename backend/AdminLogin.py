from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import datetime ,time
import random
from SQLA import CUSTOMER
from SQLA import ADMINISTRATOR
from SQLA import SESSION
from flask import request
from JsonWrap import jsonwrap
from Forum_Show import time_change

import pymysql

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()


def generate_random_str(randomlength=32):
    #随机字符串
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def adminlogin():
    try:
        res={}
        user = request.args.get('nm')
        password = request.args.get('ps')
        if(user==None):
            return jsonwrap(8,"empty",res)
        if(password==None):
            return jsonwrap(8,"empty",res)

        ans = dataforum.query(ADMINISTRATOR).filter(ADMINISTRATOR.Adname == user , ADMINISTRATOR.Adpasswd == password).all()

        res={}
        if (len(ans)>0):
            dataforum.query(SESSION).filter(SESSION.Cname == user).delete()
            ranstr = generate_random_str()
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            newsession = SESSION(sid = ranstr, Cname=user, dt = nowtime)

            dataforum.add(newsession)
            dataforum.commit()
            dataforum.close()
            res['SID'] = ranstr
            res['Adname'] = user
            res['dt']  = nowtime
            return jsonwrap(0, "Administrator login success.", res)
            
        else:
            return jsonwrap(1, "Pelease check again.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,"error",error)
    finally:
        dataforum.commit()
        dataforum.close()


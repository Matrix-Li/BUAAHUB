from flask import redirect, request, url_for
from sqlalchemy import String, Column, Integer
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, func, and_, or_
from sqlalchemy.orm import sessionmaker
import datetime ,time
import random
from SQLA import  CUSTOMER
from SQLA import SESSION
from flask import request
from JsonWrap import jsonwrap

import pymysql

engine = create_engine('mysql+pymysql://root:Ruangong2020@localhost:3306/forum')
Base = declarative_base((engine))
Session = sessionmaker(engine)
dataforum = Session()


def generate_random_str(randomlength=32):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def time_change(dtime):
    #dtime(datetime)
    un_time = time.mktime(dtime.timetuple())
    return un_time

def login():
    try:
        res={}
        user = request.args.get('nm')
        password = request.args.get('ps')
        if (user==None or password==None or user=='' and password==''):
            dataforum.close()
            return jsonwrap(8, "empty.", res)

        ans_p = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname == user , CUSTOMER.passwd== password).all()

        res={}
        if (len(ans_p)>0):
            ans = dataforum.query(CUSTOMER).filter(CUSTOMER.Cname == user , CUSTOMER.passwd== password).first()
            userrank = ans.crank
            temp_ans = dataforum.query(SESSION).filter(SESSION.Cname == user).delete()
            if(temp_ans!=None):
                dataforum.query(SESSION).filter(SESSION.Cname == user).delete()
                dataforum.commit()
            ranstr = generate_random_str()
            nowtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            newsession = SESSION(sid = ranstr, Cname=user, dt = nowtime)



            dataforum.add(newsession)
            dataforum.commit()
            
            res['SID'] = ranstr         
            res['Cname'] = user
            res['crank'] = str(int(userrank))
            dataforum.close()
            return jsonwrap(0, "login success.", res)
            
        else:
            dataforum.close()
            return jsonwrap(1, "Pelease check again.", res)
    except Exception as e:
        error = {}
        return jsonwrap(10,str(e),error)
    finally:
        dataforum.commit()
        dataforum.close()
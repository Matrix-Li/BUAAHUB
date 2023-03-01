from flask import request
from JsonWrap import jsonwrap
import random


def jsontest():
    user = request.args.get('nm')
    password = request.args.get('ps')
    res = {}
    res['YourName'] = user
    res['YourPassword'] = password
    res['YourUID'] = random.randint(50, 100)
    return jsonwrap(0, "ok", res)

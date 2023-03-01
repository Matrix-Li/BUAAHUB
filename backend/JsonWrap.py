from flask import jsonify


def jsonwrap(status, msg, data):
    return jsonify(status=int(status), msg=str(msg), data=data)

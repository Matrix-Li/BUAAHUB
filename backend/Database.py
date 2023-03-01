import pymysql

db = pymysql.connect("129.211.46.227", "root", "Ruangong2020", "forum", charset='utf8')
cursor = db.cursor()

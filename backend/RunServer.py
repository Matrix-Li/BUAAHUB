from flask import Flask,render_template,flash,request,redirect,url_for
from Register import regist
from Login import login
from Search import search
from Home import home
from Create import create
from Cidhome import cidhome
from Good import good
from Comment import comment
from CustomerHome import customerhome
from Browsemo import browsemo
from Create_in_Module import create_in_module
from BrowseFo import browsefo
from AdminLogin import adminlogin
from AdminCreate import admincreate
from AdminDelete import admindelete
from AdminBan import adminban
from Admin_Remove_Ban import admin_remove_ban
from flask_apscheduler import APScheduler
from Auto_Remove_Ban import auto_remove_ban
from Customer_Show import customer_show
from Forum_Show import forum_show
from Lastestcomment import lastestcomment
from Collect import collect
from Cancel_Collect import cancel_collect
from Returncollection import returncollection
from Returncomment import returncomment
from flask_cors import *
from Mycomment import mycomment
from Mypost import mypost
from Change import change
from Myrank import myrank
app = Flask(__name__)
CORS(app,  resources=r"/*")   # 允许所有域名跨域


app.add_url_rule(rule='/regist', view_func = regist, methods=['POST', 'GET'])                                                  #regist
#注册

app.add_url_rule(rule='/login', view_func = login,methods=['POST', 'GET'])                                                     #login
#登录

app.add_url_rule(rule='/<SID>/allpost', view_func = home,methods=['POST', 'GET'])                                                           #home
#主页面

app.add_url_rule(rule='/<SID>/home', view_func = customerhome,methods=['POST', 'GET'])                                 #customer_home
#用户中心

app.add_url_rule(rule='/<SID>/create', view_func = create,methods=['POST', 'GET'])                                     #create_forum
#创建一个论贴

app.add_url_rule(rule='/<SID>/<MOID>/create_in_module', view_func = create_in_module,methods=['POST', 'GET'])          #create_post
#在一个特定模块下创建论贴

app.add_url_rule(rule='/<SID>/<FID>/browsefo', view_func = browsefo,methods=['POST', 'GET'])                            
#查看一个论贴

app.add_url_rule(rule='/<SID>/<MOID>/browsemo', view_func = browsemo,methods=['POST', 'GET'])
#查看一个模块下的所有信息(论贴)

app.add_url_rule(rule='/<SID>/<FID>/good', view_func = good,methods=['POST', 'GET'])
#点赞

app.add_url_rule(rule='/<SID>/<FID>/comment', view_func = comment,methods=['POST', 'GET'])
#评论

app.add_url_rule(rule='/<SID>/<FID>/lastestcomment', view_func = lastestcomment,methods=['POST', 'GET'])
#返回最新评论

app.add_url_rule(rule='/<SID>/mypost', view_func = mypost,methods=['POST', 'GET'])
#评论

app.add_url_rule(rule='/<SID>/mycomment', view_func = mycomment,methods=['POST', 'GET'])
#返回最新评论

#==================================================================================================================
app.add_url_rule(rule='/adminlogin',view_func = adminlogin,methods=['POST','GET']) #adminlogin
#管理员登录

app.add_url_rule(rule='/<SID>/search', view_func = search, methods=['POST', 'GET'])           #research
#用户搜索

app.add_url_rule(rule='/<SID>/admincreate',view_func = admincreate,methods=['POST','GET'])  #admincreate
#管理员创建论贴

app.add_url_rule(rule='/<SID>/<FID>/admindelete',view_func = admindelete,methods=['POST','GET'])  #admindelete
#管理员删除论贴

app.add_url_rule(rule='/<SID>/<CID_C>/adminban',view_func = adminban,methods=['POST','GET'])  #admindelete
#管理员禁言

app.add_url_rule(rule='/<SID>/<CID_C>/admin_remove_ban',view_func=admin_remove_ban,methods=['POST','GET']) #adminremoveban
#管理员接触禁言

app.add_url_rule(rule='/<SID>/customer_show',view_func=customer_show,methods=['POST','GET']) #customer_show
#展示所有用户

app.add_url_rule(rule='/<MOID_M>/forum_show',view_func=forum_show,methods=['POST','GET']) #forum_show
#展示每个模板的前三个论贴

app.add_url_rule(rule='/<SID>/<FID>/lastestcomment',view_func=lastestcomment,methods=['POST','GET'])
#返回最新评论

app.add_url_rule(rule='/<SID>/<FID>/collect',view_func=collect,methods=['POST','GET'])

app.add_url_rule(rule='/<SID>/<FID>/cancel_collect',view_func=cancel_collect,methods=['POST','GET'])

app.add_url_rule(rule='/<SID>/returncollection', view_func=returncollection,methods=['POST','GET'])

app.add_url_rule(rule='/<SID>/returncomment', view_func=returncomment,methods=['POST','GET'])

app.add_url_rule(rule='/<SID>/change',view_func=change,methods=['POST','GET'])

app.add_url_rule(rule='/<SID>/myrank',view_func=myrank,methods=['POST','GET'])

def task():
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(func=auto_remove_ban, trigger='interval', seconds=10, id='my_job_id')
    scheduler.start()

task() #定时检查去解除禁言

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

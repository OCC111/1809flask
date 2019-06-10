from flask import Flask
from config import configs
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
import logging
import time
import os
import pymysql
from flask_login import LoginManager

from app.modelview import BaseModelview

pymysql.install_as_MySQLdb()

db = SQLAlchemy()

app = None


login_manager = LoginManager()

login_manager.login_view = 'admin.login'

'''
http://127.0.0.1:5000/api/v1/user/login

'''
def create_app(config):

    global app

    app = Flask(__name__)

    db.init_app(app)

    app.logger.addHandler(initlog())

    login_manager.init_app(app)

    from flask_babelex import Babel

    admin = Admin(app,name='订餐管理系统')

    Babel(app)
    app.config.from_object(configs[config])



    from app.models.admin import User
    from app.admin.modelview import UModelview

    admin.add_view(UModelview(User,db.session))



    from app.models.member import Member

    admin.add_view(BaseModelview(Member,db.session))



    from app.models.food import Category,Food
    admin.add_view(BaseModelview(Category,db.session))
    admin.add_view(BaseModelview(Food,db.session))


    from app.admin import admin_page
    app.register_blueprint(admin_page,url_prefix='/admin')

    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/api/v1')
    return app

def initlog():
    log_dir_name = "app/logs"
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d',time.localtime())
    log_file_str = log_dir_name + os.sep + log_file_name
    log_level = logging.DEBUG
    handler = logging.FileHandler(log_file_str,encoding='utf8')
    handler.setLevel(log_level)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)'
    )

    handler.setFormatter(logging_format)
    return handler


















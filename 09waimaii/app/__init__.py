from flask import Flask
from config import configs
from flask_sqlalchemy import SQLAlchemy
import requests
db = SQLAlchemy()

APPID = 'wxf61a425623cb924c'
APPSECRET = 'bae817c278229a7bfb0549f06ad8f350'

'''
http://127.0.0.1:5000/api/v1/user/login

'''
def create_app(type):


    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid="+APPID+"&secret='+ APPSECRET

    response = requests.post(url=url)
    if response.status_code == 200:
        print(response)



    app = Flask(__name__)

    db.init_app(app)

    app.config.from_object(configs[type])

    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(),url_prefix='/api/v1')
    return app
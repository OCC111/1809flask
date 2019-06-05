from app.libs.redprint import RedPrint
from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import request

api = RedPrint(name='user', description='用户视图')

'http://127.0.0.1:5000/api/v1/user/login'

@api.route('/login',methods=['GET','POST'])
def login():

    code = request.form.get('code')
    print(code)
    return 'login'

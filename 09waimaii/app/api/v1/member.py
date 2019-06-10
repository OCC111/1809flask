from app.libs.redprint import RedPrint
from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import request,current_app,jsonify
import requests
import pymysql
from config import Config
from app.service.member_service import MemberService

from app.models.member import OauthMemberBind,Member


pymysql.install_as_MySQLdb()

api = RedPrint(name='user', description='用户视图')

'http://127.0.0.1:5000/api/v1/user/login'

APPID = 'wxf61a425623cb924c'
APPSECRET = 'bae817c278229a7bfb0549f06ad8f350'


@api.route('/login',methods=['GET','POST'])
def login():

    resp = {'code':1,'msg':'成功','data':{}}
    code = request.form.get('code')
    nickName = request.form.get('nickName')
    avatarUrl = request.form.get('avatarUrl')
    gender = request.form.get('gender')

    if not all([code,nickName,avatarUrl,gender]):
        resp['code'] = -1
        resp['msg'] = '参数不全'
        return jsonify(resp)

    if len(code) <= 1:
        resp['code'] = -1
        resp['msg'] = 'code不对'

    openid = MemberService.getOpenid(code)

    oauthmemberbind = OauthMemberBind.query.filter_by(openid)

    if not oauthmemberbind:
        member = Member()
        member.nickname = nickName
        member.avatarurl = avatarUrl
        member.gender = gender
        member.salt = MemberService.getSalt()

        db.session.add(member)
        db.session.commit()

        oauthmemberbind = OauthMemberBind()
        oauthmemberbind.openid = openid
        oauthmemberbind.client_type = '微信'
        oauthmemberbind.type = 1
        oauthmemberbind.member_id = member.id

        db.session.add(oauthmemberbind)
        db.session.commit()

        oauthmemberbind = oauthmemberbind

    member = Member.query.get(oauthmemberbind.member_id)
    token = '%s#%s' %(MemberService.geneAuthCode(member),member.id)
    resp['data'] = {'token':token}
    return jsonify(resp)

@api.route('/cklogin',methods=['POST'])
def cklogin():
    resp = {'code': 1, 'msg': '成功', 'data': {}}
    code = request.form.get('code')


    if not code or len(code) <= 1:
        resp['code'] = -1
        resp['msg'] = 'code 不对'
        return jsonify(resp)


    openid = MemberService.getOpenid(code)
    if not openid:
        resp['code'] = -1
        resp['msg'] = '调用微信出错'
        return jsonify(resp)

    oauthmemberbind = OauthMemberBind.query.filter_by(openid)

    if not oauthmemberbind:
        resp['code'] = -1
        resp['msg'] = '没有登录1'
        return jsonify(resp)

    member = Member.query.get(oauthmemberbind.member_id)
    if not member:
        resp['code'] = -1
        resp['msg'] = '没有登录'
        return jsonify(resp)


    token = '%s#%s' % (MemberService.geneAuthCode(member), member.id)
    resp['data'] = {'token': token}
    return jsonify(resp)
















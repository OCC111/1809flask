from app.libs.redprint import RedPrint

from flask import request, current_app, jsonify, g

from app.service.member_service import MemberService

from app.models.member import Member

api = RedPrint(name='cart', description='用户模块')


@api.route('/add',methods=['POST'])
def add():
    resp = {'code': 1, 'msg': '成功', 'data': {}}

    token = request.headers.get('token')
    if not token:
        resp['code'] = -1
        resp['msg'] = '必须登录'
        return jsonify(resp)

    tuple_token = token.split('#')

    if len(tuple_token) != 2:
        resp['code'] = -1
        resp['msg'] = 'token error'
        return jsonify(resp)

    member = Member.query.get(tuple_token[1])
    if not member:
        resp['code'] = -1
        resp['msg'] = '没有找到用户'
        return jsonify(resp)

    c_token = MemberService.geneAuthCode(member)
    if c_token != tuple_token:
        resp['code'] = -1
        resp['msg'] = 'token error'
        return jsonify(resp)

    return jsonify(resp)

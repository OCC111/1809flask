from app.libs.redprint import RedPrint
from app import db
from app.models.food import Food,Category
from flask import  jsonify,request
from config import Config




api = RedPrint(description='用户模块',name='user')

@api.route('/food')
def food():
    resp = {'code':1,'msg':'成功','data':{}}

    query_foods =  Food.query.filter_by(status=1).limit(3).all()

    banners = []

    for banner_food in query_foods:
        temp_banner = {}
        temp_banner['id'] = banner_food.id
        temp_banner['pic_url'] = banner_food.main_image
        banners.append(temp_banner)

    resp['data']['banners'] = banners

    query_category = Category.query.filter_by(status=1).order_by(Category.weight.desc()).all()

    categories = []
    categories.append({'id':0,'name':'全部'})

    for category in query_category:
        temp_category = {}
        temp_category['id'] = category.id
        temp_category['name'] = category.name
        categories.append(temp_category)

    resp['data']['categories'] = categories

    return jsonify





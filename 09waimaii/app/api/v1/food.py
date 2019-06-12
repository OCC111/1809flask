from app.libs.redprint import RedPrint
from app import db
from app.models.food import Food, Category
from flask import jsonify, request
from config import Config
from app.service.url_service import UrlService

#   http://127.0.0.1:5000/api/v1/food
#   http://127.0.0.1:5000/api/food/getGoods

api = RedPrint(name='food', description='用户模块')


@api.route('/')
def getBannerAndCategory():
    resp = {'code': 1, 'msg': '成功', 'data': {}}

    query_foods = Food.query.filter_by(status=1).limit(3).all()

    banners = []

    for banner_food in query_foods:
        temp_banner = {}
        temp_banner['id'] = banner_food.id
        temp_banner['pic_url'] = UrlService.BuildStaticUrl(banner_food.main_image)
        banners.append(temp_banner)

    resp['data']['banners'] = banners

    query_category = Category.query.filter_by(status=1).order_by(Category.weight.desc()).all()

    categories = []
    categories.append({'id': 0, 'name': '全部'})

    for category in query_category:
        temp_category = {}
        temp_category['id'] = category.id
        temp_category['name'] = category.name
        categories.append(temp_category)

    resp['data']['categories'] = categories

    return jsonify(resp)


@api.route('/getGoods')
def getGoods():
    try:
        resp = {'code': 1, 'msg': '成功', 'data': {}}

        cid = request.args.get('cid')
        page = request.args.get('page')

        cid = int(cid)

        page = int(page)

        pagesize = 1

        offset = (page - 1) * pagesize

        if not cid or cid == 0:
            foods = Food.query.filter(Food.status == 1).order_by(Food.month_count.desc())

        else:
            foods = Food.query.filter(Food.status == 1, Food.cat_id == cid).order_by(Food.month_count.desc())

        # 分页处理

        foods = foods.offset(offset).limit(pagesize).all()

        goods = []

        for food in foods:
            temp_banner = {}
            temp_banner['id'] = food.id
            temp_banner['name'] = food.name
            temp_banner['price'] = str(food.price)
            temp_banner['stock'] = food.stock
            temp_banner['pic_url'] = UrlService.BuildStaticUrl(food.main_image)
            goods.append(temp_banner)

        print(goods)

        resp['data']['goods'] = goods
        if len(goods) < pagesize:
            resp['data']['ismore'] = 0
        else:
            resp['data']['ismore'] = 1

        return jsonify(resp)
    except Exception as e:
        resp['code'] = -1
        resp['msg'] = '参数有误'
        return jsonify(resp)


@api.route('/getInfo')
def getInfo():

    try:
        resp = {'code': 1, 'msg': '成功', 'data': {}}

        fid = request.args.get('fid')


        fid = int(fid)

        food = Food.query.get(fid)

        if not food:
            resp['code'] = -1
            resp['msg'] = '食品不存在'
            return jsonify(resp)



        if food.status != 1:
            resp['code'] = -1
            resp['msg'] = '食品已经下架'
            return jsonify(resp)


        info = {}
        info['id'] = food.id
        info['name'] = food.name
        info['summary'] = food.summary
        info['total_count'] = food.total_count
        info['comment_count'] = food.comment_count
        info['stock'] = food.stock
        info['price'] = str(food.price)
        info['main_image'] = UrlService.BuildStaticUrl(food.main_image)
        info['pics'] = [UrlService.BuildStaticUrl(food.main_image)]

        resp['data']['info'] = info

        return jsonify(resp)

    except Exception as e:
        resp['code'] = -1
        resp['msg'] = '参数错误'
        return jsonify(resp)




































































































































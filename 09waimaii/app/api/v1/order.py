from app.libs.redprint import RedPrint

api = RedPrint(name='order', description='订单视图')


@api.route('/')
def index():
    return 'index'

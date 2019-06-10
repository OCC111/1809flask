class Config(object):
    SECRET_KEY = 'asdfasdf$#%#@%$^@^'

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

    DEBUG = True
    # db
    SQLALCHEMY_DATABASE_URI = 'mysql://root:11111111@127.0.0.1:3306/db_09waimai'
    # 数据库和模型类同步修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    APPID = 'wxf61a425623cb924c'
    APPSECRET = 'bae817c278229a7bfb0549f06ad8f350'


# 开发配置
class DevConfig(Config):
    DEBUG = True

# 线上配置
class ProConfig(Config):
    DEBUG =  False




configs = {
    'dev':DevConfig,
    'pro':ProConfig
}
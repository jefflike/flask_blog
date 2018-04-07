# import os
#
# class Config:
#     '''
#     将这个配置类存储到单独的Python模块，以保持良好的组织结构
#     从系统变量里取SECRET_KEY
#     SECRET_KEY是我添加的唯一配置选项，对大多数Flask应用来说，它都是极其重要的。
#     Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。Flask-WTF插件使用它来保护网页表单免受CSRF恶意攻击。
#     上线服务器需要把字段配置到系统变量里，开发阶段我并没有这么做
#     '''
#     BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flaskdev'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # MAIL_SERVER = os.environ.get('smtp.sina.com') or 'smtp.sina.com'
#     # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
#     # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
#     # MAIL_USERNAME = os.environ.get('emailforproject@sina.com') or 'emailforproject@sina.com'
#     # MAIL_PASSWORD = os.environ.get('admin@123') or 'admin@123'
#     MAIL_SERVER = 'smtp.sina.com'
#     MAIL_PORT = 25
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = 'emailforproject@sina.com'
#     MAIL_PASSWORD = 'admin@123'
#     ADMINS = ['emailforproject@sina.com']
#     POSTS_PER_PAGE = 2
#     LANGUAGES = ['en', 'es']
# 不同状态下的配置信息
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'emailforproject@sina.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flaskdev'
    ADMINS = ['emailforproject@sina.com']
    POSTS_PER_PAGE = 2

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flaskdev'
    # os.environ.get('DEV_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:meian@localhost/flasktest'
    # os.environ.get('DEV_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:meian@localhost/flask'

    # os.environ.get('DEV_DATABASE_URL') or \
    # 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        # mail_handler = SMTPHandler(
        #     mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
        #     fromaddr=cls.FLASKY_MAIL_SENDER,
        #     toaddrs=[cls.FLASKY_ADMIN],
        #     subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
        #     credentials=credentials,
        #     secure=secure)
        # mail_handler.setLevel(logging.ERROR)
        # app.logger.addHandler(mail_handler)


class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


class UnixConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to syslog
        import logging
        from logging.handlers import SysLogHandler
        syslog_handler = SysLogHandler()
        syslog_handler.setLevel(logging.WARNING)
        app.logger.addHandler(syslog_handler)


# 多个环境开发的配置，目前我只配置了开发的配置，其他配置实际上并不存在
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'unix': UnixConfig,

    'default': DevelopmentConfig
}

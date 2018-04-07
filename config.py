import os

class Config:
    '''
    将这个配置类存储到单独的Python模块，以保持良好的组织结构
    从系统变量里取SECRET_KEY
    SECRET_KEY是我添加的唯一配置选项，对大多数Flask应用来说，它都是极其重要的。
    Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。Flask-WTF插件使用它来保护网页表单免受CSRF恶意攻击。
    '''
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/flaskdev'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('smtp.sina.com') or 'smtp.sina.com'
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('emailforproject@sina.com') or 'emailforproject@sina.com'
    # MAIL_PASSWORD = os.environ.get('admin@123') or 'admin@123'
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'emailforproject@sina.com'
    MAIL_PASSWORD = 'admin@123'
    ADMINS = ['emailforproject@sina.com']
    POSTS_PER_PAGE = 2
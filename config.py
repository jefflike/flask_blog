import os

class Config(object):
    '''
    将这个配置类存储到单独的Python模块，以保持良好的组织结构
    从系统变量里取SECRET_KEY
    SECRET_KEY是我添加的唯一配置选项，对大多数Flask应用来说，它都是极其重要的。
    Flask及其一些扩展使用密钥的值作为加密密钥，用于生成签名或令牌。Flask-WTF插件使用它来保护网页表单免受CSRF恶意攻击。
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
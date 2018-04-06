from app import app

@app.route('/')
@app.route('/index')
def index():
    '''
    这个视图函数装饰的两个路由的任意一个
    都可以直接访问我们的视图函数
    :return:
    '''
    return "Hello, World!"
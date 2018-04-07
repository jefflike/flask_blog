'''
    博客蓝图创建，博客的逻辑拆分到此处
'''
from flask import Blueprint


web = Blueprint('web', __name__, template_folder='templates')

from app.blog import routers
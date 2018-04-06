from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@manager.option('-n', '--name', dest='name', help='Your name', default='world')
# @manager.option('-u', '--url', dest='urls', default='www.baidu.com')
def hi(name):
    'hello world or hello <setting name>'
    print('hello', name)
    # print(urls)


if __name__ == '__main__':
    manager.run()
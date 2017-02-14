# coding=utf-8
from flask import Flask, render_template			#调用 Flask

from flask_bootstrap import Bootstrap

app = Flask(__name__)				#建立 Flask 实例

bootstrap = Bootstrap(app)

@app.route('/')						#路由建立 url 和视图函数的映射
def index():
    return render_template('index.html')
	
@app.route('/user/<name>')			#动态 url
def user(name):
    return render_template('user.html',	 name=name) # 视图函数和状态码（可选）

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
	
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
	
if __name__ == '__main__':
    app.run()
	

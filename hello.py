# coding=utf-8
from flask import Flask				#调用 Flask

app = Flask(__name__)				#建立 Flask 实例

@app.route('/')						#路由建立 url 和视图函数的映射
def index():
	return '<h1>Hello World!<h1/>'

@app.route('/user/<name>')			#动态 url
def user(name):
	return '<h1>Hello, %s!<h1/>' % name, 200 # 视图函数和状态码（可选）

if __name__ == '__main__':
	app.run(debug=True)
	

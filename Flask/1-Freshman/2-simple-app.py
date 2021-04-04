from flask import Flask, render_template, request, redirect, session
from wsgiref.simple_server import make_server

app = Flask(__name__)
app.secret_key = 'ff'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET': # 请求方法
        return render_template('login.html')
    user = request.form.get('user') # 获取POST传过来的值
    pwd = request.form.get('pwd')
    if(user == 'alex' and pwd == '123'):
        session['user_info'] = user
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误')

@app.route('/index')
def index():
    user_info = session.get('user_info')
    if not user_info:
        return redirect('/login')
    return '欢迎登录'

if __name__ == '__main__':
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()
    app.run()
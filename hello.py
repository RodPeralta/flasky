from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    ip_adress = request.remote_addr
    return '<p>Your browser is {}</p><p>And your IP is {}</p>'.format(user_agent, ip_adress)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
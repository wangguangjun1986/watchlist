from flask import Flask,escape,url_for

app=Flask(__name__)

@app.route('/')
def hello():
    return 'welcome to my watchlist!'
    
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

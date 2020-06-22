from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/my_route')
def my_route():
    return 'Welcome to this page'

@app.route('/test_post', methods=['POST'])
def test_post():
    data = request.data
    print(data)
    return 'All good, thanks for making a POST'

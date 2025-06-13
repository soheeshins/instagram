from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    print('hello')
    return { 'message': 'hello' }

@app.route('/hello/<name>')
def hello_name(name):
    print(f'hello {name}')
    return { 'message': 'hello', 'name': name }

@app.route('/users')
def users():
    return {'message': 'users'}

@app.route('/users/<user_id>')
def users_id(user_id):
    return {'message':'success', 'user_id': user_id}


app.run(debug=True, host='0.0.0.0', port=5000)
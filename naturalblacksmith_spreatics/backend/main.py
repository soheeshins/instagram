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

@app.route('/user/<userID>')
def userIDSet(userID):
    print(f'user name is {userID}')
    return { 'message': 'user', 'uswerId': userID }

app.run(debug=True, host='0.0.0.0', port=5001)
from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    print("/hello!imdoubled")
    return {'message' : 'hello!!!'}
@app.route('/hello/<name>')
def hello_name(name):
    print("/hello/{name}/endpoint")
    return {'message' :'hello','name': name}

# method 디폴트는 get
@app.route('/users/<user_id>/posts')
def posts(user_id):
    return {'message' : 'post', 'user_id' : user_id}
@app.route('/users/<user_id>/dms', methods=['GET'])
def dms(user_id):
    return {'message':'dms','user_id':user_id}
@app.route('/users/<follower_id>/follow/<followee_id>' , methods=['POST'])
def follow(follower_id,followee_id):
    return {'message':'follow','follower':follower_id, 'followee':followee_id}
app.run(debug=True,host = '0.0.0.0', port = 5000)

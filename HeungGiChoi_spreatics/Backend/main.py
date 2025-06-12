from flask import Flask

app = Flask('Choi1')
@app.route('/hello')
def hello():
    print('hello')
    return {'message': 'hello'}

@app.route('/hello/<name>')
def hello_name(name):
    return {'message':'hello', 'name': name}
#내 포스팅 목록 조회: GET /users/<user_id>/posts
@app.route('/users/<user_id>/posts')
def posts(user_id):
    return { 'message': 'post', 'user_id': user_id }

#DM 목록 조회: GET /users/<user_id>/dms
@app.route('/users/<user_id>/dms')
def dms(user_id):
    return { 'message': 'dms', 'user_id': user_id }

#follow 요청: POST /users/<follower_id>/follow/<followee_id>
@app.route('/users/<follower_id>/follow/<followee_id>', methods=['POST'])
def follow(follower_id, followee_id):
    return {
            'message': 'follow',
            'follower_id': follower_id,
            'followee_id': followee_id
            }

app.run(debug=True, host='0.0.0.0', port=5000)
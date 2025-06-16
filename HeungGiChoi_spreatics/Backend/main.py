from flask import Flask, request
import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='gmdtm457^^',
        db='create_account',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

app = Flask(__name__)
@app.route('/create_user', methods=['POST'])
def user_generation():
    data = request.get_json()

    nickname = data.get('nickname')
    password = data.get('password')
    name = data.get('name')
    birthday = data.get('birthday')
    email = data.get('email')

    if((name is None) or (nickname is None) or (password is None)):
        return {"status": "failed", "reason": "nickname, name, password is must enter."}

    conn = get_connection()

    with conn.cursor() as cursor:
        try:
            sql = """insert into users(nickname, password, name, email, birthday) 
                    values(%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nickname, password, name, email, birthday))
            conn.commit()
        except pymysql.err.IntegrityError as e:
            return {"status": "failed", "reason": f"{str(e)}, The nickname is duplicated."}

    with conn.cursor() as cursor:
        sql = """select *
                 from users
                 where nickname = %s;"""
        cursor.execute(sql, (nickname,))
        rows = cursor.fetchall()
        return rows[0]

app.run(debug=True, host='0.0.0.0', port=5000)

# from flask import Flask

# app = Flask('Choi1')
# @app.route('/hello')
# def hello():
#     print('hello')
#     return {'message': 'hello'}

# @app.route('/hello/<name>')
# def hello_name(name):
#     return {'message':'hello', 'name': name}
# #내 포스팅 목록 조회: GET /users/<user_id>/posts
# @app.route('/users/<user_id>/posts')
# def posts(user_id):
#     return { 'message': 'post', 'user_id': user_id }

# #DM 목록 조회: GET /users/<user_id>/dms
# @app.route('/users/<user_id>/dms')
# def dms(user_id):
#     return { 'message': 'dms', 'user_id': user_id }

# #follow 요청: POST /users/<follower_id>/follow/<followee_id>
# @app.route('/users/<follower_id>/follow/<followee_id>', methods=['POST'])
# def follow(follower_id, followee_id):
#     return {
#             'message': 'follow',
#             'follower_id': follower_id,
#             'followee_id': followee_id
#             }

# @app.route('/users/<user_id>')
# def users(user_id):
#     return { 'message': 'post', 'user_id': user_id }

# app.run(debug=True, host='0.0.0.0', port=5000)
from flask import Flask, request
import pymysql
from datetime import datetime

def get_connection():
    return pymysql.connect(
        host='database-1.cts2qeeg0ot5.ap-northeast-2.rds.amazonaws.com',
        user='kevin',
        password='spreatics*',
        db='instagram_inseo',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

app = Flask(__name__)
# 사용자 생성
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    nickname = data.get('nickname')
    name = data.get('name')
    password = data.get('password')
    age = data.get('age')
    email = data.get('email')
    
    if nickname is None or name is None or password is None:
        return {"status": "failed", "reason": "nickname, name, password is None"}

    conn = get_connection()

    with conn.cursor() as cursor:
        try:
            sql = """
            INSERT INTO users (nickname, name, password, age, email) 
                values (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nickname, name, password, age, email))
            conn.commit()

        except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }
    
    with conn.cursor() as cursor:
        sql = """
        SELECT user_id
        FROM users
        WHERE nickname = %s
        """
        cursor.execute(sql,(nickname,))
        return {"status": "success", "user_id": cursor.fetchone()}
    
# 사용자 인증(로그인)
@app.route('/users/login', methods = ['POST'])
def login_user():
    data = request.get_json()
    nickname = data.get('nickname')
    password = data.get('password')

    if nickname is None:
        return {"status":"failed", "reason":"nickname is None."}
    elif password is None:
        return {"status":"failed", "reason":"password is None."}
    
    conn = get_connection
    
    try:
        with conn.cursor() as cursor:
            sql_select = "SELECT * FROM users WHERE nickname = %s"
            cursor.execute(sql_select, (nickname,))
            row = cursor.fetchone()

            if not row:
                return {"status": "failed", "reason": f"nickname, {nickname} doesn't exist"}
            if row['password'] == password:
                return {"status": "success", "user_id": row['user_id']}
            else:
                return {"status": "failed", "reason": "password, password doesn't match"}

    except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }

# 특정 사용자 조회
@app.route('/users/<user_id>')
def search_user(user_id):
    conn = get_connection()

    with conn.cursor() as cursor:
        sql = """
        SELECT * 
        FROM users
        WHERE user_id = %s
        """
        cursor.execute(sql,(user_id,))
        row = cursor.fetchone()

        # 입력한 user_id 가 db에 없는 경우
        if row is None:
            return {"status": "failed", "reason": f"user_id, {user_id} doesn't exist."}

        return {"status": "success", "user": row}

# 사용자 정보 수정
@app.route('/users/<user_id>', methods = ['PUT'])
def update_user(user_id):
    data = request.get_json()
    nickname = data.get('nickname')
    name = data.get('name')
    password = data.get('password')
    age = data.get('age')
    email = data.get('email')

    conn = get_connection()

    with conn.cursor() as cursor:
        try:
            sql_select = """
            SELECT *
            FROM users
            WHERE user_id = %s
            """
            cursor.execute(sql_select,(user_id,))
            row = cursor.fetchone()

            # 입력한 user_id 가 db에 없는 경우
            if row is None:
                return {"status": "failed", "reason": f"user_id, {user_id} doesn't exist."}

            sql_update = """
            UPDATE users SET nickname = %s, name = %s, password = %s, age = %s, email = %s WHERE user_id = %s
            """
            cursor.execute(sql_update, (nickname, name, password, age, email,user_id))
            conn.commit()
            
            row['nickname'] = nickname
            row['name'] = name
            row['password'] = password
            row['age'] = age
            row['email'] = email
            
            return {"status":"success", "user":row}

        except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }
        
# 사용자 삭제
@app.route('/users/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            select = "SELECT * FROM users WHERE user_id = %s"
            cursor.execute(select, (user_id,))
            row = cursor.fetchone()

            if row is None:
                return {"status": "failed", "reason": f"user_id, {user_id} doesn't exist"}
            
            delete = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(delete, (user_id,))
            conn.commit()

            return {"status": "deleted"}

    except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }


app.run(debug=True, host='0.0.0.0', port=5000)

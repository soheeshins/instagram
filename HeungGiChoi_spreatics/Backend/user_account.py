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
# 유저 생성 및 생성 user_id 조회
@app.route('/create_user', methods=['POST'])
def user_generation():
    data = request.get_json()

    nickname = data.get('nickname')
    password = data.get('password')
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')

    if((nickname is None) or (password is None) or (name is None)):
        return {"status": "failed", "reason": "nickname, password, name is must enter."}

    conn = get_connection()

    with conn.cursor() as cursor:
        try:
            sql = """insert into users(nickname, password, name, age, email) 
                    values(%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (nickname, password, name, age, email))
            conn.commit()
        except pymysql.err.IntegrityError as e:
            return {"status": "failed", "reason": f"{str(e)}, The nickname is duplicated."}

    with conn.cursor() as cursor:
        sql = """select *
                 from users
                 where nickname = %s;"""
        cursor.execute(sql, (nickname,))
        rows = cursor.fetchall()
    
        return {"status": "Created", "user_id": rows[0]['user_id']}

app.run(debug=True, host='0.0.0.0', port=5000)
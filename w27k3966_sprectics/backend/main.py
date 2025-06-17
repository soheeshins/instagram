import pymysql
from flask import Flask, request

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host='database-1.cts2qeeg0ot5.ap-northeast-2.rds.amazonaws.com',
        user='kevin',
        password='spreatics*',
        db='instagram_kevin',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # 입력값 추출
    nickname = data['nickname']
    name = data['name']
    password = data['password']
    age = data.get('age')
    email = data.get('email')

    conn = get_connection()
    with conn.cursor() as cursor:
        try:
            sql = """
            INSERT INTO users (nickname, name, password, age, email) 
                values (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nickname, name, password, age, email))
            conn.commit()
            user_id = cursor.lastrowid

        except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }
    conn.close()

    return {
        "status": "created",
        "user_id": user_id
    }

app.run(debug=True, host='0.0.0.0', port=5001)
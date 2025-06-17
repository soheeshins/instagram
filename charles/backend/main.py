from flask import Flask, request, jsonify
import json
import traceback
import pymysql
import bcrypt


# # 사용자 생성
# 1. Endpoint
# - POST / users

# 2. Request body

# - nickname(string, required): 사용자 별명(고유)

# - name(string, required): 사용자 이름

# - password(string, required): 비밀번호

# - age(int, optional): 사용자 나이

# - email(string, optional): 사용자 이메일
# ~~~json
# {
#     "nickname": "charles",
#     "name": "김창순",
#     "password": "1234",
#     "email": "soon1234@naver.com",
#     "age": 30
# }
# ~~~

# CREATE TABLE users(
# 	user_id INT PRIMARY KEY AUTO_INCREMENT,
# 	nickname VARCHAR(50) UNIQUE NOT NULL,
# 	password VARCHAR(255) NOT NULL,
# 	name VARCHAR(50) NOT NULL,
# 	age INT,
# 	email VARCHAR(50)
# )


# 타입을 먼저 json으로 바꿔주고


app = Flask(__name__)


def get_connection():
    with open('connect_data.json', encoding='utf-8') as f:
        config = json.load(f)
        cd = config['connect_data']
    return pymysql.connect(
        host=cd['host'],
        user=cd['user'],
        password=cd['password'],
        db=cd['db'],
        charset=cd.get('charset', 'utf8mb4'),
        cursorclass=pymysql.cursors.DictCursor    # ← 클래스 객체로 지정
    )


@app.route('/users', methods=['POST'])
def create_user():
    # 1. Content-Type 체크 (클라이언트가 application/json 으로 보냈는지)
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    # 2. JSON 파싱
    data = request.get_json()
    nickname = data.get('nickname')
    name = data.get('name')
    password = data.get('password')
    age = data.get('age')    # optional
    email = data.get('email')  # optional

    # 3. 필수 값 검증
    if not nickname or not name or not password:
        return jsonify({'error': 'Nickname, name, and password are required.'}), 400

    # 4. 비밀번호 해싱
    hashed_pw = bcrypt.hashpw(password.encode(
        'utf-8'), bcrypt.gensalt()).decode('utf-8')

    # 5. DB에 저장
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO users (nickname, name, password, age, email)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nickname, name, hashed_pw, age, email))
        conn.commit()
        user_id = cursor.lastrowid
    except pymysql.err.IntegrityError as ie:
        # 닉네임 중복 등 UNIQUE 위반
        return jsonify({'error': 'Nickname already exists.'}), 409
    except Exception as e:
        traceback.print_exc()

        return jsonify({'error': str(e)}), 500

    finally:
        conn.close()

    # 6. 생성 성공 응답
    return jsonify({
        'status':   'created',
        'user_id':  user_id,
        'nickname': nickname
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

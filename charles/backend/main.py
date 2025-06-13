from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    print('hello')
    return {'message': 'hello'}


@app.route('/hello/<name>')
def hello_name(name):
    print(f'hello {name}')
    return {'message': 'hello', 'name': name}


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

# 3. Description
# - 새로운 사용자 계정을 생성한다.

# - nickname, name, password는 반드시 입력해야 하며, 중복된 nickname이 있을 경우 생성에 실패한다.

# 4. Response body

# - status(string): "created" 또는 "failed"

# - user_no(int): 생성 성공 시 사용자 고유 번호

# - reason(string): 실패 시 원인

# ~~~json
# // 성공
# {
#     "status": "created",
#     "user_no": 105
# }

# // 실패
# {
#     "status": "failed",
#     "reason": "nickname 'charles' is already taken"
# }
# ~~~


@app.route('/users', methods=['POST'])
def make_id():
    nickname = input('nickname: ')
    name = input('name: ')
    password = input('password: ')
    email = input('email: ')
    age = int(input('age: '))
    # user_no = None
    print(
        f'nickname: {nickname}, name: {name}, password: {password}, email: {email}, age: {age}')
    input('is this correct? (Press y to continue, any other key to cancel): ')
    if input() != 'y':
        return {
            "status": "failed",
            "reason": "User creation cancelled by user."
        }

    # for i in range(1, 100):
    #     if not is_user_exists(i):
    #         user_no = i
    #         break
    # try:
    #     if not nickname or not name or not password or not email or not age:
    #         raise ValueError(
    #             "nickname, name, password, email, and age are required fields.")
    #     if not isinstance(age, int) or age < 0:
    #         raise ValueError("age must be a non-negative integer.")
    #     if not isinstance(nickname, str) or not isinstance(name, str) or not isinstance(password, str):
    #         raise ValueError("nickname, name, and password must be strings.")
    #     if len(nickname) < 3 or len(nickname) > 20:
    #         raise ValueError(
    #             "nickname must be between 3 and 20 characters long.")
    #     if len(name) < 1 or len(name) > 50:
    #         raise ValueError("name must be between 1 and 50 characters long.")
    #     if len(password) < 6 or len(password) > 20:
    #         raise ValueError(
    #             "password must be between 6 and 20 characters long.")
    #     if email and not isinstance(email, str):
    #         raise ValueError("email must be a string if provided.")

    # 중복된 nickname 체크 로직 (예: 데이터베이스 조회)
    # if is_nickname_taken(nickname):
    #     raise ValueError(f"nickname '{nickname}' is already taken")

#     except ValueError as e:
#         return {
#             "status": "failed",
#             "reason": str(e)
#         }
    insert_user = create_user(nickname, name, password, email, age)

    if insert_user:
        return {
            "nickname": nickname,
            "name": name,
            "password": password,
            "email": email,
            "age": age,
            # "user_no": user_no,
            "status": "created"
        }
    else:
        return {
            "status": "failed",
            "reason": 'nickname is already taken'
        }


def create_user(nickname, name, password, email=None, age=None):
    # 사용자 생성 로직 (예: 데이터베이스에 저장)
    pass


app.run(debug=True, host='0.0.0.0', port=5000)

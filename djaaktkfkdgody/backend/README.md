
from flask import Flask, request, jsonify

app = Flask(__name__)

# 사용자 저장소 (메모리 기반)
users = {}
next_user_id = 1

# 닉네임 중복 체크용
nickname_set = set()

# 사용자 생성
@app.route('/users', methods=['POST'])
def create_user():
    global next_user_id

    data = request.get_json()

    # 필수 필드 체크
    required_fields = ['nickname', 'name', 'password']
    for field in required_fields:
        if field not in data:
            return jsonify({
                "status": "failed",
                "reason": f"Missing required field: {field}"
            }), 400

    nickname = data['nickname']
    if nickname in nickname_set:
        return jsonify({
            "status": "failed",
            "reason": f"nickname, {nickname} is duplicated"
        }), 400

    # 유저 저장
    user_id = next_user_id
    next_user_id += 1
    users[user_id] = {
        "nickname": nickname,
        "name": data["name"],
        "password": data["password"],
        "email": data.get("email", ""),
        "age": data.get("age", None)
    }
    nickname_set.add(nickname)

    return jsonify({
        "status": "created",
        "user_id": user_id
    }), 201

# 사용자 삭제
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({
            "status": "failed",
            "reason": f"user_id, {user_id} doesn't exist"
        }), 404

    # 닉네임도 set에서 제거
    nickname = users[user_id]["nickname"]
    nickname_set.discard(nickname)

    del users[user_id]

    return jsonify({
        "status": "deleted"
    })

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

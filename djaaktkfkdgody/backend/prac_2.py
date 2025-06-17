# Flask: 웹 서버 프레임워크
# request: 클라이언트 요청 처리용
# jsonify: 파이썬 객체를 JSON 응답으로 변환함
from flask import Flask, request, jsonify

# 비밀번호 해싱을 위한 모듈
# 실제 비밀번호는 저장하지 않고 해시값만 저장함 (보안 때문)
from werkzeug.security import generate_password_hash, check_password_hash

# Flask 앱 인스턴스 생성함
app = Flask(__name__)

import pymysql
def get_connection():
    return pymysql.connect(
        host='database-1.cts2qeeg0ot5.ap-northeast-2.rds.amazonaws.com',
        user='pdohee',
        password='gamzagoguma',
        db='instagram_gamza',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# 데이터 저장소 (DB 없이 파이썬 변수로만 처리함)
users = {}  # 사용자 정보 저장. key는 닉네임, value는 user dict
posts = []  # 게시글 저장 리스트
comments = []  # 댓글 저장 리스트
follows = []  # 팔로우 관계 저장 리스트
follow_requests = []  # 팔로우 요청 리스트
dms = []  # DM(쪽지) 저장 리스트

# 고유 ID 생성용 카운터 변수들
user_id_counter = 100
post_id_counter = 3000
comment_id_counter = 500
dm_id_counter = 9000
follow_request_id_counter = 2000

# 사용자 생성 또는 검색
@app.route('/users', methods=['GET', 'POST'])
def search_users():
    global user_id_counter  # user_id 증가 위해 global 선언함

    # POST: 회원가입 처리
    if request.method == 'POST':
        data = request.get_json()  # 요청 바디에서 JSON 데이터 파싱함

        # 필수 항목 확인 안 되면 에러 반환
        if 'nickname' not in data or 'name' not in data or 'password' not in data or 'email' not in data:
            return jsonify({"error": "Missing required fields"}), 400

        # 닉네임 중복이면 가입 불가
        if data['nickname'] in users:
            return jsonify({"error": "Nickname already exists"}), 409

        # 사용자 객체 생성. 비밀번호는 해시함수로 변환함
        user = {
            "user_id": user_id_counter,
            "nickname": data['nickname'],
            "name": data['name'],
            "password": generate_password_hash(data['password']),  # 보안 처리됨
            "email": data['email']
        }

        # users 딕셔너리에 저장 (닉네임이 key임)
        users[data['nickname']] = user
        user_id_counter += 1  # 다음 사용자 ID 준비

        # 사용자 생성 완료 메시지 반환
        return jsonify({"status": "created", "user": user}), 201

    # GET: 사용자 검색 (keyword 이용)
    keyword = request.args.get('keyword', '')

    # 검색 결과 리스트로 만듦. nickname이나 name에 keyword 포함되면 포함됨
    result = [
        {
            "user_id": user['user_id'],
            "nickname": user['nickname'],
            "profile_image": "https://cdn.example.com/profiles/default.jpg"  # 기본 이미지 URL
        }
        for user in users.values()
        if keyword.lower() in user['nickname'].lower() or keyword.lower() in user['name'].lower()
    ]
    return jsonify(result)

# 로그인 처리
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # JSON 요청 받아옴
    nickname = data.get("nickname")
    password = data.get("password")

    # 닉네임으로 사용자 찾음
    user = users.get(nickname)
    if not user:
        return jsonify({"error": "User not found"}), 404  # 사용자 없으면 404

    # 비밀번호 비교 (입력값 vs 해시된 저장값)
    if check_password_hash(user['password'], password):
        return jsonify({
            "status": "login success",
            "user_id": user['user_id'],
            "nickname": user['nickname']
        })
    
    return jsonify({"error": "Invalid credentials"}), 401  # 비번 틀림

# 사용자 정보 조회 (user_id로 찾음)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users.values():
        if user['user_id'] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 사용자 정보 수정 (PUT)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users.values():
        if user['user_id'] == user_id:
            # 수정 가능한 필드만 추림
            user.update({k: v for k, v in data.items() if k in ['name', 'password', 'age', 'email']})
            return jsonify({"status": "updated"})
    return jsonify({"error": "User not found"}), 404

# 사용자 삭제
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for nickname, user in list(users.items()):  # 딕셔너리 수정 위해 list로 감쌈
        if user['user_id'] == user_id:
            del users[nickname]
            return jsonify({"status": "deleted"})
    return jsonify({"error": "User not found"}), 404

# 게시글 등록
@app.route('/posts', methods=['POST'])
def create_post():
    global post_id_counter
    data = request.get_json()

    # 게시글 객체 생성
    post = {
        "post_id": post_id_counter,
        "user_id": data["user_id"],
        "content": data["content"],
        "created_at": "2025-06-15T10:00:00"  # 시간 고정됨
    }

    posts.append(post)  # 리스트에 추가
    post_id_counter += 1

    return jsonify({"status": "post created", "post_id": post["post_id"]}), 201

# 게시글 목록 조회 (user_id 기준)
@app.route('/posts', methods=['GET'])
def get_posts():
    user_id = int(request.args.get('user_id'))
    user_posts = [p for p in posts if p['user_id'] == user_id]
    return jsonify(user_posts)

# 댓글 추가
@app.route('/posts/<int:post_id>/comment', methods=['POST'])
def add_comment(post_id):
    global comment_id_counter
    data = request.json

    comment = {
        "comment_id": comment_id_counter,
        "post_id": post_id,
        "user_id": data['user_id'],
        "nickname": next((u['nickname'] for u in users.values() if u['user_id'] == data['user_id']), ''),
        "comment": data['comment'],
        "created_at": "2025-06-13T16:00:00"
    }

    comments.append(comment)
    comment_id_counter += 1

    return jsonify({"status": "created", "comment_id": comment["comment_id"]})

# 댓글 목록 조회
@app.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    result = [c for c in comments if c['post_id'] == post_id]
    return jsonify(result)

# 팔로우 요청 보내기
@app.route('/follow/request', methods=['POST'])
def follow_request():
    global follow_request_id_counter
    data = request.json
    from_id = data['from_user_id']
    to_id = data['to_user_id']

    # 이미 팔로우 중이면 요청 안 받음
    if any(f["from_user_id"] == from_id and f["to_user_id"] == to_id for f in follows):
        return jsonify({"status": "already_following"})

    request_data = {
        "request_id": follow_request_id_counter,
        "from_user_id": from_id,
        "to_user_id": to_id
    }

    follow_requests.append(request_data)
    follow_request_id_counter += 1

    return jsonify({"status": "requested"})

# 받은 팔로우 요청 목록
@app.route('/follow/requests', methods=['GET'])
def get_follow_requests():
    user_id = int(request.args.get('user_id'))
    result = []

    for fr in follow_requests:
        if fr["to_user_id"] == user_id:
            from_user = next(u for u in users.values() if u["user_id"] == fr["from_user_id"])
            result.append({
                "request_id": fr["request_id"],
                "from_user_id": from_user["user_id"],
                "nickname": from_user["nickname"],
                "profile_image": "https://cdn.example.com/profiles/default.jpg"
            })

    return jsonify(result)

# 팔로우 응답 (수락 또는 거절)
@app.route('/follow/respond', methods=['POST'])
def follow_respond():
    data = request.json
    request_id = data['request_id']
    action = data['action']

    req = next((r for r in follow_requests if r['request_id'] == request_id), None)

    if not req:
        return jsonify({"status": "failed", "reason": "request not found"}), 404

    follow_requests.remove(req)

    if action == "accept":
        follows.append({
            "from_user_id": req['from_user_id'],
            "to_user_id": req['to_user_id']
        })
        return jsonify({"status": "accepted"})

    elif action == "reject":
        return jsonify({"status": "rejected"})

    return jsonify({"status": "failed", "reason": "invalid action"}), 400

# 내가 팔로우한 사람 목록 조회
@app.route('/follow/list', methods=['GET'])
def get_following():
    user_id = int(request.args.get('user_id'))

    following = [
        {
            "user_id": f["to_user_id"],
            "nickname": next(u["nickname"] for u in users.values() if u["user_id"] == f["to_user_id"]),
            "profile_image": "https://cdn.example.com/profiles/default.jpg"
        }
        for f in follows if f["from_user_id"] == user_id
    ]

    return jsonify(following)

# DM(쪽지) 보내기
@app.route('/dm', methods=['POST'])
def send_dm():
    global dm_id_counter
    data = request.json

    dm = {
        "dm_id": dm_id_counter,
        "from_user_id": data["from_user_id"],
        "to_user_id": data["to_user_id"],
        "message": data["message"],
        "sent_at": "2025-06-13T16:30:00"
    }

    dms.append(dm)
    dm_id_counter += 1

    return jsonify({"status": "sent", "dm_id": dm["dm_id"]})

# DM 대화 목록 (두 사용자 간)
@app.route('/dm/conversation', methods=['GET'])
def get_dm_conversation():
    uid1 = int(request.args.get("user1_id"))
    uid2 = int(request.args.get("user2_id"))

    conv = [dm for dm in dms if {dm["from_user_id"], dm["to_user_id"]} == {uid1, uid2}]
    return jsonify(conv)

# DM 삭제
@app.route('/dm/<int:dm_id>', methods=['DELETE'])
def delete_dm(dm_id):
    for dm in list(dms):  # 삭제 중이라 list로 감쌈
        if dm["dm_id"] == dm_id:
            dms.remove(dm)
            return jsonify({"status": "deleted"})
    return jsonify({"status": "failed", "reason": "DM not found"}), 404

# 서버 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

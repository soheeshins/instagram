# REST API Spec.
- version 0.1 (2025/6/11)
# 사용자 계정
## 사용자 생성
1. Endpoint
   - POST /users
2. Request body 
   - nickname (string): 사용자 nickname, 필수
   - name (string): 사용자 이름, 필수
   - password (string): 비밀번호, 필수
   - age (int, optional): 사용자 나이
   - email (string, optional): 사용자 email 주소
~~~
{
  "nickname": "inseo",
  "name": "전인서",
  "password": "1234",
  "email": "zzangis345@naver.com"
}
~~~
3. Description
   - 사용자 계정을 생성한다. nickname과 name, password는 필수 입력값이다.
   - nickname은 고유한 값이며 기존 사용자와 중복되면 생성이 실패한다.
4. Response body
   - status (string): created, failed
   - user_id (int): 생성 성공 시, user_id 반환
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "created",
  "user_id": 105
}

{
  "status": "failed",
  "reason": "nickname, kevin is duplicated"
}
~~~
## 사용자 인증 (로그인)
1. Endpoint
   - POST /users
2. Request body 
   - nickname (string): 사용자 nickname, 필수
   - password (string): 사용자 비밀번호, 필수
3. Description
   - nickname에 해당하는 user_id를 찾아 로그인한다.
   - 해당하는 nickname이 없으면 로그인이 실패한다.
   - nickname에 해당하는 password 일치하지 않으면 로그인이 실패한다.
4. Response body
   - status (string): success, failed
   - user_id: 생성 성공시, 반환
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "success",
  "user_id": 1
}
~~~
~~~
{
  "status": "failed",
  "reason": "nickname, aabbcc doesn't exist"
}
~~~
~~~
{
  "status": "failed",
  "reason": "password, password doesn't match"
}
~~~
## 사용자 정보 조회
1. Endpoint
   - GET /users/<user_id>
     - user_id (int): 조회할 사용자 id
2. Request body 
   - 없음
3. Description
   - user_id에 해당하는 사용자 계정을 조회한다.
   - user_id가 없으면 조회가 실패한다.
4. Response body
   - status (string): success, failed
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
~~~
## 사용자 정보 수정
1. Endpoint
   - PUT /users/<user_id>
     - user_id (int): 수정할 사용자 id
2. Request body
   - nickname (string, optional): 사용자 nickname
   - name (string, optional): 사용자 이름
   - password (string, optional): 사용자 비밀번
   - age (int, optional): 사용자 나이
   - email (string, optional): 사용자 email 주소
3. Description
   - user_id에 해당하는 사용자 계정 정보를 수정한다.
   - user_id가 없으면 정보 수정이 실패한다.
4. Response body
   - status (string): success, failed
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
~~~
## 사용자 삭제
1. Endpoint
   - DELETE /users/<user_id>
     - user_id (int): 삭제할 사용자 id
2. Request body 
   - 없음
3. Description
   - user_id에 해당하는 사용자 계정을 삭제한다.
   - user_id가 없으면 삭제가 실패한다.
4. Response body
   - status (string): deleted, failed
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
~~~

# 포스팅
## 포스트 올리기
1. Endpoint
   - POST /users/<user_id>/posts
     - user_id (int): 포스트를 올릴 사용자 id
2. Request body 
   - post-title (string): 포스트 제목, 필수
   - post-text (string): 포스트 내용, 필수
~~~
{
  "post-title": "포스트 제목",
  "post-text": "포스트 내용"
}
~~~
3. Description
   - 포스트를 생성한다. post-title과 post-text는 필수 입력값이다.
4. Response body
   - status (string): created, failed
   - post_id (int): 생성 성공 시, post_id 반환
   - posting_date (datetime): 생성 성공시, posting_date 반환
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "created",
  "post_id": 105
}
~~~

# 소셜
# 메시지

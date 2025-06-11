# REST API Spec.
- version 0.1 (2025/6/11)
# 사용자 계정
## 사용자 생성
1. Endpoint
   - POST /users
2. Request body 
   - nickname (string): 사용자 nickname, 필수
   - name (string): 사용자 이름, 필수
   - age (int, optional): 사용자 나이
   - email (string, optional): 사용자 email 주소
~~~
{
  "nickname": "inseo",
  "name": "전인서",
  "email": "zzangis345@naver.com"
}
~~~
3. Description
   - 사용자 계정을 생성한다. nickname과 name은 필수 입력값이다.
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
   - post /users/<user_id>
     - user_id (int): 로그인할 사용자 id
2. Request body 
   - 없음
3. Description
   - user_id에 해당하는 사용자 계정을 로그인한다.
   - user_id가 없으면 로그인이 실패한다.
4. Response body
   - status (string): success, failed
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
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
# 소셜
# 메시지

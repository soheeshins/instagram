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
  "nickname": "sohee",
  "name": "shinsohee",
  "password": "1234",
  "email": "sohee.spreatics@gmail.com"
}
~~~
4. Description
   - 사용자 계정을 생성한다. nickname과 name, password는 필수 입력값이다.
   - nickname은 고유한 값이며 기존 사용자와 중복되면 생성이 실패한다.
5. Response body
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
  "reason": "nickname, sohee is duplicated"
}
~~~
## 사용자 인증 (로그인)

1. Endpoint
   - POST /users/login

2. Request body
   - nickname (string): 사용자 nickname, 필수
   - password (string): 비밀번호, 필수
~~~
{
  "nickname": "sohee",
  "password": "1234"
}
~~~
3. Description
   - 사용자 nickname과 password 입력
   - 틀릴 경우 Error
4. Response body
   - status (string): success, failed
   - reason (string): 실패 시, 실패 원인 
~~~
{
 "status" : "success"
}
{
  "status" : "failed",
  "reason" : "nickname ERROR"
}
{
  "status" : "failed",
  "reason" : "password ERROR"
}
~~~

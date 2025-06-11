# REST API Spec.
- version 0.1 (2025/6/11)
# 사용자 계정
## 사용자 생성
1. Endpoint
   - POST /users
2. Request body 
   - nickname (string): 사용자 nickname, 필수
   - password(string) : 비밀번호,필수
   - name (string): 사용자 이름, 필수
   - age (int, optional): 사용자 나이
   - email (string, optional): 사용자 email 주소
~~~
{
  "nickname": "double_d_eo",
  "name": "김현서",
  "email": "doubled0514@gmail.com"
}
~~~
4. Description
   - 사용자 계정을 생성한다. nickname과 name은 필수 입력값이다.
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
  "reason": "nickname, double_d_eo is duplicated"
}
~~~
## 사용자 인증 (로그인)
1. Endpoint
  - POST/users/<user_id>
2. Requset body
  - id(int) : 사용자 id
  - password(string) : 사용자 비밀번호
~~~
{
"user_id" : 105,
"password" : "0106514aa@"
}
~~~
3. Description
  - 사용자 인증하여 로그인한다
  - 존재하지 않는 id이거나 password가 틀리면 로그인에 실패
4. Response Body
  - status(string) : success, failed
  - user_id : 로그인 성공시 user_id 반환
  - reason(string) : 실패시 실패 원인
~~~~
{
"status" : "success",
"user_id" : 105
}
{
"status" : "failed",
"reason" : "user_id, 104 is not exist"
}
~~~~
## 사용자 정보 조회
1.Endpoint
   - Get/users/<user_id>
2.Request body
3.Description
   - 사용자 정보를 조회한다
4.Response body
   - nickname
   - name
   - age
   - email
## 사용자 정보 수정
1. Endpoint
   - PATCH/users/<user_id>/
2. Request body
   - nickname(optional)
   - name(optional)
   - age(optional)
   - email(optional)
~~~
{
"nickname" :"kevin"
}
~~~  

3. description
   - 사용자 정보를 수정한다. user_id는 수정할 수 없다
4. response body
   - status : success, failed
   - reason : 실패시, 실패 원인
~~~
{
"status" : "success"
}
{
"status" :"failed",
"reason" : "nickname, kevin is duplicated"
}
~~~
## 사용자 삭제
1. Endpoint
   - DELETE /users/<user_id>
     - user_id (int): 삭제할 사용자 id
2. Request body 
   - 없음
4. Description
   - user_id에 해당하는 사용자 계정을 삭제한다.
   - user_id가 없으면 삭제가 실패한다.
5. Response body
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

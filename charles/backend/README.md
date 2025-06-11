
# REST API Spec.
- version 0.1 (2025/6/11)
# 사용자 계정
## 사용자 생성
1. Endpoint
   - POST /users
2. Request body 
   - user_id (INT AUTO_INCREMENT PRIMARY KEY): 사용자 id, int, 자동으로 카운팅, 필수
   - nickname (string): 사용자 nickname, 필수
   - name (string): 사용자 이름, 필수
   - password (string): 비밀번호, 필수
   - age (int, optional): 사용자 나이
   - email (string, optional): 사용자 email 주소
~~~
{
  "user_id(INT AUTO_INCREMENT PRIMARY KEY)" : ' ' 
  "nickname": "charles",
  "name": "김창순",
  "password": "1234",
  "email": "charleskimjr@naver.com"
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
  "reason": "nickname, kevin is duplicated"
}
~~~

## 사용자 인증 (로그인)
1. Endpoint
    login/user

2. Request body 
   - user_no (INT AUTO_INCREMENT PRIMARY KEY): 유저 식별 번호(서버에서), 필수

   - user_id (String) : 사용자 id, 필수
   - password (string): 비밀번호, 필수
   
   - login_botton (string? object?) : 
   클릭시 서버에 id & password 매치 되는지 체크 하게 하는 버튼 
    
   
~~~

{
  "user_id": "charles",
  "password": "1234",
  "user_no"" : user_no

}
~~~



4. Description
    로그인 창으로 이동한다

    - 아이디 입력 칸을 생성
    
    - 비밀번호 입력 칸을 생성(passward 보이지 않게)
    
    - 로그인 클릭 버튼을 생성
    
    - 서버에 존재하는 아이디와 비밀번호가 일치하면 사용자 넘버에 저장된 정보를 불러오는 페이지로 이동시킨다.
    
    - 일치하지 않을시 로그인 실패

5. Response body
   - status (string): created, failed

   - move (int): 로그인 성공 시, user_no page 반환
   
   - reason (string): 실패 시, 실패 원인
~~~

{
  "status": "success",
  "url" : url?user_no
}

{
  "status": "denied",
  "reason": "
Your ID and password do not match. "
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
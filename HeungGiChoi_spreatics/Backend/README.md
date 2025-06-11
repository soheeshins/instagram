# REST API Spec
 - version 0.1(2025/06/11)
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
  "nickname": "Choi",
  "name": "최흥기",
  "password": "1234",
  "age": 32,
  "email": "pamo23@naver.com"
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
  "reason": "nickname, Choi is duplicated"
}
~~~
## 사용자 인증 (로그인)
1. Endpoint
   - POST / users / Auth_users
2. Request body 
   - nickname (string): 사용자 nickname, 필수
   - password (string): 비밀번호, 필수
~~~
{
  "nickname": "Choi",
  "password": "1234",
}
~~~
4. Description
   - 사용자가 로그인한다. nickname과 password를 필수로 입력해야한다.
   - nickname은 고유한 값이며, nickname과 password가 일치해야 한다.
   - nickname과 password가 초기에 생성한 값이 아닐 경우, 로그인이 실패한다.
6. Response body
   - status (string): log_in, failed
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "log_in",
}

{
  "status": "failed",
  "reason": "nickname, password unmatched"
}
~~~
## 사용자 정보 조회
## 사용자 정보 수정
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
## 포스트 올리기
## 올라온 포스트 조회하기
## 포스트의 커맨트 조회하기
## 특정 포스트에 커맨트 달기
# 소셜
## 다른 사용자 조회
## 팔로우 신청
## 팔로우한 목록을 조회
## 자신에게 팔로우 요청한 목록을 조회
## 팔로우를 수락/거절

# 메세지
## DM을 보내기
## DM 조회하기
## DM 삭제하기

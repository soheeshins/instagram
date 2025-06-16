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
   - birthday (string): 사용자 생년월일, 필수
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
   - GET / users / Auth_users
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
   - 로그인 성공시 user_id 같이 반환. 이후 다른 API 호출 시, 그 user_id 사용한다.
6. Response body
   - status (string): log_in, failed
   - user_id (int): 로그인 성공시, user_id 반환
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "log_in",
  "user_id": "105"
}

{
  "status": "failed",
  "reason": "nickname, password unmatched"
}
~~~
## 사용자 정보 조회
1. Endpoint
   - GET / users / <user_id>
    - user_id: 조회할 사용사 user_id
2. Request body
   - 없음
4. Description
   - user_id에 해당하는 사용자 계정 정보를 조회한다.
   - user_id가 일치하지 않으면 계정정보 조회가 실패한다.
5. Response body
   - status (string): selected, failed
   - user_id (int): 조회 성공시, user_id 반환
   - nickname (string): 조회 성공시, nickname 반환
   - name (string): 조회 성공시, name 반환
   - email (string): 조회 성공시, email 반환
   - age (int): 조회 성공시, age 반환
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "selected",
  "user_id": 105
  "nickname": "Choi",
  "name": "최흥기",
  "email": "pamo23@naver.com"
  "age": 32,
}
{
  "status": "failed",
  "reason": "user_id, 105 doesn't exist"
}
~~~
## 사용자 정보 수정
1. Endpoint
   - PUT / users 
2. Request body
   - auth_nickname (string): 초기 인증 사용자 nickname, 필수
   - auth_password (string): 초기 인증 사용자 password, 필수
   - chg_nickname (string): 변경 사용자 nickname, 필수
   - chg_password (string): 비밀번호, 필수
   - chg_email (string, optional): 사용자 email 주소
4. Description
   - 로그인 시 입력한 nickname/password와 auth_nickname/auth_password가 일치하는지 비교한다.
   - 일치하면 해당하는 사용자 계정정보를 수정한다.
   - 일치하지 않으면 계정정보를 수정할 수 없다.
   - 수정한 계정정보를 서버로 넘긴다.
6. Response body
   - status (string): updated, failed
   - chg_nickname (string): 수정 성공시, chg_nickname 반환
   - chg_password (string): 수정 성공 시, chg_password 반환
   - chg_email (string): 수정 성공시, chg_email 반환
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "updated",
  "chg_nickname": "Jun",
  "chg_password": "54321",
  "chg_email": "pamo12@nate.com",
}
{
  "status": "failed",
  "reason": "auth_nickname, auth_password was unmatched"
}
~~~
## 사용자 삭제
1. Endpoint
   - DELETE /users/<user_id>
     - user_id (int): 삭제할 사용자 id
2. Request body 
   - auth_nickname (string): 삭제 인증 nickname, 필수
   - auth_password (string): 삭제 인증 password, 필수
4. Description
   - user_id에 해당하는 사용자 계정을 삭제한다.
   - auth_nickname/auth_password를 통해 계정삭제 인증 과정을 한번 더 거친다.
   - auth_nickname/auth_password가 로그인 시 입력한 nickname/password 과 일치하지 않으면 삭제가 실패한다.
5. Response body
   - status (string): deleted, failed
   - del_status (string): 삭제 성공시, 삭제 성공을 알린다.
   - reason (string): 실패시, 실패 원인
~~~
{
  "status": "deleted",
  "del_status": "user account was deleted"
}
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
~~~
# 포스팅
## 포스트 올리기
1. Endpoint
   - POST / post / <user_id>
    - user_id (int): 포스팅할 사용자 user_id
2. Request body
   - post_id (int): 포스팅한 게시물 id, 필수
   - title (string): 게시물 제목, 필수
   - text (string): 게시물 내용, 필수
   - posting_date (string): 포스팅한 날짜
   - user_id (int): 포스팅한 사용자 id, 필수 
~~~
{
  "post_id": 001,
  "title": "원테이크 5기 정기 공연",
  "text": "원테이크 5기 정기반!일하고 자는 시간 외에는 공연 연습에 매진하고 있습니다. 6.14-15 양일 공연 기대해주세요~~",
  "posting_date": "2025-06-08",
  "user_id": 2
}
~~~
3. Description
   - user_id를 확인하고, 게시판에 포스팅한다.
   - user_id가 없으면, 포스팅을 할 수 없다.
5. Response body
   - status (string): post_success, failed
   - 
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
   - GET / users / Auth_users
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
   - 로그인 성공시 user_id 같이 반환. 이후 다른 API 호출 시, 그 user_id 사용한다.
6. Response body
   - status (string): log_in, failed
   - user_id (int): 로그인 성공시, user_id 반환
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "log_in",
  "user_id": "105"
}

{
  "status": "failed",
  "reason": "nickname, password unmatched"
}
~~~
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

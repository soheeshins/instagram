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
   - nickname: 생성 성공 시, nickname 반환
   - reason (string): 실패 시, 실패 원인
~~~
{
  "status": "created",
  "nickname": "double_d_eo"
}

{
  "status": "failed",
  "reason": "nickname, double_d_eo is duplicated"
}
~~~
## 사용자 인증 (로그인)
1. Endpoint
  - POST/users/login
2. Requset body
  - nickname (string) 
  - password(string) : 사용자 비밀번호
~~~
{
   "nickname":"double_d_eo",
   "password" : "0106514aa@"
}
~~~
3. Description
  - 사용자 인증하여 로그인한다
  - 존재하지 않는 nickname이거나 password가 틀리면 로그인에 실패
4. Response Body
  - status(string) : success, failed
  - user_id(int): 로그인 성공시 user_id 반환
  - reason(string) : 실패시 실패 원인
~~~~
{
   "status" : "success",
   "user_id" : 105
}
{
   "status" : "failed",
   "reason" : "nickname or password is wrong"
}
~~~~
## 사용자 정보 조회
1.Endpoint
   - Get/users/<user_id>
2.Request body
   - 없음
3.Description
   - 사용자 정보를 조회한다
4.Response body
   - nickname(string)
   - name(string)
   - age(int)
   - email(string)
~~~~
{
   "nickname" : "double_d_eo",
   "name" : "김현서",
   "age": "" ,
   "email" : "doubled0514@gamil.com"
}
~~~~
## 사용자 정보 수정
1. Endpoint
   - PUT/users/<user_id>
2. Request body
   - name(string,optional)
   - age(int,optional)
   - email(string,optional)
~~~
{
   "age" :25
}
~~~  
3. description
   - 사용자 정보를 수정한다. user_id는 수정할 수 없다
   - nickname은 수정 불가능
4. response body
   - status : success, failed
   - reason : 실패시, 실패 원인
~~~
{
   "status" : "success"
}
{
   "status" :"failed",
   "reason" : "age, 비밀 is not int type"
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
## 포스트 올리기
1. Endpoint
   - POST/users/<user_id>/post
2. Request body
   - title(string,필수)
   - text(string,opt)
~~~
{
   "title" : "덥다",
   "text" : "에어컨이 안돼서 너무 더워요"
}
~~~
3. Description

4. Resopnse body
   -stauts : success, failed
   -nickname(string) : user_id에 대응하는 닉네임 반환
   -title (string) : 성공시 제목 반환
   -reason(string) : 실패시 실패 이유
~~~
{
   "nickname" : "double_d_eo"
   "status" : "success",
   "title" : "덥다"
}
{
   "staus" : "failed",
   "reason" : "user_id is not exist"
}
~~~
## 올라온 포스트 조회하기
1. Endpoint
   -GET/users/<user_id>/post
2. Request body
   -title(string)
3. descriptionn
   - user_id에 대응하는 사용자의 post 조회
   - title로 포스트 조회
4. response body
   - nickname (string)
   - title(string)
   - text(string)
   - status : success , failed
   - reason : 실패시 실패 원인 
~~~
{
   "status" : "success",
   "nickname" : "double_d_eo",
   "title" : "덥다",
   "text" :"에어컨이 안돼서 너무 더워요"
}
{
   "status" : "failed",
   "reason" : "cannot find posts"
}
~~~

## 포스트의 코멘트 조회하기
1. Endpoint
   -GET/users/<user_id>/post/comment
2. Request body
   - title (string, opt)
3. Description
   - user_id에 대응하는 사용자의 포스트의 코멘트 조회
4. Respond body


## 특정 포스트에 커멘트 달기
1. Endpoint
   -POST/users/<user_id>/post/comment
2. Request body
   -user_id(int) : 커멘트 다는 사용자의 id
   -comment(string) : 커멘트
3. Description 
   - 
4. Response body
   -status(string) :성공, 실패
   -comment(string): 성공시 커멘트 반환
   -reason(string): 실패시 이유


# 소셜
## 다른 사용자 조회
## 팔로우 신청
## 팔로우한 목록 조회
## 자신에게 팔로우 요청한 목록 조회
## 팔로우를 수락/거절

# 메시지
## DM 보내기
## DM 조회하기
## DM 삭제하기

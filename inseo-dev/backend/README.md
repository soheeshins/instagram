# REST API Spec.

- version 0.1 (2025/6/11)

# 사용자 계정

## 사용자 생성

1. Endpoint
   - POST /users
2. Request body
   - nickname (string): 사용자 nickname, 필수/고유
   - name (string): 사용자 이름, 필수
   - password (string): 비밀번호, 필수
   - age (int): 사용자 나이
   - email (string): 사용자 email 주소

```
{
  "nickname": "inseo",
  "name": "전인서",
  "password": "1234",
  "email": "zzangis345@naver.com"
}
```

3. Description
   - 사용자 계정을 생성한다. nickname과 name, password는 필수 입력값이다.
   - nickname은 고유한 값이며 기존 사용자와 중복되면 생성이 실패한다.
4. Response body
   - status (string): created, failed
   - user_id (int): 생성 성공 시, user_id 반환
   - reason (string): 실패 시, 실패 원인

```
{
  "status": "created",
  "user_id": 105
}

{
  "status": "failed",
  "reason": "nickname, kevin is duplicated"
}
```

## 사용자 인증 (로그인)

1. Endpoint
   - POST /users/login
2. Request body
   - nickname (string): 사용자 nickname, 필수
   - password (string): 사용자 비밀번호, 필수

```
{
  "nickname": "inseo",
  "password": "1234"
}
```

3. Description
   - nickname에 해당하는 user_id를 찾아 로그인한다.
   - 해당하는 nickname이 없으면 로그인이 실패한다.
   - nickname에 해당하는 password 일치하지 않으면 로그인이 실패한다.
4. Response body
   - status (string): success, failed
   - user_id: 생성 성공시, 반환
   - reason (string): 실패시, 실패 원인

```
{
  "status": "success",
  "user_id": 1
}
```

```
{
  "status": "failed",
  "reason": "nickname, aabbcc doesn't exist"
}
```

```
{
  "status": "failed",
  "reason": "password, password doesn't match"
}
```

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
   - user (object): 조회할 사용자 정보
   - reason (string): 실패시, 실패 원인

```
{
  "status": "success",
  "user": {
    "user_id": 105,
    "nickname": "inseo",
    "name": "전인서",
    "age": 30,
    "email": "zzangis345@naver.com",
  }
}
```

```
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
```

## 사용자 정보 수정

1. Endpoint
   - PUT /users/<user_id>
     - user_id (int): 수정할 사용자 id
2. Request body
   - nickname (string): 사용자 nickname
   - name (string): 사용자 이름
   - password (string): 비밀번호
   - age (int): 사용자 나이
   - email (string): 사용자 email 주소
3. Description
   - user_id에 해당하는 사용자 계정을 수정한다.
   - user_id가 없으면 조회가 실패한다.
4. Response body
   - status (string): success, failed
   - user (object): 조회할 사용자 정보
   - reason (string): 실패시, 실패 원인

```
{
  "status": "success",
  "user": {
    "user_id": 105,
    "nickname": "inseo_two",
    "name": "전인서",
    "age": 31,
    "email": "zzangis345@naver.com",

  }
}
```

```
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
```

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

```
{
  "status": "deleted"
}
```

```
{
  "status": "failed",
  "reason": "user_id, 101 doesn't exist"
}
```

# 포스팅

## 포스트 올리기

1. Endpoint
   - POST /posts
2. Request body
   - post_title (string): 포스트 제목, 필수
   - post_text (string): 포스트 내용, 필수
   - user_id(int): 작성자 user_id, 필수

```
{
  "post_title": "포스트 제목",
  "post_text": "포스트 내용"
  "user_id": 105
}
```

3. Description
   - 포스트를 생성한다. post_title과 post_text, user_id는 필수 입력값이다.
4. Response body
   - status (string): created, failed
   - post_id (int): 생성 성공 시, post_id 반환
   - posting_date (datetime): 생성 성공시, posting_date 반환
   - reason (string): 실패 시, 실패 원인

```
{
  "status": "created",
  "post_id": 105,
  "posting_date": '2025-04-26 09:00:00.007'
}
```

```
{
  "status": "failed",
  "reason": "user_id, 99 doesn't exist"
}
```

## 올라온 포스트 조회하기

1. Endpoint
   - GET /posts
2. Request body
   - user_id (int): 조회할 특정 사용자 id
   - post_id (int): 조회할 특정 포스트 id
3. Description
   - post_id, user_id에 해당하는 포스트를 조회한다.
   - post_id가 없으면 조회가 실패한다.
   - 디폴트로 전체 포스트가 조회된다.
4. Response body
   - status (string): success, failed
   - posts (array of objects):
     - post_id (int) : 조회한 포스트 id
     - user_id (int) : 조회한 포스트 작성자 id
     - post_title (string): 포스트 제목
     - post_text (string): 포스트 내용
     - posting_date (datetime): 개시 날짜
   - reason (string): 실패시, 실패 원인

```
{
  "status": "success",
  "posts":
  [{
    "post_title": "this is post title",
    "post_text": "this is post text",
    "posting_date": "2025-04-26 09:00:00.007",
    "user_id": 1,
    "post_id": 1
  }]
}
```

```
{
  "status": "failed",
  "reason": "post_id, 101 doesn't exist"
}
```

## 포스트의 커맨트 조회하기

1. Endpoint
   - GET /posts/<post_id>/comments
     - post_id (int): 조회할 포스트 id
2. Request body
   - 없음
3. Description
   - post_id에 해당하는 포스트의 커맨트를 조회한다.
   - post_id가 없으면 조회가 실패한다.
   - 커맨트가 없으면 조회가 실패한다.
4. Response body
   - status (string): success, failed
   - comments (array):
     - comment_id (int): 성공시, 커맨트 id 반환
     - post_id (int): 성공시, 포스트 id 반환
     - user_id (int): 성공시, 해당 커맨트 작성 유저 id 반환
     - comment_text (string): 성공시, 커맨트 내용 반환
   - reason (string): 실패시, 실패 원인

```
{
  "status": "success",
  "comments":
  [{
    "comment_id":1,
    "post_id":105,
    "user_id":1,
    "comment_text":"this is comment text"
  }]
}
```

```
{
  "status": "failed",
  "reason": "post_id, 101 doesn't exist"
}
```

## 특정 포스트에 커맨트 달기

1. Endpoint
   - POST /posts/<post_id>/comments
     - post_id (int): 커맨트를 작성할 포스트 id
2. Request body
   - user_id (int): 커맨트를 작성할 사용자 id, 필수
   - comment_text (string): 커맨트 내용, 필수

```
{
  "user_id": 1,
  "comment_text": "커맨트 내용"
}
```

3. Description
   - 특정 포스트에 커맨트를 생성한다. user_id, comment_text는 필수 입력값이다.
   - post_id가 없으면 커맨트 생성을 실패한다.
4. Response body
   - status (string): created, failed
   - comment_id (int): 생성 성공 시, post_id 반환
   - reason (string): 실패 시, 실패 원인

```
{
  "status": "created",
  "comment_id": 105,
}
```

```
{
  "status": "failed",
  "reason": "post_id, 101 doesn't exist"
}
```

# 소셜

## 다른 사용자 조회

1. Endpoint
   - GET /users
2. Request body
   - search (string): 조회할 닉네임 또는 이름
3. Description
   - search에 해당하는 사용자 계정을 조회한다.
   - 디폴트로 전체 사용자를 조회한다.
4. Response body
   - status (string): success, failed
   - users (array):
     - user_id (int)
     - nickname (string)
     - name (string)
     - age (int)
     - email (string)
   - reason (string): 실패 시, 실패 원인

```
{
  "status":"success",
  "users": [{...}]
}
```

## 팔로우 신청

1. Endpoint

   - POST /follows

2. Request body
   - follower_id (int): 팔로우 신청을 보낸 user_id, 필수
   - followee_id (int): 팔로우할 대상 user_id, 필수

```
{
  "follower_no": 105,
  "followee_no": 106
}
```

3. Description
   - 팔로우 요청을 생성한다.
   - follower_id, followee_id 조합은 고유로, 중복되어서는 안된다.
4. Response body
   - status (string): "created" 또는 "failed"
   - follow_id (int): 생성된 follow 요청 id
   - reason (string): 실패 시 원인

```
{
  "status": "created",
  "follow_id": 50
}
```

```
{
  "status": "failed",
  "reason": "The follow request has already been sent."
}
```

## 팔로우한 목록을 조회

1. Endpoint
   - GET /users/<user_id>/follows
     - user_id (int): 팔로우한 목록을 조회할 사용자 id
2. Request body
   - 없음
3. Description
   - user_id가 팔로우한 사용자 목록을 반환한다.
4. Response body
   - status (string): "success" 또는 "failed"
   - following (array of objects):
     - follow_id (int)
     - user_id (int)
     - name (string)
     - nickname (string)
   - reason (string): 실패 시 원인

```
{
  "status": "success",
  "following": [ { ...  } ]
}
```

## 자신에게 팔로우 요청한 목록을 조회

## 팔로우를 수락/거절

# 메시지

## DM을 보내기

## DM 조회하기

## DM 삭제하기

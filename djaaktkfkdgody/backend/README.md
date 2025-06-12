### 사용자 생성 API

- **Method**: POST
- **Endpoint**: /users
- **Request Body**:
  - nickname (필수)
  - name (필수)
  - password (필수)
  - email (선택)
  - age (선택)

- **요청 예시**:
```json
{
  "nickname": "kevin",
  "name": "이승학",
  "password": "1234",
  "email": "kevin.spreatics@gmail.com"
}


# 성공 응답
~~~
{
  "status": "created",
  "user_id": 105
}
~~~

# 실패 응답
~~~
{
  "status": "failed",
  "reason": "nickname, kevin is duplicated"
}
~~~

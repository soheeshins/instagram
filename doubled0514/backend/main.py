from flask import Flask, request 
import pymysql
from datetime import datetime 
app = Flask(__name__)
def get_connection():
    return pymysql.connect(
        host='database-1.cts2qeeg0ot5.ap-northeast-2.rds.amazonaws.com',
        user='kevin',
        password='spreatics*',
        db='insta_doubled',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
     )

# 1. 사용자
@app.route("/users",methods = ['POST'])
def newid():
    data = request.get_json()
    nickname = data.get('nickname')
    password = data.get('password')
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    conn = get_connection()
    with conn.cursor() as cursor:
        try:
            sql = """
            INSERT INTO users (nickname, name, password, age, email) 
                values (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (nickname, name, password, age, email))
            conn.commit()

        except pymysql.err.IntegrityError as e:
            return { "status": "failed", "reason": str(e) }
        
        cursor.execute("SELECT LAST_INSERT_ID()")
        result = cursor.fetchone()  
        user_id = result['LAST_INSERT_ID()']

    return {"user_id" : user_id} 

@app.route("/users/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data['nickname']
    password = data['password']
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("select * from users where nickname = %s and password = %s",(nickname,password))
        user = cursor.fetchone()

        if not user :
            return {'status':'failed','reason':'wrong nickname or password'}
    
    return {'status':'success','user_id':user['user_id']}

@app.route('/users')
def check():
    data = request.get_json()
    user_id = data.get('user_id')
    nickname = data.get('nickname')
    email = data.get('email')
    name = data.get('name')
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(
            "select nickname, name, age, email, user_id from users where user_id = %s or name = %s or email = %s or nickname =%s ", (user_id,name,email,nickname))
        user = cursor.fetchone()
        if not user :
            return {'status':'failed', 'reason':'wrong informaion'}
    return {'nickname':user['nickname'], 'name':user['name'], 'email':user['email'],'user_id':user['user_id'] }        

@app.route('/users/<user_id>/<password>', methods = ['PUT'])
def edit(user_id,password):
    data = request.get_json()
    fields = []
    values = []
    if 'password' in data :
        fields.append('password = %s')
        values.append(data['password'])
    if 'nickname' in data:
        fields.append("nickname = %s")
        values.append(data['nickname'])
    if 'name' in data:
        fields.append("name = %s")
        values.append(data['name'])
    if 'age' in data:
        fields.append("age = %s")
        values.append(data['age'])
    if 'email' in data:
        fields.append("email = %s")
        values.append(data['email'])
    if not fields :
        return {'status':'failed','reason':'No update'}

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute( "select * from users where user_id = %s and password = %s",(user_id,password))
        user = cursor.fetchone()

        if not user :
            return {'status':'failed','reason':'Invalid user_id or password'}
        
        sql = f"update users set {', '.join(fields)} where user_id = %s"
        values.append(user_id)
        cursor.execute(sql,tuple(values))
        conn.commit()
    return {'status': 'success', 'message': 'User info updated'}

@app.route('/users/<user_id>/<password>', methods=['DELETE'])
def delete(user_id, password):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE user_id = %s AND password = %s", (user_id, password))
        user = cursor.fetchone()
        if not user:
            return {'status': 'failed', 'reason': 'Invalid user_id or password'}, 403

        cursor.execute("DELETE FROM users WHERE user_id = %s AND password = %s", (user_id, password))
        conn.commit()
    return {'status': 'deleted', 'message': f'User {user_id} deleted'}




# post
@app.route('/posts/<user_id>',methods = ['POST'])
def post (user_id):
    data = request.get_json()
    title = data.get('title')
    text = data.get('text')
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT 1 FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            return {'status': 'failed', 'reason': 'invalid user_id'}

        cursor.execute("insert into post (user_id,title,text,created_at) values (%s,%s,%s,%s) ",(user_id,title,text,created_at))
        conn.commit()
        post_id = cursor.lastrowid

    return {'status':'success','created_at':created_at, 'post_id':post_id}    

@app.route('/posts')
def viewpost():
    data = request.get_json()
    post_id = data.get('post_id')
    user_id = data.get('user_id')
    nickname = data.get('nickname')
    title = data.get('title')
       
    query = """
            SELECT u.nickname, p.title, p.text
            FROM post p
            JOIN users u ON p.user_id = u.user_id
            WHERE 1=1
        """
    params = []

    if post_id:
        query += " AND p.post_id = %s"
        params.append(post_id)
    if user_id:
        query += " AND p.user_id = %s"
        params.append(user_id)
    if nickname:
        query += " AND u.nickname = %s"
        params.append(nickname) 
    if title:
        query += " AND p.title = %s"
        params.append(title)

    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, tuple(params))
        result = cursor.fetchall()
        if not result :
            return {"stats":"failed","reason":"cannot find posts"}
    return result

@app.route('/posts/<post_id>/comment/<user_id>',methods =["POST"])
def comment(post_id,user_id):
    data = request.get_json()
    comment = data['comment']
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute('select 1 from users where user_id = %s',(user_id))
        user = cursor.fetchone()
        if not user:
            return {'status':'faield','reason':'invalid user'}
        cursor.execute("insert into comment (user_id,post_id,comment) values (%s,%s,%s)",(user_id,post_id,comment)) 
        conn.commit()
        comment_id = cursor.lastrowid

    return {'status': 'success', "comment_id":comment_id}

@app.route('/posts/<post_id>/comment')
def viewcomment(post_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("""select p.title as "글제목", p.text as "내용", p.user_id as "글쓴이", c.user_id as"댓글단이", c.comment from comment c 
                       join post p on c.post_id = p.post_id
                       where c.post_id = %s""",(post_id,))
        result = cursor.fetchall()
    if not result :
        return {'satus':'faield', 'reason':'Invalid Input'}
    return result

# social

@app.route('/follow/<follower_id>/<followee_id>',methods = ['POST'])
def follow(follower_id,followee_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = %s", (follower_id,))
        follower_exists = cursor.fetchone()
        cursor.execute("SELECT COUNT(*) FROM users WHERE user_id = %s", (followee_id,))
        followee_exists = cursor.fetchone()
        if follower_exists == 0 or followee_exists == 0:
            return {'status': 'failed', 'message': '존재하지 않는 user_id입니다'}
        
        cursor.execute("""
            insert into follows (follower_id,followee_id) values (%s,%s)
                       """,(follower_id,followee_id))
        conn.commit()
        follow_id = cursor.lastrowid
    return {'message':'팔로우 신청 완료','status':'pending','follow_id':follow_id}


#팔로우한 목록
@app.route('/follow/following/<follower_id>')
def viewfollowing (follower_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute('select 1 from users where user_id = %s',(follower_id,))
        follower = cursor.fetchone()
        if not follower :
            return {'message':'invalid user'}
        cursor.execute("""
                select u.user_id, u.nickname, u.name, u.email
                       from follows f 
                       join users u on f.followee_id = u.user_id
                       where f.follower_id = %s
                       """,(follower_id,))
        followees = cursor.fetchall()
    following_list = []
    for row in followees:
        following_list.append({
            'user_id': row['user_id'],
            'nickname': row['nickname'],
            'name': row['name'],
            'email': row['email']
        })
    return {'following': following_list}
# 팔로우 요청한 목록
@app.route('/follow/request/<followee_id>')
def viewfollower(followee_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("select 1 from users where user_id = %s",(followee_id,))
        followee_exists = cursor.fetchone()
        if not followee_exists :
            return{'message':'invalid user'}
        cursor.execute("""
            SELECT u.user_id, u.nickname, u.name, u.email,f.status
            FROM follows f
            JOIN users u ON f.follower_id = u.user_id
            WHERE f.followee_id = %s and f.status = 'pending'
        """, (followee_id,))
        followers = cursor.fetchall()
    follower_list = []
    for row in followers:

        follower_list.append({
            'user_id': row['user_id'],
            'nickname': row['nickname'],
            'name': row['name'],
            'email': row['email']
        })
    return {'followers': follower_list}

@app.route('/follow/request/<followee_id>', methods = '[POST]')
def accpetfollow(followee_id):
    
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute

app.run(debug=True,host = '0.0.0.0', port = 5000)
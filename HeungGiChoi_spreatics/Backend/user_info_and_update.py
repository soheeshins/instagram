from flask import Flask, request
import pymysql

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='gmdtm457^^',
        db='create_account',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

app = Flask(__name__)
@app.route('/users/<user_id>')
def get_info(user_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        sql = """select *
                 from users
                 where user_id = %s;"""
        cursor.execute(sql, (user_id))
        rows = cursor.fetchall()

        return {"status": "selected", 
                "user_id": rows[0]['user_id'], 
                "nickname": rows[0]['nickname'], 
                "password": rows[0]['password'],
                "name": rows[0]['name'], 
                "age": rows[0]['age'], 
                "email": rows[0]['email']}

@app.route('/user_update/<user_id>', methods=['PUT'])
def update_info(user_id):
    info = get_info(user_id)
    new_info = info.copy()
    data = request.get_json()

    auth_nickname = data.get('auth_nickname')
    auth_password = data.get('auth_password')

    if((auth_nickname is None) or (auth_password is None)):
        return {"status": "failed", "reason": "You will need to re-authenticate to edit your information."}
    
    for key_1, value_1 in data.items():
        new_info[key_1] = value_1
    
    conn = get_connection()

    with conn.cursor() as cursor:
        sql_1 = """select *
                   from users
                   where nickname = %s
                        and password = %s;"""
        cursor.execute(sql_1, (auth_nickname, auth_password))

        rows = cursor.fetchall()
        if len(rows) == 1:
            sql_2 = """update users
                        set nickname = %s, password = %s, email = %s
                        where user_id = %s;"""
            cursor.execute(sql_2, (new_info['nickname'], new_info['password'], new_info['email'], user_id))
            conn.commit()
            return {"status": "Update", "chg_nickname": new_info['nickname'], "chg_password": new_info['password'], "chg_email": new_info['email']}
        elif len(rows) == 0:
            return {"status": "failed", "reason": "auth_nickname, auth_password was unmatched"}
        
app.run(debug=True, host='0.0.0.0', port=5000)
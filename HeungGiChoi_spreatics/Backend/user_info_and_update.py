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

    if data.get('chg_nickname'):
        chg_nickname = data.get('chg_nickname')
    else:
        chg_nickname = new_info.get('nickname')

    if data.get('chg_password'):
        chg_password = data.get('chg_password')
    else:
        chg_password = new_info.get('password')
    
    if data.get('chg_email'):
        chg_email = data.get('chg_email')
    else:
        chg_email = new_info.get('email')

    if((auth_nickname is None) or (auth_password is None)):
        return {"status": "failed", "reason": "You will need to re-authenticate to edit your information."}
    
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
            cursor.execute(sql_2, (chg_nickname, chg_password, chg_email, user_id))
            conn.commit()
            return {"status": "Update", "chg_nickname": chg_nickname, "chg_password": chg_password, "chg_email": chg_email}
        elif len(rows) == 0:
            return {"status": "failed", "reason": "auth_nickname, auth_password was unmatched"}
        
app.run(debug=True, host='0.0.0.0', port=5000)    
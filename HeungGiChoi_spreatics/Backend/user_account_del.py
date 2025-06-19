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
@app.route('/users/<user_id>', methods=['DELETE'])
def del_user(user_id):
    data = request.get_json()

    auth_nickname = data.get('auth_nickname')
    auth_password = data.get('auth_password')

    if (auth_nickname is None) or (auth_password is None):
        return {"status": "failed", "reason": "You must re-authenticate to delete account."}
    
    conn = get_connection()

    with conn.cursor() as cursor:
        sql_1 = """select *
                   from users
                   where nickname = %s
                        and password = %s;"""
        cursor.execute(sql_1, (auth_nickname, auth_password))

        rows = cursor.fetchall()
        if len(rows) == 1:
            sql = """delete from users
                    where user_id = %s;"""
            cursor.execute(sql, (user_id, ))
            conn.commit()
            return {"status": "deleted", "result": "user account was deleted"}
        elif len(rows) == 0:
            return {"status": "failed", "reason": "auth_nickname, auth_password was unmatched"}
        
app.run(debug=True, host='0.0.0.0', port=5000)
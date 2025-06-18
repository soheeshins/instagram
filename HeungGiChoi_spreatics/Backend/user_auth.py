from flask import Flask, request
import pymysql

def get_connetion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='gmdtm457^^',
        db='create_account',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

app = Flask(__name__)
@app.route('/Auth_users', methods=['POST'])
def authenticatioin_user():
    data = request.get_json()

    nickname = data.get('nickname')
    password = data.get('password')

    if((nickname is None) or (password is None)):
        return {"status": "failed", "reason": "enter both your nickname and password"}
    
    conn = get_connetion()

    with conn.cursor() as cursor:
        sql = """select *
                from users
                where nickname = %s
                    and password = %s;"""
        cursor.execute(sql, (nickname, password))
        rows = cursor.fetchall()
        if len(rows) == 1:
            return {"status": "log_in Succenss", "user_id": f'{rows[0]['user_id']}'}
        elif len(rows) == 0:
            return {"status": "log_in failed", "reason": "nickname, password was unmatched"} 
        
app.run(debug=True, host='0.0.0.0', port=5000)
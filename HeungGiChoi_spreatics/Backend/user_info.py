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
                "name": rows[0]['name'], 
                "age": rows[0]['age'], 
                "email": rows[0]['email']}
    
app.run(debug=True, host='0.0.0.0', port=5000)
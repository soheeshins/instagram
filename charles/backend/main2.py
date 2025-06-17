from flask import Flask, request
import pymysql
from pymysql.cursors import DictCursor

app = Flask(__name__)
# MySQL 연결 함수


app.run(debug=True, host='0.0.0.0', port=5000)

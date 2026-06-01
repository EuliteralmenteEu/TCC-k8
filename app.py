from flask import Flask, render_template
import mysql.connector as mysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    return mysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'username'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'almoxarifado')
    )

@app.route('/')
def index():
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM table_name")
        data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    
    return render_template('index.html', data=data)

@app.route('/estoque')
def estoque():
    connection = get_db_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estoque")
        data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()
    
    return render_template('estoque.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

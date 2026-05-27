from flask import Flask, render_template
import mysql.connector as mysql

app = Flask(__name__)

db = mysql.connect(
    host="localhost",
    user="username",
    password="password",
    database="name"
)

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM table_name")
    data = cursor.fetchall()
    cursor.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

if __name__ == '__main__':
    app.run(debug=True)
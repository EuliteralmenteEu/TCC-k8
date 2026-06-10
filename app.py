from flask import Flask
import mysql.connector 
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Satanael vai se libertar do senai!"


if __name__ == "__main__":
    app.run(debug=True)

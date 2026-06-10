from flask import Flask
import mysql.connector 
import os


app = Flask(__name__)


@app.route("/")
def home():
    return "Olá, mundo! Este é o documento padrão do Flask."


if __name__ == "__main__":
    app.run(debug=True)

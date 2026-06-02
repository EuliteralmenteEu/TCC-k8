from flask import Flask, render_template, redirect, url_for
import mysql.connector as mysql
from mysql.connector import Error
import os
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db_connection():
    """
    Estabelece uma conexão com o database, se estabelecer ele mostrará o objeto, se falhar vai mostrar uma mensagem de erro
    """
    try:
        connection = mysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "username"),
            password=os.getenv("DB_PASSWORD", "password"),
            database=os.getenv("DB_NAME", "almoxarifado"),
            autocommit=True,
            connection_timeout=10
        )  
        return connection
    except Error as e:
        logger.error(f"Database connection failed: {e}")
        return None


@app.route("/")
def index():
    """
    Index route - redirects to cadastrar page
    """
    return redirect(url_for("cadastrar"))


@app.route("/cadastrar")
def cadastrar():
    """
    Cadastrar route - main screen for registration
    """
    return render_template("cadastrar.html")


@app.route("/estoque")
def estoque():
    """
    Estoque route - mostra os dados do inventario
    """
    connection = None
    data = []
    error_msg = None  # Add this
    
    try:
        connection = get_db_connection()
        if connection is None:
            logger.warning("Estoque: falhou na conexão")
            error_msg = "Database falhou na conexão"
        else:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM estoque")
            data = cursor.fetchall()
            cursor.close()
    except Error as e:
        logger.error(f"Estoque - Database error: {e}")
        data = []
        error_msg = "Failed to retrieve inventory data"
    finally:
        if connection and connection.is_connected():
            connection.close()

    return render_template("estoque.html", data=data, error=error_msg)

if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "5000"))
    )

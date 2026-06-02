from flask import Flask, render_template
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
    Index route - mostra coisas do database.
    """
    connection = None
    data = []
    error_msg = None  # Variável para armazenar o erro, se houver

    try:
        connection = get_db_connection()
        if connection is None:
            logger.warning("Index: conexão invalida")
            error_msg = "Database falhou em se conectar"
        else:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM items")
            data = cursor.fetchall()
            cursor.close()
            
    except Error as e:
        logger.error(f"Index - Database error: {e}")
        data = []
        error_msg = "Failed to retrieve data"
        
    finally:
        if connection and connection.is_connected():
            connection.close()

    # Um único ponto de saída para a rota
    return render_template("index.html", data=data, error=error_msg)


@app.route("/estoque")
def estoque():
    """
    Estoque route - mostra os dados do inventario
    """
    connection = None
    data = []
    try:
        connection = get_db_connection()
        if connection is None:
            logger.warning("Estoque: falhou na conexão")
            return render_template("estoque.html", data=data, error="Database falhu na conexão")
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estoque")
        data = cursor.fetchall()
        cursor.close()
    except Error as e:
        logger.error(f"Estoque - Database error: {e}")
        data = []
        return render_template("estoque.html", data=data, error="Failed to retrieve inventory data")
    finally:
        if connection and connection.is_connected():
            connection.close()

    return render_template("estoque.html", data=data)


if __name__ == "__main__":
    app.run(
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "5000"))
    )


from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def get_db_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
            return conn
        except:
            print("Waiting for DB...")
            time.sleep(2)

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    cursor.execute("INSERT INTO users (name) VALUES ('Suma')")
    conn.commit()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    return str(data)

app.run(host="0.0.0.0", port=5000)
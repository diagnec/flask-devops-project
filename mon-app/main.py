from flask import Flask, jsonify  # Ajout de jsonify
import os
import psycopg2

app = Flask(__name__)

# Connexion à la base de données
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        return None

@app.route("/")
def home():
    return "Hello Cheikh, Bienvenue dans Kubernetes"

@app.route("/health")
def health():
    return {"Status": "ok"}

@app.route("/db")
def check_db():
    conn = get_db_connection()
    if conn:
        conn.close()
        return jsonify({"database": "connected"})
    else:
        return jsonify({"database": "not connected"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

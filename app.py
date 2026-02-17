from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create DB automatically
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/add", methods=["POST"])
def add_question():
    data = request.json
    question = data.get("question")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO questions (question) VALUES (?)", (question,))
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})

@app.route("/all", methods=["GET"])
def get_all():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "question": row[1]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an academic tutor. Answer clearly and concisely."},
            {"role": "user", "content": question}
        ]
    )

    return jsonify({
        "answer": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run()

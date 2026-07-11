from flask import Flask, render_template, request, jsonify

from search_knowledge import search_knowledge, ask_openrouter

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question", "")

    context = search_knowledge(question)

    reply = ask_openrouter(question, context)

    return jsonify({

        "question": question,

        "reply": reply

    })


if __name__ == "__main__":

    app.run(debug=True)
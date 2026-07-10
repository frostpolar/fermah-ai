from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def search_knowledge(question):

    with open(
        "knowledge.txt",
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    question_words = question.lower().split()

    paragraphs = text.split("\n\n")

    scored = []

    for paragraph in paragraphs:

        score = 0

        for word in question_words:

            if len(word) > 2 and word in paragraph.lower():
                score += 1

        # Only keep paragraphs with at least 2 matching words
        if score >= 2:
            scored.append((score, paragraph))

    if not scored:
        return "I couldn't find information about that topic."

    # Sort from highest score to lowest
    scored.sort(key=lambda x: x[0], reverse=True)

    top_sections = []

    seen = set()

    for score, paragraph in scored:

        cleaned = paragraph.strip()

        if cleaned not in seen:

            seen.add(cleaned)

            top_sections.append(cleaned)

        # Stop after 3 unique paragraphs
        if len(top_sections) == 3:
            break

    return "\n\n".join(top_sections)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question", "")

    reply = search_knowledge(question)

    return jsonify({
        "question": question,
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)
import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("OPENROUTER_API_KEY:", repr(OPENROUTER_API_KEY))

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

        if score >= 2:
            scored.append((score, paragraph))

    if not scored:
        return "I couldn't find information about that topic."

    scored.sort(key=lambda x: x[0], reverse=True)

    top_sections = []

    seen = set()

    for score, paragraph in scored:

        cleaned = paragraph.strip()

        if cleaned not in seen:

            seen.add(cleaned)

            top_sections.append(cleaned)

        if len(top_sections) == 3:
            break

    return "\n\n".join(top_sections)


def ask_openrouter(question, context):

    headers = {

        "Authorization": f"Bearer {OPENROUTER_API_KEY}",

        "Content-Type": "application/json"

    }

    prompt = f"""
You are Fermah AI.

You are a friendly assistant for the Fermah ecosystem.

If the user greets you or asks general conversational questions
like "hello", "how are you", or "who are you",
respond naturally.

For questions about Fermah, answer ONLY using the knowledge below.

If the answer is not in the knowledge, politely explain that you
don't have that information.

Knowledge:

{context}

Question:

{question}
"""
    
    response = requests.post(

        "https://openrouter.ai/api/v1/chat/completions",

        headers=headers,

        json={

            "model": "tencent/hy3:free",

            "messages":[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        }

    )

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)

    if response.status_code != 200:
        return f"OpenRouter Error:\n{response.text}"

    data = response.json()

    return data["choices"][0]["message"]["content"]
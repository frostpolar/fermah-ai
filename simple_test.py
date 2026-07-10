import ollama

response = ollama.chat(
    model="phi3:mini",
    messages=[
        {
            "role": "user",
            "content": "what is fermah?"
        }
    ]
)

print(response["message"]["content"])
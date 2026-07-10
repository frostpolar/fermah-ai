import chromadb
import ollama

question = input("Ask a question: ")

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="project_knowledge"
)

results = collection.query(
    query_texts=[question],
    n_results=1
)

context = results["documents"][0][0]

prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

response = ollama.chat(
    model="phi3:mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nANSWER:\n")
print(
    response["message"]["content"]
)
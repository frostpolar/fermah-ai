import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="project_knowledge"
)

with open(
    "knowledge.txt",
    "r",
    encoding="utf-8"
) as f:

    data = f.read()

collection.add(
    documents=[data],
    ids=["fermah"]
)

print("stored successfully")
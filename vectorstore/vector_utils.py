import os
import json
import chromadb
from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer


def load_cleaned_articles(json_path):
    with open(json_path, "r") as f:
        return json.load(f)


def create_vector_store(collection_name="news_articles", data_path="data/processed/"):
    client = chromadb.PersistentClient(path=".chroma_store")

    # Reset collection if it exists
    if collection_name in [c.name for c in client.list_collections()]:
        client.delete_collection(collection_name)

    collection = client.create_collection(collection_name)

    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Load latest cleaned file
    json_files = sorted([f for f in os.listdir(data_path) if f.endswith(".json")])
    if not json_files:
        raise ValueError("No processed files found in data/processed/")

    latest_file = os.path.join(data_path, json_files[-1])
    articles = load_cleaned_articles(latest_file)

    texts = [f"{a['title']} — {a['summary']}" for a in articles]
    ids = [f"article_{i}" for i in range(len(articles))]
    metadatas = [
        {"title": a["title"], "link": a["link"], "published": a["published"]}
        for a in articles
    ]

    embeddings = model.encode(texts)

    collection.add(documents=texts, embeddings=embeddings, ids=ids, metadatas=metadatas)

    # client.persist()
    print(f"Stored {len(texts)} articles into ChromaDB collection '{collection_name}'")


if __name__ == "__main__":
    create_vector_store()

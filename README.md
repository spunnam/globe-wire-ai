# 🌐 Globe-Wire AI — Real-Time News Intelligence with Agentic AI

Globe-Wire AI is an agentic AI-powered system that fetches, analyzes, and answers questions about **real-time global news** using state-of-the-art open-source tools. It combines live data fetching, semantic understanding, and retrieval-augmented generation (RAG) to deliver meaningful insights from current events.

---

## 🔍 What It Does

- 📡 Fetches the latest news articles using Google News RSS
- 🧹 Cleans and preprocesses articles (removes HTML, decodes text)
- 🧠 Embeds articles using sentence-transformers
- 📦 Stores them in a local vector database using ChromaDB
- 🤖 Powers similarity-based search and intelligent Q&A (coming soon)

---

## 💡 Use Cases

- 🗞️ Stay informed on complex global events
- 📊 Analysts tracking trends and sentiment
- 🧑‍💼 Journalists and researchers doing deep-dive investigations
- 🧠 Demo for agentic AI workflows and interviews

---

## 🧰 Tech Stack

| Layer      | Tool                                                   |
| ---------- | ------------------------------------------------------ |
| Language   | Python 3.10+                                           |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`)           |
| Vector DB  | `ChromaDB` (DuckDB + Parquet backend)                  |
| Fetching   | RSS via `feedparser`, optionally extendable to NewsAPI |
| Frameworks | Modular custom agents (LangGraph/LLM to be integrated) |

---

## 📁 Current Structure

```
globe-wire-ai/
├── data/                # Raw and processed articles
├── ingest/              # Scripts to fetch and save news
├── extract/             # Clean & preprocess news
├── vectorstore/         # Create and manage embeddings
├── .env                 # API keys and secrets (not committed)
├── config.yaml          # Config file for sources and settings
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🛣️ Roadmap

- [x] Real-time news ingestion using RSS
- [x] Article cleaning & processing
- [x] Vector embedding + ChromaDB storage
- [ ] Semantic search using embeddings
- [ ] LLM-powered Q&A system
- [ ] Frontend using Streamlit for interactive use

---

## ⚙️ Setup Instructions

```bash
# Create and activate a virtual environment (conda recommended)
conda create -n globe-wire python=3.10
conda activate globe-wire

# Install dependencies
pip install -r requirements.txt

# Run initial pipeline
python ingest/save_news.py
python extract/clean_articles.py
python vectorstore/vector_utils.py
```

---

## 👨‍💻 Author

**Samarasimha Reddy Punnam**  
[GitHub](https://github.com/spunnam) | [LinkedIn](https://www.linkedin.com/in/spunnam)

---

## 🛡️ License

This project is open-source under the [MIT License](LICENSE).

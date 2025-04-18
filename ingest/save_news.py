import os
import json
from datetime import datetime
from fetch_news import fetch_google_news


def save_articles(query="global", max_results=5):
    articles = fetch_google_news(query, max_results)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"data/raw/{query.replace(' ', '_')}_{timestamp}.json"

    os.makedirs("data/raw", exist_ok=True)
    with open(filename, "w") as f:
        json.dump(articles, f, indent=2)

    print(f"Saved {len(articles)} articles to {filename}")


if __name__ == "__main__":
    save_articles(query="Trump tariffs", max_results=5)

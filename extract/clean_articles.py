import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
import html


def clean_html(raw_html):
    if raw_html:
        # 1. Remove HTML tags
        text = BeautifulSoup(raw_html, "html.parser").get_text()
        # 2. Decode HTML entities (like &amp;, &quot;)
        return html.unescape(text)
    return ""


def clean_articles(input_path, output_path):
    with open(input_path, "r") as f:
        articles = json.load(f)

    cleaned_articles = []
    for article in articles:
        cleaned_summary = clean_html(article.get("summary", ""))
        cleaned_title = clean_html(article.get("title", ""))

        cleaned_articles.append(
            {
                "title": cleaned_title.strip(),
                "link": article.get("link", "").strip(),
                "published": article.get("published", "").strip(),
                "summary": cleaned_summary.strip(),
            }
        )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(cleaned_articles, f, indent=2)

    print(f"Cleaned {len(cleaned_articles)} articles saved to {output_path}")


if __name__ == "__main__":
    # Example usage: clean the most recent file
    from glob import glob

    files = sorted(glob("data/raw/*.json"))
    if not files:
        print("No raw files found in data/raw/")
    else:
        latest = files[-1]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"data/processed/cleaned_{timestamp}.json"
        clean_articles(latest, output_file)

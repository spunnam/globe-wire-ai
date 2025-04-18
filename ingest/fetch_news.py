import feedparser


def fetch_google_news(query="global", max_results=5):
    query = query.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"

    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries[:max_results]:
        article = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary,
        }
        articles.append(article)

    return articles


if __name__ == "__main__":
    # Example usage
    results = fetch_google_news("Trump tariffs", max_results=3)
    for i, article in enumerate(results):
        print(f"\n[{i+1}] {article['title']}")
        print(f"Published: {article['published']}")
        print(f"Link: {article['link']}")
        print(f"Summary: {article['summary'][:200]}...")

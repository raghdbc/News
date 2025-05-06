import requests
import streamlit as st
from datetime import datetime, timedelta

def fetch_news(topic, num_articles=10):
    """Fetches the latest news articles from NewsAPI."""
    api_key = st.secrets["general"]["NEWS_API_KEY"]
    
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    url = f'https://newsapi.org/v2/everything?q={topic}&from={yesterday}&sortBy=publishedAt&pageSize={num_articles}&apiKey={api_key}'
    
    response = requests.get(url).json()
    articles = response.get("articles", [])

    # Get the actual number of articles found
    available_articles = len(articles)
    
    news_data = []
    for article in articles[:available_articles]:  
        image_url = article.get("urlToImage") or "https://via.placeholder.com/300?text=No+Image"

        news_data.append({
            "title": article.get("title", "No Title"),
            "description": article.get("description", "No description available"),
            "image": image_url,
            "url": article.get("url", "#"),
            "published_at": article.get("publishedAt", "Unknown date"),
        })

    return news_data, available_articles

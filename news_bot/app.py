import streamlit as st
from news_fetcher import fetch_news
from email_handler import send_email

st.title("📰 Daily News Newsletter")

# User selects category
interests = ["Technology", "Health", "Business", "Sports", "Entertainment"]
interest = st.selectbox("Choose your field of interest:", interests)

# Default max news articles (we'll adjust later)
max_articles = 10  
num_articles = st.slider("How many articles do you want?", min_value=1, max_value=max_articles, value=5)

if st.button("Fetch News"):
    news, available_articles = fetch_news(interest, num_articles)
    
    # Adjust max value dynamically
    if available_articles < num_articles:
        st.warning(f"Only {available_articles} articles found!")

    if news:
        for item in news:
            st.image(item["image"], width=300)
            st.write(f"### [{item['title']}]({item['url']})")
            st.write(f"🕒 Published: {item['published_at']}")
            st.write(item["description"])
    else:
        st.error("No fresh news found!")

# Email Subscription
if st.checkbox("Do you want this daily?"):
    email = st.text_input("Enter your email:")
    if st.button("Subscribe"):
        if email:
            news, available_articles = fetch_news(interest, num_articles)
            send_email(news, email)
            st.success("✅ Newsletter subscription successful!")
        else:
            st.error("⚠️ Please enter a valid email!")

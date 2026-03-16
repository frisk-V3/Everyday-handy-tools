import feedparser

def get_news_marquee():
    url = "https://news.yahoo.co.jp"
    try:
        feed = feedparser.parse(url)
        titles = [e.title for e in feed.entries[:10]]
        return "　　|　　".join(titles)
    except:
        return "ニュースを取得できません"

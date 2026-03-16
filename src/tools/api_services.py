import requests
import feedparser
from抽取 import GoogleTranslator # deep-translator

def get_weather():
    lat, lon, city = get_location()
    url = f"https://api.open-meteo.com{lat}&longitude={lon}&hourly=temperature_2m&daily=precipitation_sum&timezone=auto"
    try:
        data = requests.get(url).json()
        temp = data['hourly']['temperature_2m'][0]
        return f"{city}: {temp}℃"
    except:
        return "天気取得不可"

def get_news_titles():
    url = "https://news.yahoo.co.jp"
    try:
        feed = feedparser.parse(url)
        return " | ".join([e.title for e in feed.entries[:10]])
    except:
        return "ニュースオフライン"

def translate_text(text, target='ja'):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except:
        return "翻訳エラー (オフライン)"

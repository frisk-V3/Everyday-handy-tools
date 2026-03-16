import requests

def get_location():
    try:
        # IPから緯度経度取得
        data = requests.get("http://ip-api.com", timeout=3).json()
        return data.get("lat"), data.get("lon"), data.get("city")
    except:
        return None, None, None

def get_weather():
    lat, lon, city = get_location()
    if not lat: return "オフライン: 天気取得不可"
    url = f"https://api.open-meteo.com{lat}&longitude={lon}&hourly=temperature_2m&timezone=auto"
    try:
        res = requests.get(url).json()
        temp = res['hourly']['temperature_2m'][0]
        return f"{city} {temp}℃"
    except:
        return "取得エラー"

def check_umbrella_needed():
    lat, lon, _ = get_location()
    if not lat: return False
    url = f"https://api.open-meteo.com{lat}&longitude={lon}&daily=precipitation_sum&timezone=auto"
    try:
        res = requests.get(url).json()
        return res['daily']['precipitation_sum'][0] > 0.1
    except:
        return False

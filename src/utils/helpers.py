import requests

def is_online():
    try:
        requests.get("https://8.8.8.8", timeout=2)
        return True
    except:
        return False

def get_location():
    """IP-APIで現在地取得。失敗時はデフォルト値を返す"""
    try:
        res = requests.get("http://ip-api.com", timeout=3).json()
        return res.get("lat", 35.6895), res.get("lon", 139.6917), res.get("city", "不明")
    except:
        return 35.6895, 139.6917, "オフライン"

PRIVACY_POLICY = "プライバシーポリシー: 天気予報取得のためIPアドレスから位置情報を特定しますが、サーバーへの保存は行いません。"

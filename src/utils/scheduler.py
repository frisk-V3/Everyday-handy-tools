import schedule
import time
import threading
from tools.weather import check_umbrella_needed

def start_reminder(notify_func):
    def job():
        if check_umbrella_needed():
            notify_func("傘リマインダー", "今日は雨の予報です。傘を持っていきましょう！")

    schedule.every().day.at("07:00").do(job)
    
    def run():
        while True:
            schedule.run_pending()
            time.sleep(60)
            
    threading.Thread(target=run, daemon=True).start()

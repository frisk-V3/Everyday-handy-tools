import flet as ft
import schedule
import time
import threading
from tools import api_services as api, local_tools as local, helpers

def main(page: ft.Page):
    page.title = "Multi-Tool Kit"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # 7時のリマインダー通知設定 (簡易版)
    def check_rain():
        while True:
            now = time.strftime("%H:%M")
            if now == "07:00":
                # 雨判定ロジックを呼び出し、通知を出す処理
                pass
            time.sleep(60)

    threading.Thread(target=check_rain, daemon=True).start()

    # --- 上部：ニューステロップ & 天気 ---
    news_text = ft.Text(api.get_news_titles(), size=16, color="white")
    weather_text = ft.Text(api.get_weather(), weight="bold")
    
    header = ft.Container(
        content=ft.Row([news_text, weather_text], alignment="spaceBetween"),
        bgcolor=ft.colors.BLUE_GREY_900, padding=10
    )

    # --- 各タブのコンテンツ ---
    # 翻訳
    trans_input = ft.TextField(label="翻訳するテキスト")
    trans_out = ft.Text()
    tab_trans = ft.Column([trans_input, ft.ElevatedButton("翻訳", on_click=lambda _: setattr(trans_out, "value", api.translate_text(trans_input.value))), trans_out])

    # JSON
    json_input = ft.TextField(label="Raw JSON", multiline=True)
    json_out = ft.Markdown()
    tab_json = ft.Column([json_input, ft.ElevatedButton("整形", on_click=lambda _: setattr(json_out, "value", f"```json\n{local.format_json(json_input.value)}\n```")), json_out])

    # タブ構成
    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="翻訳", content=tab_trans),
            ft.Tab(text="JSON", content=tab_json),
            ft.Tab(text="QR生成", content=ft.Text("QRコード機能")),
            ft.Tab(text="Todo", content=ft.Text("Todo機能")),
        ],
        expand=1
    )

    # 全体レイアウト
    page.add(
        header,
        tabs,
        ft.Text(helpers.PRIVACY_POLICY, size=10, color="grey")
    )

ft.app(target=main)

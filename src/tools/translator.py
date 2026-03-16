from deep_translator import GoogleTranslator

def translate_text(text, target_lang='ja'):
    """APIキー不要の翻訳ツール"""
    if not text.strip():
        return ""
    try:
        # 言語は自動判別(auto)から指定言語(target)へ
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception:
        return "翻訳エラー（ネットワークを確認してください）"

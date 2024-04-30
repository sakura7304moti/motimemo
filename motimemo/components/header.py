import reflex as rx

# アプリのヘッダー
def app_header():
    return rx.hstack(
        rx.text(
            "日記帳",size='7'
        )
    )
import reflex as rx
from motimemo.options.app_color import AppColor

ac = AppColor()

def dialy_create_button():
    return rx.button(
        #画像
        rx.image(src="/okayu.png",height="48px",width="auto"),

        #style
        '日記を書く',
        height="48px",
        background_color=ac.sub(),
        color=ac.accent(),

        #onClick
        on_click = rx.redirect(
            "/create"
        )
    )
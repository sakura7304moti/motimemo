import reflex as rx
from motimemo.options.app_color import AppColor

ac = AppColor()

def dialy_create_button():
    return rx.button(
        #画像
        rx.image(src="/okayu.png",height="48px",width="auto"),

        #style
        '日記を書く',
        style = {
            "height" : "48px",
            "background_color" : "rgba(167,159,138,1)",
            "color" : "rgba(255,255,255,1)"
        },

        #onClick
        on_click = rx.redirect(
            "/create"
        )
    )
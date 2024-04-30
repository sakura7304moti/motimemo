"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from motimemo.components import header,button
from motimemo.options.app_color import AppColor

import reflex as rx

ac = AppColor()



class State(rx.State):
    """The app state."""

@rx.page(route = "/" , title = "motimemo")
def index() -> rx.Component:
    """
    page : ホーム
    """
    return rx.vstack(
        header.app_header(),
        button.dialy_create_button(),
        height="100vh",
    )

@rx.page(route = "/create" , title = "motimemo | create")
def create() -> rx.Component:
    """
    page : 日記作成画面
    """
    return rx.vstack(height="100vh")
    

style = {
    "font_family" : "Noto Sans JP",
    "font_size" : "16px",
    "background_color" : ac.base(),
    "padding" : "16px"
}

app = rx.App(style = style)
app.add_page(index)
app.add_page(create, route="/create")

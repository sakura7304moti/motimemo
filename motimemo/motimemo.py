"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from motimemo.src import const,component,table

import reflex as rx

cp = component.Component()
table.QueryModel.make_table()


class State(rx.State):
    """The app state."""

@rx.page(route = "/" , title = "motimemo")
def index() -> rx.Component:
    """
    page : ホーム
    """
    return rx.vstack(
        cp.app_header(),
        min_height="100vh",
        padding="16px"
    )

@rx.page(route = "/create" , title = "motimemo | create")
def create() -> rx.Component:
    """
    page : 日記作成画面
    """
    return rx.vstack(
        cp.app_header(),
        cp.dialy_create_dialog(),
        min_height="100vh",
        padding="16px"
    )
    

style = {
    "font_family" : "Noto Sans JP",
    "font_size" : "16px",
    "background_color" : const.AppColor.base(),
    
}

app = rx.App(style = style)
app.add_page(index)
app.add_page(create, route="/create")

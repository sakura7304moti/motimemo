import reflex as rx
import datetime

from motimemo.src.const import AppColor

#----- 定数 -----
BUTTON_STYLE = {
    "height": "32px",
    "background_color": "rgba(0,0,0,0)",
    "cursor": "pointer",
}
BUTTON_HOVER_STYLE = {"background_color": "#e0e0e0"}

#----- rx Model -----
class PhotoState(rx.State):
    """The app state."""

    # The images to show.
    img: list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_upload_dir() / file.filename

            # Save the file.
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

#----- Component -----
class Component:
    def get_today_text(self):
        return datetime.datetime.now().strftime("%Y/%m/%d")
    
    def app_header(self):
        """
        画面のヘッダー
        """
        return rx.card(
            rx.flex(
                # タイトル
                rx.text(
                    "日記帳",
                    size="7",
                ),
                # 画像
                rx.image(
                    src="/okayu.png",
                    height="32px",
                    width="auto",
                    style={"padding-right": "32px"},
                ),
                # ホーム
                rx.button(
                    # 画像
                    rx.image(src="/home_24dp.png", height="32px", width="auto"),
                    # style
                    style=BUTTON_STYLE,
                    _hover=BUTTON_HOVER_STYLE,
                    # onClick
                    on_click=rx.redirect("/"),
                ),
                # 追加
                rx.button(
                    # 画像
                    rx.image(src="/edit_note_24dp.png", height="32px", width="auto"),
                    # style
                    style=BUTTON_STYLE,
                    _hover=BUTTON_HOVER_STYLE,
                    # onClick
                    on_click=rx.redirect("/create"),
                ),
            )
        )
    
    def dialy_create_dialog(self):
        """
        日記の登録画面
        """
        return rx.card(
        rx.vstack(
            #1行目
            rx.flex(
                #タイトル
                rx.input(
                    placeholder="タイトル",
                    id="title",
                    style = {
                        "width" : "100%"
                    }
                ),
                #今日の日付
                rx.input(
                    type_="date",
                    id="date",
                    default_value=self.get_today_text()
                )
                ,spacing="5"
            ),

            #2行目 内容
            rx.text_area(
                placeholder="詳細",
                id="detail",
                style = {
                    "width" : "100%",
                    "height" : "300px"
                }
            ),

            #3行目 ファイルアップロード
            self.photo_uploader(),

            #4行目 追加ボタン
            rx.button(
                '保存する',
                style = {
                    "background_color" : AppColor.accent()
                }
            )
        ),
        
        style={
            "max-width" : "600px",
            "width" : "100%"
        }
    )

    def photo_uploader(self):
        """The main view."""
        color = AppColor.accent()
        return rx.vstack(
            rx.upload(
                rx.vstack(
                    rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                    rx.text("ファイルドロップ・クリック", color="rgba(200,200,200,1)"),
                ),
                id="photo",
                border=f"1px dotted {color}",
                padding="5em",
            ),
            rx.hstack(rx.foreach(rx.selected_files("photo"), rx.text)),
            
            #rx.button(
            #    "Upload",
            #    on_click=PhotoState.handle_upload(rx.upload_files(upload_id="photo")),
            #),

            rx.button(
                "画像のクリア",
                on_click=rx.clear_selected_files("photo"),
                background_color = "rgba(200,200,200,1)"
            ),
            rx.foreach(PhotoState.img, lambda img: rx.image(src=rx.get_upload_url(img))),
            padding="5em",
        )
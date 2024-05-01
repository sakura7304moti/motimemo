import reflex as rx
from motimemo.options.app_color import AppColor

ap = AppColor()
color = ap.accent()

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


def photo_uploader():
    """The main view."""
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

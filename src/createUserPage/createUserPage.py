
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from front_end_cud import registerUser


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def createUserPage(window):
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 322,
        width = 584,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        584.0,
        322.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        584.0,
        34.0,
        fill="#5D5FEF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: registerUser(window, entry_2.get("1.0","end-1c"), entry_1.get()),
        relief="flat"
    )
    button_1.place(
        x=229.0,
        y=188.0,
        width=127.0,
        height=29.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        292.5,
        150.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#9C9C9C",
        show="*",
        highlightthickness=0
    )
    entry_1.place(
        x=178.0,
        y=133.0,
        width=229.0,
        height=32.0
    )

    canvas.create_text(
        178.0,
        120.0,
        anchor="nw",
        text="Password:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        292.5,
        85.0,
        image=entry_image_2
    )
    entry_2 = Text(
        bd=0,
        bg="#9C9C9C",
        highlightthickness=0
    )
    entry_2.place(
        x=178.0,
        y=68.0,
        width=229.0,
        height=32.0
    )

    canvas.create_text(
        178.0,
        55.0,
        anchor="nw",
        text="Username:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_text(
        136.0,
        2.0,
        anchor="nw",
        text="Create User",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    from loginPage.loginPage import loginPage
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: loginPage(window),
        relief="flat"
    )
    button_2.place(
        x=15.0,
        y=6.0,
        width=59.0,
        height=20.0
    )
    window.resizable(False, False)
    window.mainloop()

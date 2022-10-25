from tkinter import Button, Canvas, PhotoImage, Text

from main import relative_to_assets
from requests import loginUser
#from registerPage import registerPage


def loginPage(window):
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
        file=relative_to_assets("login_button_1.png"))

    from pages.registerPage import registerPage
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: registerPage(window),
        relief="flat"
    )
    button_1.place(
        x=229.0,
        y=239.0,
        width=127.0,
        height=32.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("login_entry_1.png"))
    entry_bg_1 = canvas.create_image(
        292.5,
        150.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#9C9C9C",
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
        file=relative_to_assets("login_entry_2.png"))
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

    button_image_2 = PhotoImage(
    file=relative_to_assets("login_button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: loginUser(entry_2.get("1.0","end-1c"), entry_1.get("1.0","end-1c")),
        relief="flat"
    )
    button_2.place(
        x=229.0,
        y=188.0,
        width=127.0,
        height=29.0
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
        259.0,
        3.0,
        anchor="nw",
        text="Login",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
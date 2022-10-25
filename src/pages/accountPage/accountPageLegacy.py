from tkinter import Button, Canvas, PhotoImage

from main import relative_to_assets
from pages.createUserPage.registerPageLegacy import registerPage
from requests import getUsername


def accountPage(window):
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

    canvas.create_text(
        156.0,
        176.0,
        anchor="nw",
        text="Password: Hidden",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        156.0,
        118.0,
        anchor="nw",
        text="Username: " + getUsername(),
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        259.0,
        3.0,
        anchor="nw",
        text="Account",
        fill="#000000",
        font=("Inter", 24 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("account_button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: registerPage(window),
        relief="flat"
    )
    button_1.place(
        x=15.0,
        y=6.0,
        width=59.0,
        height=20.0
    )

    window.resizable(False, False)
    window.mainloop()

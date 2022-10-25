from tkinter import Button, Canvas, PhotoImage
from pages.accountPage import accountPage
from main import relative_to_assets


def browsePage(window):
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

    canvas.create_rectangle(
        313.0,
        56.0,
        568.0,
        299.0,
        fill="#999393",
        outline="")

    canvas.create_text(
        318.0,
        41.0,
        anchor="nw",
        text="Shared Lists:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        56.0,
        281.0,
        299.0,
        fill="#999393",
        outline="")

    canvas.create_text(
        29.0,
        41.0,
        anchor="nw",
        text="My Lists:",
        fill="#000000",
        font=("Inter", 12 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("browse_button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: accountPage(window),
        relief="flat"
    )
    button_1.place(
        x=509.0,
        y=7.0,
        width=59.0,
        height=20.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("browse_button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=80.0,
        y=8.0,
        width=59.0,
        height=20.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("browse_button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=13.0,
        y=7.0,
        width=59.0,
        height=20.0
    )
    window.resizable(False, False)
    window.mainloop()
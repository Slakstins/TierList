
from tkinter import Canvas, Tk


class tkWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("584x322")
        self.root.configure(bg = "#FFFFFF")

    def start(self):
        from pages.loginPage.loginPageLegacy import loginPage
        self.canvas = loginPage(self.root)
        self.root.mainloop()    
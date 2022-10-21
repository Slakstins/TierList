from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from pymongo import MongoClient
import redis
import pyorient
# Pages were generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

#orient tips:
#Shouldn't need any classes other than USER for registration/login feature. I already created the USER vertex. Probably don't want to use schema restraints. 
#A vertex is just a class that edges can connect to. A class is equivalent to a mongo collection. Syntactically it is treated as an SQL table
#Insert a new user with the json given as content
# username = "seth123"
# Hash = "aeounth"
# salt = "saneotuh"
# client.command("CREATE VERTEX USER CONTENT {Username: '%s', Hash: '%s', Salt: '%s'}" % (username, Hash, salt))

#Equivalent to the SQL command. JSON attribtutes are treated the same syntactically as columns in SQL. 
# res = client.command("SELECT FROM USER WHERE Username='%s'" % (username))
# print(res)
# print(res[0])
# for k in res:
#     print(k)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

window = Tk()
window.geometry("584x322")
window.configure(bg = "#FFFFFF")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
        text="Password:",
        fill="#000000",
        font=("Inter", 16 * -1)
    )

    canvas.create_text(
        156.0,
        118.0,
        anchor="nw",
        text="Username:",
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

def registerPage(window):
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
        file=relative_to_assets("register_button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: print("button_1 clicked"),
        command=lambda: accountPage(window),
        relief="flat"
    )
    button_1.place(
        x=229.0,
        y=188.0,
        width=127.0,
        height=29.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("register_entry_1.png"))
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
        file=relative_to_assets("register_entry_2.png"))
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
        259.0,
        3.0,
        anchor="nw",
        text="Register",
        fill="#000000",
        font=("Inter", 24 * -1)
    )
    
    window.resizable(False, False)
    window.mainloop()

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
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=229.0,
        y=239.0,
        width=127.0,
        height=32.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("login_button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=229.0,
        y=188.0,
        width=127.0,
        height=29.0
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

def browsePage():
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
        command=lambda: print("button_1 clicked"),
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

def testConnections():
    global mClient, oClient, rClient

    #test mongo
    try:
        mClient = MongoClient("433-11.csse.rose-hulman.edu", 40000)
        print("Connected to Mongo Client")
        #print(mclient.server_info(mon))
    except:
        print("Failed to connect to Mongo Client")

    #test redis
    try:
        rClient = redis.Redis(host="433-10.csse.rose-hulman.edu", port=6379)
        rClient.ping()
        print("Connected to Redis Client")
    except:
        print("Failed to connect to Redis Client")
    
    #test orient
    try:
        oClient = pyorient.OrientDB("433-12.csse.rose-hulman.edu", 2424)
        oClient.connect("root", "ich3aeNg")
        #username and password are both admin by default
        oClient.db_open("TierList", "admin", "admin")
        print("Connected to Orient Client")
    except:
        print("Failed to connect to Orient Client")

    return True

testConnections()
registerPage(window)


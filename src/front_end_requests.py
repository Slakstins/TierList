from pickletools import pybytes
from pymongo import MongoClient
import redis
import pyorient
import redis_queue_commands
import bcrypt

global mClient, oClient, userDB, tierlistDB, mConnected, oConnected
mConnected = False
oConnected = False
#test mongo

connectDBs()

def connectDBs():
    if (not mConnected):
        try:
            mClient = MongoClient("433-11.csse.rose-hulman.edu", 40000)
            print("Connected to Mongo Client")
            dbname = mClient['tierList']
            userDB = dbname["users"]
            tierlistDB = dbname["tierlists"]
            mConnected = True
        except:
            mConnected = False
            print("Failed to connect to Mongo Client")

    #test orient
    if (not oConnected):
        try:
            oClient = pyorient.OrientDB("433-12.csse.rose-hulman.edu", 2424)
            oClient.connect("root", "ich3aeNg")
            oClient.db_open("TierList", "admin", "admin")
            oConnected = True
            print("Connected to Orient Client")
        except:
            oConnected = False
            print("Failed to connect to Orient Client")

def registerUser(window, username, password):
    global currentUser
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    redis_queue_commands.createUser(username, salt, hash)
    currentUser = username
    from browsePage.browsePage import browsePage
    browsePage(window)

def loginUser(window, username, password):
    global currentUser
    userForHash = userDB.find_one({"username": username})
    if(userForHash):
        hash = userForHash["hash"]
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), hash)
        userForValidation = userDB.find_one({"username": username, "hash": hashedPassword})
        if(userForValidation):
            currentUser = username
            from browsePage.browsePage import browsePage
            browsePage(window)
        else:
            print("login invalid")
    else:
        print("login invalid")

def updateUser(window, username, password):
    global currentUser
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    redis_queue_commands.updateUser(currentUser, username, salt, hash)
    currentUser = username
    from accountPage.accountPage import accountPage
    accountPage(window)

def getUsername():
    global currentUser
    return currentUser

def deleteUser(window):
    redis_queue_commands.deleteUser(currentUser)
    from loginPage.loginPage import loginPage
    loginPage(window)

def userExists(username):
    #used in redis_queue_commands.py. Thought it would be good to keep
    #direct db requests outside of that file.
    connectDBs()
    mUser = None
    oUserLi = None
    try:
        mUser = userDB.find_one({"username": username})
    except:
        mConnected = False
    try:
        oUserLi = oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
    except:
        oConnected = False
    #only needs to exist on one DB to be considered existing

    #if not (mConnected or oConnected) prevent action

    return (mUser is not None) or ((oUserLi is not None) and (len(oUserLi) > 0))

def tierListExists(title, username):
    #only needs to exist on one DB to be considered existing
    tids = userDB.find_one({"username": username})["tierlist-ids"]
    mTierList = tierlistDB.find_one({"title": title, "_id": {"$in": tids}})
    oUser = oClient.command("SELECT(SELECT FROM USER WHERE username='%s')" % (username))
    oTierListLi = oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
            % (title, username))
    return (mTierList is not None) or len(oTierListLi) > 0

def createTierList(window, name):
    global currentUser
    redis_queue_commands.createTierList(currentUser, name)
    from browsePage.browsePage import browsePage
    browsePage(window)


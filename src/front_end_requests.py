from pickletools import pybytes
from pymongo import MongoClient
import pyorient
import redis_queue_commands
import bcrypt

global mClient, oClient, userDB, tierlistDB, mConnected, oConnected
mConnected = False
oConnected = False

def tryConnections():
    global mClient, oClient, mConnected, oConnected, userDB, tierlistDB
    #it's okay to have just one connection. Only need to reconnect if current connections fail
    if (oConnected or mConnected):
        print("CONNECTION STABLE")
        return True
    if (not mConnected):
        try:
            mClient = MongoClient("433-11.csse.rose-hulman.edu", 40000, serverSelectionTimeoutMS=1000)
            dbname = mClient['tierList']
            userDB = dbname["users"]
            tierlistDB = dbname["tierlists"]
            mClient.server_info()
            print("Connected to Mongo Client")
            mConnected = True
        except:
            mConnected = False
            print("Failed to connect to Mongo Client")
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
    return oConnected or mConnected

print(" opening windows")
tryConnections()

def registerUser(window, username, password):
    global currentUser, userDB, oClient, oConnected, mConnected
    connected = tryConnections()
    if (not connected):
        print("cannot register user if dbs are down")
        return
    res = userExists(username)
    if (res is None):
        print("Connection down. try again later")
        return
    elif (res is True):
        print("username already in use")
        return
    else:
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        if (redis_queue_commands.createUser(username, salt, hash)):
            currentUser = username
            from browsePage.browsePage import browsePage
            browsePage(window)
        else:
            print("failed to create user. try a different username or try again later")

def loginUser(window, username, password):
    global currentUser, userDB, oClient, oConnected, mConnected

    connected = tryConnections()
    if (not connected):
        print("cannot login user if dbs are down")
        return
    mUser = None
    oUsrArray = None
    found = False
    if (oConnected):
        try:
            oUsrArray = oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
            if (len(oUsrArray) > 0):
                found = True
        except:
            oConnected = False
    elif (mConnected):
        try:
            mUser = userDB.find_one({"username": username})
            if (mUser is not None):
                found = True
        except:
            mConnected = False

    if (not found):
        print("user not found")
        return

    if (mUser is not None):
        userForSalt = mUser
    elif (oUsrArray is not None and len(oUsrArray) > 0) :
        userForSalt = oUsrArray[0]
    else:
        #neither DB is connected
        print("weird case. What do we do?")
        return

    if(userForSalt is not None):
        #ternary operator
        salt = userForSalt.salt if oConnected else userForSalt["salt"]
        hash_ = userForSalt.hash if oConnected else userForSalt["hash"]
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        if(hashedPassword.decode('utf-8') == hash_):
            currentUser = username
            from browsePage.browsePage import browsePage
            browsePage(window)
        else:
            print("incorrect password")
    else:
        print("login invalid")

def updateUser(window, username, password):
    global currentUser
    connected = tryConnections()
    if (not connected):
        print("cannot update user if dbs are down")
        return
    salt = bcrypt.gensalt()
    hash_ = bcrypt.hashpw(password.encode('utf-8'), salt)
    redis_queue_commands.updateUser(currentUser, username, salt, hash_)
    currentUser = username
    from accountPage.accountPage import accountPage
    accountPage(window)

def getUsername():
    global currentUser
    return currentUser

def deleteUser(window):
    connected = tryConnections()
    if (not connected):
        print("db not connected")
        return
    redis_queue_commands.deleteUser(currentUser)
    from loginPage.loginPage import loginPage
    loginPage(window)

def userExists(username):
    global mClient, oClient, mConnected, oConnected
    mUser = None
    oUserLi = None
    print("checking user exists with front end")
    if (oConnected):
        try:
            mUser = userDB.find_one({"username": username})
        except:
            mConnected = False
    if (mConnected):
        try:
            oUserLi = oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
        except:
            oConnected = False
    #only needs to exist on one DB to be considered existing
    if (not (mConnected or oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR USR EXISTS")
        return None
    else:
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


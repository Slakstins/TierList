from pickletools import pybytes
import redis_queue_commands
import front_end_r
import bcrypt
import connections


#initial establishment of connections at runtime
connections.tryConnections()

def registerUser(window, username, password):
    global currentUser, userDB, oClient, oConnected, mConnected
    connected = connections.tryConnections()
    if (not connected):
        print("cannot register user if dbs are down")
        return
    res = front_end_r.userExists(username)
    if (res is None):
        print("Connection down. pushing instruction to queue regardless")
    elif (res is True):
        print("username already in use")
        return
    else:
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        if (redis_queue_commands.createUser(username, salt, hash)):
            #redirect to login page to fix identical username issue
            from loginPage.loginPage import loginPage
            loginPage(window, username, password)
        else:
            print("failed to create user. try a different username or try again later")

def loginUser(window, username, password):
    global currentUser
    connected = connections.tryConnections()
    if (not connected):
        print("cannot login user if dbs are down")
        return
    mUser = None
    oUsrArray = None
    salt = None
    hash_ = None
    if (connections.oConnected):
        try:
            oUsrArray = connections.oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
            if (oUsrArray is not None and len(oUsrArray) > 0):
                salt = oUsrArray[0].salt
                hash_ = oUsrArray[0].hash
        except:
            connections.oConnected = False
    #not an elif in case oConnection fails in except case above
    if (connections.mConnected and not connections.oConnected):
        try:
            mUser = connections.userDB.find_one({"username": username})
            if (mUser is not None):
                salt = mUser["salt"]
                hash_ = mUser["hash"]
        except:
            connections.mConnected = False

    if (not (connections.tryConnections())):
        print("db connection failed. Trying to reconnect...")
        connections.tryConnections()

    if (salt is None):
        print("user not found")
        return
    else:
        hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
        if(hashedPassword.decode('utf-8') == hash_):
            currentUser = username
            from browsePage.browsePage import browsePage
            browsePage(window)
        else:
            print("incorrect password. It is possible another user made an account with your username before you did")

def updateUser(window, username, password):
    global currentUser
    connected = connections.tryConnections()
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
    connected = connections.tryConnections()
    if (not connected):
        print("db not connected")
        return
    redis_queue_commands.deleteUser(currentUser)
    from loginPage.loginPage import loginPage
    loginPage(window)

def createTierList(window, title, t1, l1, t2, l2, t3, l3):
    global currentUser
    connected = connections.tryConnections()
    if (not connected):
        print("db not connected")
        return

    res = front_end_r.tierListExists(currentUser, title)
    if (res is None):
        print("Connection down. pushing instruction to queue regardless")
    elif (res is True):
        print("username already in use")
        return
    else:
        if(redis_queue_commands.createTierList(currentUser, title, l1, t1, l2, t2, l3, t3)):
            from browsePage.browsePage import browsePage
            browsePage(window)
        else:
            print("Failed to create tier list")

def updateTierList(window, oldTitle, newTitle, l1, t1, l2, t2, l3, t3):
    print("oldtitle: " + oldTitle)
    print("newtitle: " + newTitle)
    print("l1: " + l1)
    print("t1: " + t1)
    print("l2: " + l2)
    print("t2: " + t2)
    print("l3: " + l3)
    print("t3: " + t3)
    print("TODO")

def deleteTierList(window, title):
    global currentUser
    connected = connections.tryConnections()
    if (not connected):
        print("db not connected")
        return
    if(redis_queue_commands.deleteTierList(currentUser, title)):
        from browsePage.browsePage import browsePage
        browsePage(window)
    else:
        print("Failed to create tier list")


#probably going to end up replacing this. Our use case will probably require
#to be able to use the mTierList or oTierListLi for calls after this so it
#won't be all that helpful.
# def tierListExists(title, username):
#     #only needs to exist on one DB to be considered existing
#     tids = connections.userDB.find_one({"username": username})["tierlist-ids"]
#     mTierList = connections.tierlistDB.find_one({"title": title, "_id": {"$in": tids}})
#     oUser = connections.oClient.command("SELECT(SELECT FROM USER WHERE username='%s')" % (username))
#     oTierListLi = connections.oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
#             % (title, username))
#     return (mTierList is not None) or len(oTierListLi) > 0


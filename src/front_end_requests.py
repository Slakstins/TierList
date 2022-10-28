from pickletools import pybytes
from pymongo import MongoClient
import redis
import pyorient
import redis_queue_commands
import bcrypt

global mClient, oClient, userDB, tierlistDB
#test mongo
try:
    mClient = MongoClient("433-11.csse.rose-hulman.edu", 40000)
    print("Connected to Mongo Client")
    dbname = mClient['tierList']
    userDB = dbname["users"]
    tierlistDB = dbname["tierlists"]
    #print(mclient.server_info(mon))
except:
    print("Failed to connect to Mongo Client")

#test orient
try:
    oClient = pyorient.OrientDB("433-12.csse.rose-hulman.edu", 2424)
    oClient.connect("root", "ich3aeNg")
    #username and password are both admin by default
    oClient.db_open("TierList", "admin", "admin")
    print("Connected to Orient Client")
except:
    print("Failed to connect to Orient Client")

def registerUser(window, username, password):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    redis_queue_commands.createUser(username, salt, hash)
    from browsePage.browsePage import browsePage
    browsePage(window)

def loginUser(window, username, password):
    global currentUser
    userForHash = userDB.find_one({"username": username})
    hash = userForHash["hash"]
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), hash)
    userForValidation = userDB.find_one({"username": username, "hash": hashedPassword})
    if(userForValidation):
        currentUser = userForValidation["username"]
        from browsePage.browsePage import browsePage
        browsePage(window)
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
    return currentUser

def deleteUser(window):
    redis_queue_commands.deleteUser(currentUser)
    from loginPage.loginPage import loginPage
    loginPage(window)

def userExists(username):
    #used in redis_queue_commands.py. Thought it would be good to keep
    #direct db requests outside of that file.
    mUser = userDB.find_one({"username": username})
    oUserLi = oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
    #only needs to exist on one DB to be considered existing
    return (mUser is not None) or (len(oUserLi) > 0)

def tierListExists(title, username):
    #only needs to exist on one DB to be considered existing
    tids = userDB.find_one({"username": username})["tierlist-ids"]
    mTierList = tierlistDB.find_one({"title": title, "_id": {"$in": tids}})
    oUser = oClient.command("SELECT(SELECT FROM USER WHERE username='%s')" % (username))
    oTierListLi = oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
            % (title, username))
    return (mTierList is not None) or len(oTierListLi) > 0






    

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

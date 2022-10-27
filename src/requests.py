from pymongo import MongoClient
import redis
import pyorient

def testConnections():
    global mClient, oClient, rClient, userDB
    #test mongo
    try:
        mClient = MongoClient("433-11.csse.rose-hulman.edu", 40000)
        print("Connected to Mongo Client")
        dbname = mClient['tierList']
        userDB = dbname["Users"]
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

def registerUser(window, username, password):
    #TODO: fix 
    global currentUser
    document = {
        "Username": username,
        "Password": password,
    }
    userDB.insert_one(document)
    currentUser = username
    from pages.browsePage.browsePage import browsePage
    browsePage(window)
    return

def getUsername():
    return userDB.find_one({"Username": currentUser})["Username"]

def loginUser(window, username, password):
    #TODO: fix 
    global currentUser
    user = userDB.find_one({"Username": username, "Password": password})
    if(user):
        currentUser = user["Username"]
        from pages.browsePage.browsePage import browsePage
        browsePage(window)
    else:
        print("login invalid")


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
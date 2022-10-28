import front_end_requests
import json
import redis
from pymongo import MongoClient
import pyorient
import bcrypt

#test redis
global mClient, oClient, userDB, tierlistDB
try:
    rClient = redis.Redis(host="433-13.csse.rose-hulman.edu", port=6379)
    rClient.ping()
    print("Connected to Redis Client")
except:
    print("Failed to connect to Redis Client")

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

#add to redis queue
def pushToRedisQueue(doc):
    s = json.dumps(doc) + ""
    print(s)
    rClient.lpush("orient", s)
    rClient.lpush("mongo", s)

def createUser(username, salt, _hash):
    global mClient, rClient, currentUser
    if (front_end_requests.userExists(username)):
        return False

    #replace with redis
    #document = {
    #    "username": username,
    #    "salt": salt,
    #    "hash": hash
    #}
    #userDB.insert_one(document)
    #currentUser = username

    redis
    doc = ({
        "instruction": "createUser",
        "username": username,
        "salt": salt.decode("utf-8"),
        "hash": _hash.decode("utf-8")
        })
    json.dumps(doc)
    print(doc)
    
    pushToRedisQueue(doc)
    return True

def deleteUser(username):

    #replace with redis
    #userDB.delete_one({"username": username})

    #redis
    doc = ({
        "instruction": "deleteUser",
        "username": username
        })
    print(doc)

    pushToRedisQueue(doc)
    return True

def updateUser(oldUsername, newUsername, newSalt, newHash):
    global currentUser

    #replace with redis
    #userDB.update_one({"username": oldUsername}, {"$set": {"salt": newSalt}})
    #userDB.update_one({"username": oldUsername}, {"$set": {"hash": newHash}})
    #userDB.update_one({"username": oldUsername}, {"$set": {"username": newUsername}})

    #redis
    doc = ({
        "instruction": "updateUser",
        "oldUsername": oldUsername,
        "newUsername": newUsername,
        "newSalt": newSalt.decode('utf-8'),
        "newHash": newHash.decode('utf-8')
        })
    print(doc)
    pushToRedisQueue(doc)
    currentUser = newUsername

    return True

def createTierList(title, username):
    if (front_end_requests.tierListExists(title, username)):
        return False

    #replace with redis stuff
    #document = {
    #    "title": title,
    #    "username": username,
    #}
    #tierlistDB.insert_one(document)

    #redis
    doc = ({
        "instruction": "createTierList",
        "title": title,
        "username": username
        })
    pushToRedisQueue(doc)
    return True


def updateTierList(oldTitle, newTitle, username, tiers):
    doc = ({
        "instruction": "updateTierList",
        "oldTitle": oldTitle,
        "newTitle": newTitle,
        "username": username,
        "tiers": tiers
        })
    pushToRedisQueue(doc)
    return True


def deleteTierList(username, title):
    doc = ({
        "username": username,
        "title": title
        })
    pushToRedisQueue(doc)
    return True




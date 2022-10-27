import requests
import json

#private to file
def pushToRedisQueue(doc):
    rClient.lpush("orient", json.dumps(doc))
    rClient.lpush("mongo", json.dumps(doc))

def createUser(username, salt, hash_)
    global mClient, rClient
    if (requests.userExists(username)):
        return False
    doc = ({
        "instruction": "updateTierList",
        "username": username,
        "salt": salt,
        "hash": hash_
        })
    pushToRedisQueue(doc)
    return True

def deleteUser(username):
    doc = ({
        "instruction": "deleteUser",
        "username": username
        })
    pushToRedisQueue(doc)
    return True

def updateUser(oldUsername, newUsername, newSalt, newHash)
    doc = ({
        "instruction": "updateUser",
        "oldUsername": oldUsername,
        "newUsername": newUsername,
        "newSalt": newSalt,
        "newHash": newHash
        })
    pushToRedisQueue(doc)
    return True

def createTierList(title, username):
    if (tierListExists(title, username)):
        return False
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




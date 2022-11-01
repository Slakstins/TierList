import front_end_cud
import json
import connections


def pushToRedisQueue(doc):
    s = json.dumps(doc)
    connections.rClient.rpush("orient", s)
    connections.rClient.rpush("mongo", s)

def createUser(username, salt, _hash):
    global rClient, currentUser
    doc = ({
        "instruction": "createUser",
        "username": username,
        "salt": salt.decode("utf-8"),
        "hash": _hash.decode("utf-8")
        })
    print(doc)
    json.dumps(doc)
    pushToRedisQueue(doc)
    return True

def deleteUser(username):
    doc = ({
        "instruction": "deleteUser",
        "username": username
        })
    print(doc)

    pushToRedisQueue(doc)
    return True

def updateUser(oldUsername, newUsername, newSalt, newHash):
    global currentUser
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
    if (front_end_cud.tierListExists(title, username)):
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
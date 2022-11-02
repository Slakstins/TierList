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

def createTierList(currentUser, title, l1, t1, l2, t2, l3, t3):
    t1List = t1.split(',')
    t2List = t2.split(',')
    t3List = t3.split(',')

    doc = ({
        "instruction": "createTierList",
        "title": title,
        "username": currentUser,
        "tiers": [{
            "lable1": [{
                "name": l1,
                "values": t1List
            }],
            "lable2": [{
                "name": l2,
                "values": t2List
            }],
            "lable3": [{
                "name": l3,
                "values": t3List
            }]
        }]
        })

    print(doc)
    #pushToRedisQueue(doc)
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
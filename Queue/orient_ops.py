
import hashlib
import json
import pyorient
import constants
import instructions



#if a db connection fails here, it should throw an exception
def orientCreateUser(inst):
    inst["username"]
    inst["salt"]
    inst["hash"]
    user = ({
        "username": inst["username"],
        "salt": inst["salt"],
        "hash": inst["hash"]
        })
    instructions.oclient.command("CREATE VERTEX USER CONTENT " + json.dumps(user))
    print("orient created user")

#need to delete the user and all of the tier lists they had created
#can use deleteTierList to make this a bit cleaner
def orientDeleteUser(inst):
    inst["username"]

    instructions.oclient.command("DELETE EDGE E WHERE @rid IN (SELECT _in FROM TIERLIST )



    instructions.oclient.command("DELETE VERTEX USER WHERE username=%s" % (inst["username"]))

    print("orient deleted user")

def orientUpdateUser(inst):
    inst["oldUsername"]
    inst["newUsername"]
    inst["newSalt"]
    inst["newHash"]
    print("orient updated user")

def orientCreateTierList(inst):
    inst["title"]
    print("orient created tier list")

def orientUpdateTierList(inst):
    inst["title"]
    inst["username"]
    inst["tiers"]
    print("orient updated tier list")

def orientDeleteTierList(inst):
    inst["username"]
    inst["title"]
    print("orient deleted tier list")



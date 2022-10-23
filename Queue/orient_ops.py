

import pyorient
import constants
import instructions


#if a db connection fails here, it should throw an exception
def orientCreateUser(inst):
    instructions.oclient.command("SELECT * FROM E")
    print("orient created user")

def orientDeleteUser(inst):
    print("orient deleted user")

def orientUpdateUser(inst):
    print("orient updated user")

def orientCreateTierList(inst):
    print("orient created tier list")

def orientUpdateTierList(inst):
    print("orient updated tier list")

def orientDeleteTierList(inst):
    print("orient deleted tier list")



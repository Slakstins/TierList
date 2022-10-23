

import pyorient

oclient = pyorient.OrientDB(ORIENT_VM,ORIENT_PORT)
oclient.connect(ORIENT_USERNAME,ORIENT_PASSWORD)

oclient.db_open(ORIENT_DB_NAME, ORIENT_DB_USERNAME, ORIENT_DB_PASSWORD)

def orientCreateUser(inst):
    print("orient creating user")
    return True

def orientDeleteUser(inst):
    print("orient deleting user")
    return True

def orientUpdateUser(inst):
    print("orient updating user")
    return True

def orientCreateTierList(inst):
    print("orient create tier list")
    return True

def orientUpdateTierList(inst):
    print("orient update tier list")
    return True

def orientDeleteTierList(inst):
    print("orient delete tier list")
    return True




import mongo_ops
import orient_ops
import constants
import pyorient
import pymongo
from pymongo import MongoClient

mongoConnected = False
orientConnected = False
oclient = None
mclient = None

def establishConnections():
    global mongoConnected
    global orientConnected
    global oclient
    global moclient
    if (not mongoConnected):
        try:
            mclient = MongoClient(constants.MONGO_VM, constants.MONGO_PORT)
            mongoConnected = True
        except:
            mongoConnected = False
    if (not orientConnected):
        try:
            oclient = pyorient.OrientDB(constants.ORIENT_VM, constants.ORIENT_PORT)
            oclient.connect(constants.ORIENT_USERNAME, constants.ORIENT_PASSWORD)
            oclient.db_open(constants.ORIENT_DB_NAME, constants.ORIENT_DB_USERNAME, constants.ORIENT_DB_PASSWORD)
            orientConnected = True
        except:
            orientConnected = False

def runInstruction(jsonInst, mongoOrOrient):
    global mongoConnected
    global orientConnected
    global oclient
    global moclient
    establishConnections()
    if (jsonInst is None):
        return False
    #small optimization:
    if ((mongoOrOrient == constants.ORIENT_KEY and not orientConnected) or
            mongoOrOrient == constants.MONGO_KEY and not mongoConnected):
        return False
    inst = jsonInst['instruction']
    success = False
    try:
        if (inst == constants.CREATE_USER):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientCreateUser(inst)
            else:
                mongo_ops.mongoCreateUser(inst)
        elif (inst == constants.DELETE_USER):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientDeleteUser(inst)
            else:
                mongo_ops.mongoDeleteUser(inst)
        elif (inst == constants.UPDATE_USER):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientUpdateUser(inst)
            else:
                mongo_ops.mongoUpdateUser(inst)
        elif (inst == constants.CREATE_TIERLIST):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientCreateTierList(inst)
            else:
                mongo_ops.mongoCreateTierList(inst)
        elif (inst == constants.UPDATE_TIERLIST):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientUpdateTierList(inst)
            else:
                mongo_ops.mongoUpdateTierList(inst)
        elif (inst == constants.DELETE_TIERLIST):
            if (mongoOrOrient == constants.ORIENT_KEY):
                orient_ops.orientDeleteTierList(inst)
            else:
                mongo_ops.mongoDeleteTierList(inst)
        else:
            print("unsupported instruction received")
            #throw an error here
        success = True
    except:
        success = False

    if (not success):
        if (mongoOrOrient == constants.ORIENT_KEY):
            orientConnected = False
        elif (mongoOrOrient == constants.MONGO_KEY):
            mongoConnected = False
    return success




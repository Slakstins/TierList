
import mongo_ops.py
import orient_ops.py
from constants import *

def runInstruction(jsonInst, mongoOrOrient):
    inst = jsonInst['instruction']
    success = False
    if (inst == CREATE_USER):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientCreateUser(inst)
        else:
            success = mongoCreateUser(inst)
    elif (inst == DELETE_USER):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientDeleteUser(inst)
        else:
            success = mongoDeleteUser(inst)
    elif (inst == UPDATE_USER):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientUpdateUser(inst)
        else:
            success = mongoUpdateUser(inst)
    elif (inst == CREATE_TIERLIST):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientCreateTierList(inst)
        else:
            success = mongoCreateTierList(inst)
    elif (inst == UPDATE_TIERLIST):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientUpdateTierList(inst)
        else:
            success = mongoUpdateTierList(inst)
    elif (inst == DELETE_TIERLIST):
        if (mongoOrOrient == ORIENT_KEY):
            success = orientDeleteTierList(inst)
        else:
            success = mongoDeleteTierList(inst)
    else:
        print("unsupported instruction received")
    return success




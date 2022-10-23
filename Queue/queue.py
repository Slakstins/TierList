import json
import redis
from constants import *


r = redis.Redis(host=REDIS_VM, port=REDIS_PORT)
r.ping()




while(True):
    sleep(CLOCK)
    #obtain and parse mongo queue value
    mpeekJSONStringEncoded = r.lindex(MONGO_KEY, 0)
    mpeekJSONStringDecoded = mpeekJSONStringEncoded.decode("utf-8")
    mpeekJSON = json.loads(mpeekJSONStringDecoded)

    #obtain and parse orient queue value
    opeekJSONStringEncoded = r.lindex(ORIENT_KEY, 0)
    opeekJSONStringDecoded = opeekJSONStringEncoded.decode("utf-8")
    opeekJSON = json.loads(opeekJSONStringDecoded)

    #attempt to run the mongo instruction
    mongoSuccess = runMongoInstruction(mpeekJSON)
    #attempt to run redis instruction
    orientSuccess = runOrientInstruction(opeekJSON)

    #pop queues where the instruction ran successfully (db is not down)
    if (orientSuccess):
        r.lpop(ORIENT_KEY)
    if (mongoSuccess):
        r.lpop(MONGO_KEY)
















import pymongo
from pymongo import MongoClient
import redis
import pyorient


#test mongo
mclient = MongoClient("csse@433-11.csse.rose-hulman.edu", 27017)
mclient.server_info()

#test redis
r = redis.Redis(host="csse@433-10.csse.rose-hulman.edu", port=6379)
r.ping()

#test orient
oclient = pyorient.OrientDB("csse@433-10.csse.rose-hulman.edu", 2424)



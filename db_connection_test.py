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
client.connect("root", "ich3aeNg")
#username and password are both admin by default
client.db_open("TierList", "admin", "admin")
username = "seth123"
client.command("SELECT FROM USER WHERE Username=%s" % (username))



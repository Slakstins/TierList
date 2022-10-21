import pymongo
from pymongo import MongoClient
import redis
import pyorient


#test mongo
mclient = MongoClient("433-11.csse.rose-hulman.edu", 40000)
#print(mclient.server_info())

#test redis
r = redis.Redis(host="433-10.csse.rose-hulman.edu", port=6379)
r.ping()

#test orient
client = pyorient.OrientDB("433-12.csse.rose-hulman.edu", 2424)
client.connect("root", "ich3aeNg")
#username and password are both admin by default
client.db_open("TierList", "admin", "admin")


#orient tips:
#Shouldn't need any classes other than USER for registration/login feature. I already created the USER vertex. Probably don't want to use schema restraints. 
#A vertex is just a class that edges can connect to. A class is equivalent to a mongo collection. Syntactically it is treated as an SQL table
#Insert a new user with the json given as content
username = "seth123"
Hash = "aeounth"
salt = "saneotuh"
client.command("CREATE VERTEX USER CONTENT {Username: '%s', Hash: '%s', Salt: '%s'}" % (username, Hash, salt))

#Equivalent to the SQL command. JSON attribtutes are treated the same syntactically as columns in SQL. 
res = client.command("SELECT FROM USER WHERE Username='%s'" % (username))
print(res)
print(res[0])
for k in res:
    print(k)



import connections


def userExists(username):
    mUser = None
    oUserLi = None
    print("checking user exists with front end")
    if (connections.oConnected):
        try:
            mUser = connections.userDB.find_one({"username": username})
        except:
            mConnected = False
    if (mConnected):
        try:
            oUserLi = connections.oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
        except:
            oConnected = False
    #only needs to exist on one DB to be considered existing
    if (not (mConnected or oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR USR EXISTS")
        return None
    else:
        return (mUser is not None) or ((oUserLi is not None) and (len(oUserLi) > 0))
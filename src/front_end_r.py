import connections


def userExists(username):
    mUser = None
    oUserLi = None
    print("checking user exists with front end")
    if (connections.oConnected):
        try:
            mUser = connections.userDB.find_one({"username": username})
        except:
            connections.mConnected = False
    if (connections.mConnected):
        try:
            oUserLi = connections.oClient.command("SELECT FROM USER WHERE username='%s'" % (username))
        except:
            connections.oConnected = False
    #only needs to exist on one DB to be considered existing
    if (not (connections.mConnected or connections.oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR USR EXISTS")
        return None
    else:
        return (mUser is not None) or ((oUserLi is not None) and (len(oUserLi) > 0))

def tierListExists(username, title):
    mList = None
    oList = None
    print("checking tier list exists with front end")
    if(connections.oConnected):
        try:
            mList = connections.tierlistDB.find_one({"username": username, "title": title})
        except:
            connections.mConnected = False
    if(connections.mConnected):
        try:
            oList = connections.oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
            % (title, username))
        except:
            connections.oConnected = False
    if (not (connections.mConnected or connections.oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR TIERLIST EXISTS")
        return None
    else:
        return (mList is not None) or ((oList is not None) and (len(oList) > 0))
    
def getTierLists(username):
    mList = None
    oList = None
    if(connections.oConnected):
        try:
            mList = connections.tierlistDB.find({"username": username})
        except:
            connections.mConnected = False
    if(connections.mConnected):
        try:
            oList = connections.oClient.command("SELECT FROM TIERLIST WHERE in.out[@Class = 'USER'].username = '%s'"
            % (username))
        except:
            connections.oConnected = False
    if (not (connections.mConnected or connections.oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR TIERLIST EXISTS")
        return None
    else:
        if(mList):
            return mList
        elif(oList):
            return oList
        else:
            return []


    #only needs to exist on one DB to be considered existing
    # tids = connections.userDB.find_one({"username": username})["tierlist-ids"]
    # mTierList = connections.tierlistDB.find_one({"title": title, "_id": {"$in": tids}})
    # oUser = connections.oClient.command("SELECT(SELECT FROM USER WHERE username='%s')" % (username))
    # oTierListLi = connections.oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
    #         % (title, username))
    # return (mTierList is not None) or len(oTierListLi) > 0
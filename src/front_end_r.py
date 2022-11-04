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
    mTierLists = None
    oTierLists = None
    # if(connections.oConnected):
    #     try:
    #         oTierLists = connections.oClient.command("SELECT FROM TIERLIST WHERE in.out[@Class = 'USER'].username = '%s'"
    #         % (username))
    #     except:
    #         connections.oConnected = False
    #if(connections.mConnected and not connections.oConnected):
    try:
        mUserLists = connections.userDB.find({"username": username})
        tids = mUserLists[0]['tierlist-ids']
        mTierLists = []
        for curId in tids:
            print(curId)
            tl = connections.tierlistDB.find({"_id": curId})[0]
            mTierLists.append(tl)
    except:
        connections.mConnected = False
    
    if (not (connections.mConnected or connections.oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR TIERLIST EXISTS")
        return None
    else:
        if(oTierLists):
            return oTierLists
        elif(mTierLists):
            return mTierLists
        else:
            return []

def getTierListByTitle(username,title):
    mTierList = None
    oTierList = None
    # if(connections.oConnected):
    #     try:
    #         oTierList = connections.oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
    #         % (username))
    #     except:
    #         connections.oConnected = False
    #if(connections.mConnected and not connections.oConnected):
    try:
        mUserList = connections.userDB.find({"username": username})
        tids = mUserList[0]['tierlist-ids']
        mTierList = []
        for curId in tids:
            tl = connections.tierlistDB.find({"_id": curId})[0]
            mTierList = tl
    except:
        connections.mConnected = False
    if (not (connections.mConnected or connections.oConnected)):
        #returns None if dbs are no longer connected
        print("NO CONNECTION FOR TIERLIST EXISTS")
        return None
    else:
        if(oTierList):
            return oTierList
        elif(mTierList):
            return mTierList
        else:
            return []


    #only needs to exist on one DB to be considered existing
    # tids = connections.userDB.find_one({"username": username})["tierlist-ids"]
    # mTierList = connections.tierlistDB.find_one({"title": title, "_id": {"$in": tids}})
    # oUser = connections.oClient.command("SELECT(SELECT FROM USER WHERE username='%s')" % (username))
    # oTierListLi = connections.oClient.command("SELECT FROM TIERLIST WHERE title='%s' AND in.out[@Class = 'USER'].username = '%s'"
    #         % (title, username))
    # return (mTierList is not None) or len(oTierListLi) > 0
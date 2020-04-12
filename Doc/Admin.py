import pymongo

class Admin:
    def __init__(self, Username = None):
        Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = Myclient["databaselaptop"]
        self.Mycoladmin = mydb ["Admin"]
        if Username :
            self.Username = Username

    def getUsername(self):
        return self.Username

    def getData(self):
        return self.Mycoladmin.find_one({"Username" : self.Username})

    def addAdmin(self, Username, Password, Nama):
        ListAdmin = {"Username" : Username, "Password" : Password, "Nama" : Nama}
        return self.Mycoladmin.insert_one(ListAdmin)

    def getAdmin(self, Username):
        find = self.Mycoladmin.find_one({"Username" : int(Username)})
        if find == None:
            return None
        return find['Username']

    def setAdmin(self, Username):
        newid = { "$set": { "Username" : Username } }
        return self.Mycoladmin.update_one({"Username":self.Username})

    def getPassword(self):
        getpass = self.Mycoladmin.find_one({'Username':self.Username})
        if getpass == None:
            return None
        return getpass['Password']
    
    def setPassword(self, newpass):
        toid = {"Username": self.Username}
        setnewpass = {"$set" : {"Password": newpass}}
        return self.Mycoladmin.update_one(toid, setnewpass)

    def getName(self):
        getname = self.Mycoladmin.find_one({"Username": self.Username})
        if getname == None:
            return None
        return getname['Nama']
    
    def setName(self, newname):
        toid = { "Username": self.Username}
        setnewname = {"$set": {"Nama": newname}}
        return self.Mycoladmin.update_one(toid, setnewname)

    def getallAdmin(self):
        ListAdmin = []
        for x in self.Mycoladmin.find({},{"Password" : 0}):
            ListAdmin.append(x)
        return ListAdmin

if __name__ == "__main__":
    model = Admin()
    model.getAdmin("111")
    print(model.getallAdmin())

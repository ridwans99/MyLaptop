import pymongo

class Customers:
    def __init__(self, Username = None):
        Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = Myclient["databaselaptop"]
        self.Mycolcustomers = mydb ["Customers"]
        if Username :
            self.Username = Username

    def showAll(self):
        arr = []
        for x in self.Mycolcustomers.find():
            arr.append(x)
        return arr

    def getUsername(self):
        return self.Username

    def getData(self):
        return self.Mycolcustomers.find_one({'Username':self.Username})

    def addCustomers(self, Username, Password, Nama, Email, Alamat, no_hp):
        ListCustomers = {"Username" : Username, "Password" : Password, "Nama" : Nama, "Email": Email, "Alamat" : Alamat, "no_hp" : no_hp}
        return self.Mycolcustomers.insert_one(ListCustomers)

    def getCustomers(self, Username):
        find = self.Mycolcustomers.find_one({"Username" : int(Username)})
        if find == None:
            return None
        return find['Username']
    
    def setCustomers(self, Username):
        newid = { "$set": { "Username" : Username } }
        return self.Mycolcustomers.update_one({"Username":self.Username})

    def getPassword(self):
        getpass = self.Mycolcustomers.find_one({'Username':self.Username})
        if getpass == None:
            return None
        return getpass['Password']
    
    def setPassword(self, newpass):
        toid = {"Username": self.Username}
        setnewpass = {"$set" : {"Password": newpass}}
        return self.Mycolcustomers.update_one(toid, setnewpass)

    def getName(self):
        getname = self.Mycolcustomers.find_one({"Username": self.Username})
        if getname == None:
            return None
        return getname['Nama']
    
    def setName(self, newname):
        toid = { "Username": self.Username}
        setnewname = {"$set": {"Nama": newname}}
        return self.Mycolcustomers.update_one(toid, setnewname)

    def getEmail(self):
        getemail = self.Mycolcustomers.find_one({"Username": self.Username})
        if getemail == None:
            return None
        return getemail['Email']

    def setEmail(self, newemail):
        toid = { "Username": self.Username}
        setnewemail = {"$set": {"Email": newemail}}
        return self.Mycolcustomers.update_one(toid, setnewemail)

    def getAlamat(self):
        getalamat = self.Mycolcustomers.find_one({"Username": self.Username})
        if getalamat == None:
            return None
        return getalamat['Alamat']

    def setAlamat(self, newalamat):
        toid = { "Username": self.Username}
        setnewalamat = {"$set": {"Alamat": newalamat}}
        return self.Mycolcustomers.update_one(toid, setnewalamat)

    def getno_hp(self):
        getno_hp = self.Mycolcustomers.find_one({"Username": int(Username)})
        if getno_hp == None:
            return None
        return getno_hp['no_hp']

    def setno_hp(self, newno_hp):
        toid = { "Username": self.Username}
        setnewno_hp = {"$set": {"no_hp": newno_hp}}
        return self.Mycolcustomers.update_one(toid, setnewno_hp)
    
    def getallCustomers(self):
        ListCustomers = []
        for x in self.Mycolcustomers.find({},{"Password" : 0}):
            ListCustomers.append(x)
        return ListCustomers

if __name__ == "__main__":
    model = Customers()
    model.getCustomers("11111")
    print(model.getallCustomers())

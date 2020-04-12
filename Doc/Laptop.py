import pymongo

class Laptop:
    def __init__(self, idLaptop = None):
        Myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = Myclient["databaselaptop"]
        self.Mycollaptop = mydb["Laptop"]
        if idLaptop :
            self.idLaptop = idLaptop

    def getidLaptop(self,idLaptop):
        cariid = self.Mycollaptop.find_one({"_id" : idLaptop}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if cariid == None:
            return None
        return cariid['_id']
    
    def getMerkLaptop(self,MerkLaptop):
        cariMerk = self.Mycollaptop.find_one({"Merk Laptop" : MerkLaptop}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if cariMerk == None:
            return None
        return cariMerk['Merk Laptop']

    def getTahunKeluaran(self,TahunKeluaran):
        cariTahun = self.Mycollaptop.find_one({"Tahun Keluaran" : TahunKeluaran}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if cariTahun == None:
            return None
        return cariTahun['Tahun Keluaran']

    def getRAM(self,RAM):
        cariram = self.Mycollaptop.find_one({"RAM" : RAM}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if cariram == None:
            return None
        return cariram ['RAM']

    def getHDD(self,HDD):
        carihdd = self.Mycollaptop.find_one({"HDD" : HDD}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if carihdd == None:
            return None
        return carihdd ['HDD']
    
    def getHarga(self,Harga):
        cariharga = self.Mycollaptop.find_one({"Harga" : Harga}, {"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1})
        if cariharga == None:
            return None
        return cariharga['Harga']

    def addLaptop(self,idLaptop,Merk,Tahun,RAM,HDD,Harga):
        ListLaptop = {"_id" : idLaptop, "Merk Laptop" : Merk, "Tahun Keluaran": Tahun, "RAM" : RAM, "HDD" : HDD, "Harga" : Harga}
        return self.Mycollaptop.insert_one(ListLaptop)

    def getallLaptop(self):
        ListLaptop = []
        for x in self.Mycollaptop.find({},{"_id" : 0, "Merk Laptop": 1, "Tahun Keluaran": 1, "RAM" : 1, "HDD" : 1, "Harga" : 1}):
           ListLaptop.append(x)
        return ListLaptop
    

    
if __name__ == "__main__":
    model = Laptop()
    model.getMerkLaptop("Asus")
    print(model.getallLaptop())




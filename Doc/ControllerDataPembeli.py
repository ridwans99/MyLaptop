from Customers import Customers
from Laptop import Laptop
from Admin import Admin

class ControlDataPembeli:

    def __init__(self, username):
        self.customers = Customers(username)
        self.laptop = Laptop()

    def showAllCustomers(self):
        return self.Customers.showAll()
    
    def showTableData(self):
        data = []
        allcustomers = self.showAllCustomers()
        for i in allcustomers:
            ListCustomers = {}
            for key, value in i.items():
                if key == "_id":
                    continue
                elif key == "id_Laptop":
                    id_Laptop = value
                    l = Laptop(id_Laptop)
                    ListData['_id'] = l.getidLaptop()
                    ListData['Nama'] = l.getName()
                    ListData['Email'] = l.Email()
                    ListData['Alamat'] = l.getAlamat()
                    ListData['no_hp'] = l.getno_hp()
                else:
                    ListData[key] = value
            data.append(ListData)
        return data

    def getName(self):
        return self.Customers.getName()

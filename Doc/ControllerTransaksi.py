from Customers import Customers
from Laptop import Laptop

class ControlTransaksi:
    def __init__ (self):
        pass

    def addidLaptop(self, idLaptop, Merk, Tahun, RAM, HDD, Harga):
        return self.idLaptop.add(idLaptop, Merk, Tahun, RAM, HDD, Harga)

    def cariidLaptop(self, idLaptop):
        return self.Laptop.getidLaptop(idLaptop)

    def addCustomers(self, Username, Password, Nama, Email, Alamat, no_hp):
        return self.Customers.Username.add(Username, Password, Nama, Email, Alamat, no_hp)

    def cariNama(self,Nama):
        return self.Customers.getName(Nama)

    def cariEmail(self,Email):
        return self.Customers.getEmail(Email)

    def cariAlamat(self,Alamat):
        return self.Customers.getAlamat(Alamat)

    def carino_hp(self,no_hp):
        return self.Customers.getno_hp(no_hp)

    def beliLaptop (self, idLaptop):
        laptop = Laptop()
        return laptop.getLaptop(Merk)

    def semuaCustomers(self):
        customers = Customers
        return customers.getallCustomers()

from Customers import Customers
from Laptop import Laptop

class ControlPencarianLaptop:
    def __init__ (self):
        pass

    def addidLaptop(self, idLaptop, Merk, Tahun, RAM, HDD, Harga):
        return self.idLaptop.add(idLaptop, Merk, Tahun, RAM, HDD, Harga)

    def cariidLaptop(self, idLaptop):
        return self.Laptop.getidLaptop(idLaptop)

    def cariMerkLaptop(self, MerkLaptop):
        return self.Laptop.getMerkLaptop(MerkLaptop)

    def cariTahunKeluaran(self,TahunKeluaran):
        return self.Laptop.getTahunKeluaran(TahunKeluaran)

    def cariRAM(self,RAM):
        return self.Laptop.getRAM(RAM)

    def cariHDD(self,HDD):
        return self.Laptop.getHDD(HDD)

    def cariHarga(self,Harga):
        return self.Laptop.getHarga(Harga)

    def pesanLaptop (self, Merk):
        laptop = Laptop()
        return laptop.getLaptop(Merk)

    def semuaLaptop(self):
        laptop = Laptop
        return laptop.getallLaptop()

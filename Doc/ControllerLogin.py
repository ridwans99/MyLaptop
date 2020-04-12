import pymongo

from Customers import Customers
from Admin import Admin

class ControlLogin:
    def __init__ (self):
        pass

    def cekLoginCustomers(self,Username,Password):
        user = Username(int(username))
        if user.getPassword() == password:
            return True
        return False

    def cekLoginAdmin(self,Username,Password):
        admin = Admin(int(Username))
        if admin.getPassword() == password:
            return True
        return False

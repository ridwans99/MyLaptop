from Customers import Customers

class ControlCustomers:
    def __init__(self, Username, Password):
        self.username = Username
        self.password = Password

    def cekLoginCutomers (self, Username, Password):
        Cus = Customers(self.Username)
        Password = Cus.getPassword()
        if self.Password() == Password:
            return True
        return False

    

        

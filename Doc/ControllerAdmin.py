from Admin import Admin

class ControllerAdmin:
    def __init__ (self, Username, Password):
        self.username = Username
        self.password = Password
        
    def cekLoginAdmin (self, Username, Password):
        Ad = Admin(self.Username)
        Password = Ad.getPassword()
        if self.password() == Password:
            return True
        return False

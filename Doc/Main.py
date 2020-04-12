from TampilanLoginView import TampilanLogin_Window
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Main:
    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        ui = TampilanLogin_Window()
        sys.exit(app.exec_())

        

if __name__ == "__main__":
    startapp = Main()
    startapp.run()

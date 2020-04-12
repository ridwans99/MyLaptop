from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from LoginCustomersView import LoginCustomers_Window
from LoginAdminView import LoginAdmin_Window

class TampilanLogin_Window(object):
    def __init__ (self):
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 310, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 100, 431, 61))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TampilanLogin"))
        self.pushButton.setText(_translate("MainWindow", "Login sebagai customers"))
        self.pushButton_2.setText(_translate("MainWindow", "Login sebagai admin"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#0000ff;\">Welcome to MyLaptop</span></p></body></html>"))
        self.pushButton.clicked.connect(lambda: self.pushLoginCustomersView(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.pushLoginAdminView(MainWindow))

    def pushLoginCustomersView(self, MainWindow):
            self.logincustomers = LoginCustomers_Window()
            MainWindow.close()

    def pushLoginAdminView(self, MainWindow):
            self.loginadmin = LoginAdmin_Window()
            MainWindow.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TampilanLogin_Window()
    sys.exit(app.exec_())

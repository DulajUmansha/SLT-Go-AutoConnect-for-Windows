# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from __Interface__.ui_mainwindow import Ui_MainWindow as mainWindowUI
from __Interface__.rc_resource import *
from logic import SLTLogin,WiFiLogin
import threading
import time

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.mainWindow = mainWindowUI()
        self.wifiLogin = WiFiLogin()
        self.stop = False
        self.mainWindow.setupUi(self)

    def buttonClick(self):
        self.mainWindow.connectBtn.clicked.connect(self.connectBtn)
        self.mainWindow.disconnectBtn.clicked.connect(self.disconnectBtn)
        self.mainWindow.profileBtn.clicked.connect(lambda:self.mainWindow.stackedWidget.setCurrentIndex(5))
        self.mainWindow.homeBtn.clicked.connect(lambda:self.mainWindow.stackedWidget.setCurrentIndex(4))
        self.mainWindow.saveBtn.clicked.connect(self.saveCredential)

    def connectBtn(self,tryCount=0)->None:
        self.mainWindow.connectBtn.setEnabled(False)
        self.sltLogin = SLTLogin()
        if (SSID for SSID in self.wifiLogin.discoverWifi() if SSID =="sltgo"):
            try:
                self.wifiLogin.connectToSLTGo()
                if self.wifiLogin.checkInternet()==True:
                    self.mainWindow.connectBtn.setEnabled(True)
                    return
                time.sleep(1)
                self.sltLogin.openNewLink()
            except:
                pass
            
            while tryCount<=3:
                tryCount+=1
                try:
                    self.sltLogin.enterCreditnals()
                    self.sltLogin.clickLogin()
                except:
                    pass
                if self.wifiLogin.checkInternet()==True:
                    break
                time.sleep(1)
        self.mainWindow.connectBtn.setEnabled(True)
            

    def disconnectBtn(self):
        self.stop = True
        self.sltLogin.clickLogoff()
        self.wifiLogin.disconnectFromSLTGo()

    def checkPeroidInternetConn(self):
        while True:
            if(self.stop == True):
                self.stop = False
                break
            elif (self.wifiLogin.checkInternet() == False):
                time.sleep(1)
                self.connectBtn()
            else:
                time.sleep(5)
                
    def closeEvent(self, event) -> None:
        self.stop = True
        return super().closeEvent(event)

    def saveCredential(self):
        userName = self.mainWindow.lineEdit_userName.text()
        password = self.mainWindow.lineEdit_password.text()

        file = open('credentials.txt','w')
        file.write(userName+'\n')
        file.write(password+'\n')
        file.close()

        self.mainWindow.stackedWidget.setCurrentIndex(4)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.buttonClick()
    window.show()
    t2 = threading.Thread(target=window.checkPeroidInternetConn, args = ())
    t2.start()
    sys.exit(app.exec())

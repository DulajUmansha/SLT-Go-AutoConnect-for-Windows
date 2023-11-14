import getpass
import socket
import subprocess
import time
import requests
from webDriver import Divers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

class WiFiLogin():
   def __init__(self):
      pass

   def checkInternet(self,url = "https://www.google.com"):
      timeout = 10
      try:
         request = requests.get(url,timeout=timeout)
         return(True)
      except (requests.ConnectionError,requests.Timeout) as exception:
         return(False)

   def discoverWifi(self):
      networks=[]
      scan_results = subprocess.check_output(["netsh", "wlan", "show", "network"]).decode("ascii").replace("\r","").split("\n")[4:]
      if len(scan_results)>0:
            for eachItem in scan_results:
               if eachItem[0:4] == "SSID":
                  SSID_cleared = eachItem[eachItem.find(":")+2:]
                  networks.append(SSID_cleared)
      return(networks)

   def connectToSLTGo(self):
      # netsh wlan connect ssid=sltgo name=sltgo
      subprocess.call(["netsh","wlan","connect","ssid=sltgo","name=sltgo"])

   def disconnectFromSLTGo(self):
      # netsh wlan disconnect interface='wi-fi'
      subprocess.call(["netsh","wlan","disconnect","interface=wi-fi"])

   def setCreditnals(self):
      pass

class SLTLogin():
   def __init__(self):
      driver = Divers()
      chrome_options = Options()
      try:
         chrome_options.add_argument("--user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(getpass.getuser()))
         chrome_options.add_argument('--profile-directory=Profile 1')
         self.driver = webdriver.Chrome(options=chrome_options)
      except:
         self.driver = driver.choose()

   def openNewLink(self,link="http://www.msftconnecttest.com/redirect"):
      self.driver.get(link)
      while True:
         time.sleep(1)
         if (self.driver.current_url==link):
            self.driver.refresh()
         else:
            break
      
   def enterCreditnals(self):
      file = open('credentials.txt','r')
      data = file.read()
      print(data[0])
      try:
         btniID = "acceptButton"
         cookiesBtn = self.driver.find_element(By.CLASS_NAME,value=btniID)
         cookiesBtn.click()
      except:pass

      btniID = "userFake"
      sltUsername = self.driver.find_element(By.ID,value=btniID)
      sltUsername.send_keys(data[0])

      btniID = "password"
      sltpassword = self.driver.find_element(By.ID,value=btniID)
      sltpassword.send_keys(data[1])

   def clickLogin(self):
      btniID = "login"
      sltLogBtn = self.driver.find_element(By.ID,value=btniID)
      sltLogBtn.click()

   def closeWebbrowser(self):
      self.driver.close()


import subprocess
import time
import requests
from webDriver import Divers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
      data = file.read().split("\n")
      try:
         btniID = "acceptButton"
         cookiesBtn = self.driver.find_element(By.CLASS_NAME,value=btniID)
         cookiesBtn.click()
      except:pass

      btniID = "userFake"
      sltUsername = self.driver.find_element(By.ID,value=btniID)
      sltUsername.send_keys(data[0].strip())

      btniID = "password"
      sltpassword = self.driver.find_element(By.ID,value=btniID)
      sltpassword.clear()
      sltpassword.send_keys(data[1].strip())

      # f = WebDriverWait(self.driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'error')))
      # s = WebDriverWait(self.driver).until(EC.presence_of_element_located((By.CLASS_NAME, 'success')))


   def clickLogin(self):
      btniID = "login"
      sltLogBtn = self.driver.find_element(By.ID,value=btniID)
      sltLogBtn.click()

   def clickLogoff(self):
      self.driver.find_element(By.CLASS_NAME,value='logoffButton').click()
     
   def closeWebbrowser(self):
      self.driver.close()


from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
import getpass

class Divers:
    def __init__(self) -> None:
        pass
        
    def choose(self):
        browser_options = Options()
        browser_options.add_argument('headless')
        try:
            return (webdriver.Chrome(browser_options))
        except selenium.common.NoSuchDriverException:
            return (webdriver.Edge())
        except selenium.common.NoSuchDriverException:
            return (webdriver.Firefox())
        except selenium.common.NoSuchDriverException:
            return (webdriver.Safari())
        except:
            return(None)
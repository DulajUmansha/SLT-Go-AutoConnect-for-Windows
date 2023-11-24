from selenium import webdriver
import selenium


class Divers:
    def __init__(self) -> None:
        pass

    def choose(self):
        try:
            from selenium.webdriver.chrome.options import Options
            browser_options = Options()
            # browser_options.add_argument("headless")
            return webdriver.Chrome(browser_options)
        
        except selenium.common.NoSuchDriverException:
            from selenium.webdriver.edge.options import Options
            browser_options = Options()
            # browser_options.add_argument("headless")
            return webdriver.Edge(browser_options)
        
        except selenium.common.NoSuchDriverException:
            from selenium.webdriver.firefox.options import Options
            browser_options = Options()
            # browser_options.add_argument("headless")
            return webdriver.Firefox(browser_options)
        
        except selenium.common.NoSuchDriverException:
            from selenium.webdriver.safari.options import Options
            browser_options = Options()
            # browser_options.add_argument("headless")
            return webdriver.Safari(browser_options)
        
        except:
            return None

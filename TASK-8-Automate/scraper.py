#    ___| _)             |          |                   _)        |   _)             
#   |      |   __|  __|  |   _ \    |       _ \    _` |  |   __|  __|  |   __|   __| 
#   |      |  |    (     |   __/    |      (   |  (   |  | \__ \  |    |  (    \__ \ 
#  \____| _| _|   \___| _| \___|   _____| \___/  \__, | _| ____/ \__| _| \___| ____/ 
#                                                |___/                               
#  
#  AUTHOR: 
#  NOTES: 
#         
#         
#     

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Scraper():
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        s = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=s,options=chrome_options)
        self.browser.maximize_window()
        self.browser.get(start)

    #Do not touch
    def screenshot_error(self, error):
        self.browser.save_screenshot('error_screenshot/' + error.__class__.__name__ + '_' + str(time.time()) + '.png')

    #Come up with your own functions, there should be atleast two
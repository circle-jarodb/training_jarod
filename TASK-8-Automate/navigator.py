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

class Navigator():
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

    #This function should navigate to the pricing page
    def navigate(self):
        #PUT YOUR CODE HERE
        pass
    
    #This function should click all the check boxes and also the buy now button
    def  click_em_all(self):
        #PUT YOUR CODE HERE
        pass

    #This function should fill in the form and lie to it as well
    def fill_form(self):
        #PUT YOUR CODE HERE
        pass
from selenium.webdriver.common.by import By
from selenium.webdriver import *





class HomePage:

    def __init__(self,driver):
        self.driver = driver

    menuBtn = (By.CSS_SELECTOR,"a[data-qa-id='login-select']")
    loginBtn = (By.CSS_SELECTOR,"a[data-qa-id='login-hudl']")
    RequestBtn = (By.XPATH,"//a[@id='homepage-cta_button']")
    footer = (By.XPATH,"//footer[@class='site-footer']")

    def getMenuBtn(self):
        return self.driver.find_element(*HomePage.menuBtn)
    
    def getloginBtn(self):
        return self.driver.find_element(*HomePage.loginBtn)
    
    def getRequestBtn(self):
        return self.driver.find_element(*HomePage.RequestBtn)
    
    def getfooter(self):
        return self.driver.find_element(*HomePage.footer)


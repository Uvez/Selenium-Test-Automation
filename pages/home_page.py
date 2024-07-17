from selenium.webdriver.common.by import By
from selenium.webdriver import *
from pages.base_page import BasePage
from utilities.log import log




class HomePage(BasePage,log):

    def __init__(self,driver):
        super().__init__(driver)

    menuBtn = (By.CSS_SELECTOR,"a[data-qa-id='login-select']")
    loginBtn = (By.CSS_SELECTOR,"a[data-qa-id='login-hudl']")
    RequestBtn = (By.XPATH,"//a[@id='homepage-cta_button']")
    footer = (By.XPATH,"//footer[@class='site-footer']")


    def click_on_Menu_Button(self):
        self.click(self.menuBtn)
        self.getLogger().info('click on the menu button in the home page')
    

    def click_on_Login_Button(self):
        self.click(self.loginBtn)
        self.getLogger().info('click on the login button')
    
    def click_on_Request_Button(self):
        self.click(self.RequestBtn)
        self.getLogger().info('click on the request button in the home page')
    
    def verify_footer(self):
        self.getLogger().info('verify footer message in the home page')
        return self.getText(self.footer)


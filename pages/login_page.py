from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utilities.log import log


class LoginPage(BasePage,log):

    def __init__(self, driver):
        super().__init__(driver)
 

    email = (By.XPATH, "//input[@id='email']")
    password = (By.XPATH, "//input[@id='password']")
    continueBtn = (By.XPATH, "//button[@id='logIn']")
    requiredtext = (By.XPATH,"//p[normalize-space()='Please fill in all of the required fields']")
    errortext = (By.XPATH,"//p[@class='error-message uni-text uni-text--small uni-text--set-solid'][1]")
    home_button = (By.XPATH,"//span[@id='nav-btn-logo-hudl']//*[name()='svg']//*[name()='path'][1]")
    

    def enter_Email(self,emailvalue):
        self.sendKeys(self.email,emailvalue)
        self.getLogger().info('Entered email address in the login page')
            


    def enter_Password(self,passwordvalue):
        self.sendKeys(self.password,passwordvalue)
        self.getLogger().info('Entered password in the login page')

    def click_on_Continue_Button(self):
        self.click(self.continueBtn)
        self.getLogger().info('click on the Continue button')
    
    def verify_Login_text(self):
        self.getLogger().info('verify login text in the login page')
        return self.getText(self.requiredtext)
    
    def verify_error_text(self):
        self.getLogger().info('verify error text in the login page')
        return self.getText(self.errortext)
    
    def click_on_Home_button(self):
        self.click(self.home_button)
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from pages.base_page import BasePage
from utilities.log import log


class ForgotPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    forgotLink = (By.XPATH,"//a[@id='forgot-password']")
    PageTitle = (By.XPATH,"//h2[normalize-space()='Forgot Password']")
    EmailText = (By.XPATH,"//input[@id='email-reset']")
    ContineBtn = (By.XPATH,"//button[@id='btn-reset']")
    SuccessText = (By.XPATH,"//h2[@class='headline uni-headline--2 page-title']")
    confirmationText = (By.XPATH,"//p[@id='reset-confirmation-hudl-message']")
    LoginBtn = (By.XPATH,"//button[@id='nav-btn-page'] ")
    invalid_email_error = (By.XPATH,"//p[normalize-space()='Please enter a valid email address']")

    def click_on_forgot_link(self):
        self.click(self.forgotLink)
        self.getLogger().info('click on the forgot link')
    
    def verify_page_title(self):
        self.getLogger().info('verify the page title in the forgot page')
        return self.getText(self.PageTitle)

    def enter_Email_ID(self,emailvalue):
        self.sendKeys(self.EmailText,emailvalue)
        self.getLogger().info('enter the email address in the forgot page')
    
    def click_on_Continue_button(self):
        self.click(self.ContineBtn)
        self.getLogger().info('click on the continue button')
    
    def verify_text_message(self):
        self.getLogger().info('verify the text message in the forgot page')
        return self.getText(self.SuccessText)
    
    def verify_confirm_message(self):
        self.getLogger().info('verify the confirmation message in the forgot page')
        return self.getText(self.confirmationText)
    
    def click_to_login_button(self):
        self.click(self.LoginBtn)
        self.getLogger().info('click on the login button')

    def verify_invalid_email_message(self):
        self.getLogger().info('verify the invalid email message')
        return self.getText(self.invalid_email_error)
    


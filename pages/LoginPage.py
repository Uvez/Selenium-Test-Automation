from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id='email']")
    password = (By.XPATH, "//input[@id='password']")
    continueBtn = (By.XPATH, "//button[@id='logIn']")

    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getcontinueBtn(self):
        return self.driver.find_element(*LoginPage.continueBtn)
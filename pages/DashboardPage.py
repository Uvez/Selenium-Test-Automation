from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

class DashBoardPage:

    def __init__(self,driver):
        self.driver = driver

    menuTitle = (By.XPATH,"//div[@class='hui-globaluseritem__display-name']//span")

    
    def getMenuText(self):
        return self.driver.find_element(*DashBoardPage.menuTitle)
    
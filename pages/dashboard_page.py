from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import *
from pages.base_page import BasePage
from utilities.log import log

class DashBoardPage(BasePage,log):

    def __init__(self,driver):
        super().__init__(driver)

    nametext = (By.XPATH,"//div[@class='hui-globaluseritem__display-name']")
    menuText = (By.XPATH,"(//span[contains(text(),'Newcastle Jets FC')])[1]")
    #menuHead = (By.XPATH,"//div[@id='explore-header']")
    logoutBtn = (By.XPATH,"//div[@class='hui-globaladditionalitems hui-globaladditionalitems--not-phone']//a[@class='hui-globalusermenu__item']")
    
    def click_on_name_text(self):
        self.click(self.nametext)
        self.getLogger().info('Click on the Menu text in the dashboard page')

    def verify_menu_text(self):
        self.getLogger().info('Verify the Menu text in the dashboard page')
        return self.getText(self.menuText)
    
    def click_on_Logout_button(self):
        self.click(self.logoutBtn)
        self.getLogger().info('Click on the logout button in the menubar')
        
         
    
    
    
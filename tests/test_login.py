import pytest
import base64
from actions.Actions import Actions
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashBoardPage
from tests.test_base import BaseTest
from assertpy import assert_that

from utilities.log import log

class Test_login(BaseTest,log):

    def test_login(self):
        #log = self.getlog()
        username = self.config_reader.config_section_dict("AUT")["username"]
        #password = base64.b64decode(self.config_reader.config_section_dict("AUT")["password"])
        password = self.config_reader.config_section_dict("AUT")["password"]
        Home = HomePage(self.driver)
        login = LoginPage(self.driver)
        DashBoard = DashBoardPage(self.driver)
        actions = Actions(self.driver)

        actions.click(Home.getMenuBtn())
        #log.info()
        #log.info("Clicked on Menu Button")
        actions.click(Home.getloginBtn())
        actions.sendKeys(login.getEmail(),username)
        actions.sendKeys(login.getPassword(),password)
        actions.click(login.getcontinueBtn())
        #actions.click(DashBoard.getMenuText())
        expected_success_message = self.json_reader.read_from_json()["validateMessage"]["Dashboardtext"]
        #assert_that(expected_success_message).is_equal_to(actions.getText(DashBoard.getMenuText()))
     




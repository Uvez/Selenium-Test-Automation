import re 
from pathlib import Path
import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
from pages.forgot_page import ForgotPage
from utilities.config_parser import ConfigParser
from globals import dir_global
from utilities.log import log

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

#reading your property file
@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    config_reader = ConfigParser("property.ini")
    return config_reader

#initialize the page objects
@pytest.fixture
def pages():
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    dashboard_page = DashBoardPage(driver)
    forgot_page = ForgotPage(driver)
    return locals()

#setup of driver
@pytest.fixture(scope="class")
def setup(prep_properties,request):
    global driver,base_url,browsername
    base_url = prep_properties.config_section_dict("AUT")["base_url"]
    browsername = request.config.getoption("browser")
    if browsername == "chrome":
        driver = webdriver.Chrome()
    if browsername == "firefox":
        driver = webdriver.Firefox()
    elif browsername =="edge":
        driver = webdriver.Edge()
    elif browsername =="chrome_headless":
        parameters = webdriver.ChromeOptions()
        parameters.add_argument("--headless")
        driver = webdriver.Chrome(parameters)
    else:
         driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()


#creating report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra',[])

    if report.when =='call' or report.when == "setup":
        xfail = hasattr(report,'wasxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            file_name = dir_global.SCREENSHOTS_PATH+"/screenshots/"+tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                #html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       #'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.image(file_name))
        report.extra = extra

#saving file 
def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)



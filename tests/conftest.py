import re 
from pathlib import Path
import pytest
import os
from selenium import webdriver
from pages.LoginPage import LoginPage
from utilities.config_parser import ConfigParserIni

driver = None

#WEB_URL ='https://www.hudl.com/'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")

@pytest.fixture(scope="session")
# instantiates ini file parses object
def prep_properties():
    config_reader = ConfigParserIni("props.ini")
    return config_reader



@pytest.fixture(scope="class")
def setup(prep_properties,request):
    global driver,base_url,browsername
    #browser = request.config.option.browser
    base_url = prep_properties.config_section_dict("AUT")["base_url"]
    browsername = request.config.getoption("browser")
    if browsername == "chrome":
        driver = webdriver.Chrome()
    elif browsername == "firefox":
        #driver = webdriver.Firefox(executable_path=log.Path+"/resources/geckodriver")
        driver = webdriver.Firefox()
    elif browsername =="edge":
        driver = webdriver.Edge()
    

    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()





##@fixture()
##def browsername(request):
    ##return request.config.getoption("--browsername")
#def pytest_generate_tests(metafunc):
#    option_value = metafunc.config.option.name
 #   if 'browsername' in metafunc.fixturenames and option_value is not None:
 #       metafunc.parametrize("browsername", [option_value])
"""
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report,'extra',[])

    if report.when =='call' or report.when == "setup":
        xfail = hasattr(report,'wasxfail')
        if(report.skipped and xfail) or (report.failed and not xfail):
            tc_name = report.nodeid.split("::")[-1]
            file_name = log.PATH+"/reports/screenshots/"+tc_name + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="screenshots/%s.png" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % tc_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
"""

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object

    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
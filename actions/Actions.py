from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Actions:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, element):
        el = self._wait.until(expected_conditions.element_to_be_clickable(element))
        el.click()

    def sendKeys(self, inputfield, value):
        el = self._wait.until(expected_conditions.element_to_be_clickable(inputfield))
        el.clear()
        el.send_keys(value)
        #inputfield.send_keys(value)

    def selectFromDropdown(self, dropdown, value):
        dropdown_element = Select(dropdown)
        dropdown_element.select_by_value(value)

    def getText(self, element):
         el = self._wait.until(expected_conditions.visibility_of_element_located(element))
         return el.text
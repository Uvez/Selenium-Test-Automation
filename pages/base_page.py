from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from utilities.log import log

class BasePage(log):

    def __init__(self,driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, element):
        try:
            el = self._wait.until(expected_conditions.element_to_be_clickable(element))
            el.click()
        except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
        except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
        except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise
           

    def sendKeys(self, inputfield, value):
        try:
            el = self._wait.until(expected_conditions.element_to_be_clickable(inputfield))
            el.clear()
            el.send_keys(value)
        except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
        except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
        except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise

    def selectFromDropdown(self, dropdown, value):
        try:
          dropdown_element = Select(dropdown)
          dropdown_element.select_by_value(value)
        except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
        except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
        except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise

    def getText(self, element):
         try:
            el = self._wait.until(expected_conditions.visibility_of_element_located(element))
            return el.text
         except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
         except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
         except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise
    
    def isVisible(self, element):
        try:
            el = self._wait.until(expected_conditions.visibility_of_element_located(element))
            return element.is_displayed()
        except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
        except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
        except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise
    
    def clickonMouse(self,element):
        try:
            hover = ActionChains(self).move_to_element(element)
            hover.perform() 
        except NoSuchElementException as err:
            self.getLogger().info('Element is not found in the webpage'+err)
        except ElementNotVisibleException as err:
            self.getLogger().info('Element is not visible in the webpage'+err)
        except Exception as err:
            self.getLogger().info(f"Unexpected {err=}, {type(err)=}")
            raise

    def scroll_to_bottom(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  
import pytest

from utilities.json_parser import JsonParser


class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, prep_properties):
        # instantiates pages object, and data readers
        #self.pages = pages
        self.config_reader = prep_properties
        self.json_reader = JsonParser("tests_data.json")
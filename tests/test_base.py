import pytest

from utilities.json_parser import JsonParser


class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self,pages,prep_properties):
        self.pages = pages
        self.config_reader = prep_properties
        self.json_reader = JsonParser("tests_data.json")
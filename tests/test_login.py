import pytest
import base64
from tests.test_base import BaseTest
from assertpy import assert_that
import time
from utilities.log import log
import allure
from utilities.json_parser import JsonParser


class Test_login(BaseTest,log):
       
       def test_enter_valid_credentails_in_login(self):
              username = self.config_reader.config_section_dict("AUT")["username"]
              password = str(base64.b64decode(self.config_reader.config_section_dict("AUT")["password"]))
              password = password.replace('b','').replace("'", "")
              self.pages['home_page'].click_on_Menu_Button()
              self.pages['home_page'].click_on_Login_Button()
              self.pages['login_page'].enter_Email(username)
              self.pages['login_page'].enter_Password(password)
              self.pages['login_page'].click_on_Continue_Button()
              time.sleep(10)
              expected_success_message = self.json_reader.read_from_json()["validate_text_Message"]["verify_dashboard_page_text"]
              actual_text = self.pages['dashboard_page'].verify_menu_text()
              assert_that(expected_success_message).is_equal_to(actual_text)
              self.pages['dashboard_page'].click_on_name_text()
              self.pages['dashboard_page'].click_on_Logout_button()


       def test_enter_empty_credentails_in_login(self):
              username =''
              password=''
              self.pages['home_page'].click_on_Menu_Button()
              self.pages['home_page'].click_on_Login_Button()
              self.pages['login_page'].enter_Email(username)
              self.pages['login_page'].enter_Password(password)
              self.pages['login_page'].click_on_Continue_Button()
              time.sleep(10)
              expected_success_message =  self.json_reader.read_from_json()["validate_text_Message"]["verify_required_Text"]
              actual_text = self.pages['login_page'].verify_Login_text()
              assert_that(expected_success_message).is_equal_to(actual_text)
              self.getLogger().info('Login successful!')
              self.pages['login_page'].click_on_Home_button()

       def test_enter_invalid_credentails_in_login(self):
              username = self.config_reader.config_section_dict("AUT")["invalid_username"]
              password = self.config_reader.config_section_dict("AUT")["invalid_password"]
              self.pages['home_page'].click_on_Menu_Button()
              self.pages['home_page'].click_on_Login_Button()
              self.pages['login_page'].enter_Email(username)
              self.pages['login_page'].enter_Password(password)
              self.pages['login_page'].click_on_Continue_Button()
              expected_success_message =  self.json_reader.read_from_json()["validate_text_Message"]["verify_Error_Message"]
              time.sleep(10)
              actual_text = self.pages['login_page'].verify_error_text()
              assert_that(expected_success_message).is_equal_to(actual_text)
              self.pages['login_page'].click_on_Home_button()


       def test_valid_forgot_password(self):
              username = self.config_reader.config_section_dict("AUT")["username"]
              self.pages['home_page'].click_on_Menu_Button()
              self.pages['home_page'].click_on_Login_Button()
              time.sleep(10)
              self.pages['forgot_page'].click_on_forgot_link()
              expected_success_message = self.json_reader.read_from_json()["validate_text_Message"]["verify_forgot_page_title"]
              assert_that(expected_success_message).is_equal_to(self.pages['forgot_page'].verify_page_title())
              self.pages['forgot_page'].enter_Email_ID(username)
              self.pages['forgot_page'].click_on_Continue_button()
              time.sleep(10)
              expected_success_message = self.json_reader.read_from_json()["validate_text_Message"]["verify_Page_title"]
              assert_that(expected_success_message).is_equal_to(self.pages['forgot_page'].verify_text_message())
              self.pages['forgot_page'].click_to_login_button()
              self.pages['login_page'].click_on_Home_button()

       def test_enter_invalid_details_in_forgot_password(self):
              username = self.config_reader.config_section_dict("AUT")["invalid_password"]
              self.pages['home_page'].click_on_Menu_Button()
              self.pages['home_page'].click_on_Login_Button()
              time.sleep(10)
              self.pages['forgot_page'].click_on_forgot_link()
              expected_success_message = self.json_reader.read_from_json()["validate_text_Message"]["verify_forgot_page_title"]
              assert_that(expected_success_message).is_equal_to(self.pages['forgot_page'].verify_page_title())
              self.pages['forgot_page'].enter_Email_ID(username)
              self.pages['forgot_page'].click_on_Continue_button()
              error_message = self.json_reader.read_from_json()["validate_text_Message"]["verify_Invalid_Message"]
              time.sleep(10)
              assert_that(error_message).is_equal_to(self.pages['forgot_page'].verify_invalid_email_message())
              self.pages['forgot_page'].click_to_login_button()
              self.pages['login_page'].click_on_Home_button()
    

     




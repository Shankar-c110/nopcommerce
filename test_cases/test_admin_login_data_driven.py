import time

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nopcommerce_selenium.base_pages.Login_Admin_Page import Login_Admin_Page
from Nopcommerce_selenium.Utilities.read_properties import Read_Config
from Nopcommerce_selenium.Utilities.custom_logger import Log_Maker
from Nopcommerce_selenium.Utilities import excel_utils

class Test_02_Admin_Login_data_driven:
    admin_page_url = Read_Config.get_admin_page_url()


    logger=Log_Maker.log_gen()
    path = ".//test_data//admin_login_data.xlsx"
    status_list = []


    # Testcase 2 and 3 actually will work. but, its not working here because of BOT
    # which is checking whether the test is automated or manually by verifying captcha
    def test_valid_admin_login_data_driven(self, setup):
        self.logger.info("**********************Test_valid_admin_login_data_driven started************************")
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(".//test_data//admin_login_data.xlsx", "Sheet1")
        print("Number of rows: ",self.rows)

        for r in range(2, self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1", r, 1)
            self.password = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.expected_login = excel_utils.read_data(self.path, "Sheet1", r, 3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)

            act_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"
            #test validation
            if act_title == expected_title :
                if self.expected_login == "Yes" :
                    self.logger.info("test data is passed") #log
                    self.status_list.append("Pass")
                    self.admin_lp.click_logout()
                elif self.expected_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.admin_lp.click_logout()
            elif act_title != expected_title:
                if self.expected_login =="Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                elif self.expected_login == "No":
                    self.logger.info("Test data is Passed")
                    self.status_list.append("Pass")
        print("Status List is: ", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test admin data driven test case is failed")
            assert False
        else:
            self.logger.info("Test admin data driven test case is Passed")
            assert True

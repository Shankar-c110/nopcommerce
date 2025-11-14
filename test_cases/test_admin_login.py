import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Nopcommerce_selenium.base_pages.Login_Admin_Page import Login_Admin_Page
from Nopcommerce_selenium.Utilities.read_properties import Read_Config
from Nopcommerce_selenium.Utilities.custom_logger import Log_Maker

class Test_01_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger=Log_Maker.log_gen()


    @pytest.mark.regression
    # Self.driver we can use it to access the class variable of above
    def test_title_verification(self, setup):
        self.logger.info("**********************Test_01_Admin_Login************************")
        self.logger.info("**********************verification of admin login page title************************")

        self.driver=setup
        self.driver.get(self.admin_page_url)
        act_title=self.driver.title
        exp_title= "nopCommerce demo store. Login"
        if act_title==exp_title:
            self.logger.info("**********************Test title verification title matched************************")
            assert True
           # self.driver.save_screenshot("nopcommerce\\screenshots\\back.png")
            self.driver.close()
        else:
            self.logger.info("**********************Test title verification title mismatched************************")
            self.driver.save_screenshot("nopcommerce\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    # Testcase 2 and 3 actually will work. but, its not working here because of BOT
    # which is checking whether the test is automated or manually by verifying captcha
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_admin_login(self, setup):
        self.logger.info("**********************Test valid admin login started************************")
        self.driver=setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        assert True
        # self.driver.close()

        act_dashboard_text= (self.driver.find_element(By.CSS_SELECTOR, "div.content-header > h1")).text
        if act_dashboard_text == "Dashboard":
               self.logger.info("**********************Dashboard text found************************")
               assert True
               self.driver.close()
        else:
               self.driver.save_screenshot("nopcommerce\\screenshots\\test_valid_admin_login.png")
               self.driver.close()
               assert False

    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
           self.logger.info("**********************Test invalid admin login started************************")
           self.driver = setup
           self.driver.get(self.admin_page_url)
           self.admin_lp = Login_Admin_Page(self.driver)
           self.admin_lp.enter_username(self.invalid_username)
           self.admin_lp.enter_password(self.password)
           self.admin_lp.click_login()
           # error_message = WebDriverWait(self.driver, 20).until(
           #     EC.visibility_of_element_located(
           #         (By.XPATH, "//div[@class='message-error validation-summary-errors']//li")
           #     )
           # ).text
           error_message=self.driver.find_element((By.XPATH, "//div[@class='message-error validation-summary-errors']//li")).text
           # error_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
           #     (By.XPATH, "//div[@class='message-error validation-summary-errors']"))).text

           if "No customer account found" in error_message:
               self.logger.info("******************************Error messages matched************************")
               assert True
               self.driver.close()
           else:
               self.driver.save_screenshot("nopcommerce//screenshots//test_invalid_admin_login.png")
               self.driver.close()
           assert False


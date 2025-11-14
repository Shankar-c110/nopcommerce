import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Nopcommerce_selenium.Utilities.custom_logger import Log_Maker
from Nopcommerce_selenium.Utilities.read_properties import Read_Config
from Nopcommerce_selenium.base_pages.Add_Customer_Page import Add_Customer_Page
from Nopcommerce_selenium.base_pages.Login_Admin_Page import Login_Admin_Page
from Nopcommerce_selenium.base_pages.Search_Customer_Page import Search_Customer_Page


class Test_03_Search_Customer:
    admin_page_url=Read_Config.get_admin_page_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()
    logger=Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_email(self, setup):
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.logger.info("******* Login Page *********")

        #Login
        self.admin_lp=Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()

        self.logger.info("******* Login Page successfull *********")

        # Handle "Verify you are human" page
        if "Verify you are human" in self.driver.page_source:
            self.logger.warning("Human verification page detected — skipping automation.")
            pytest.skip("Skipping test — Captcha present on page")

        self.logger.info("******* navigating to customer search Page **********")
        self.add_customer = Add_Customer_Page(self.driver)
        self.add_customer.click_customers()
        self.add_customer.click_customer_menu()

        # Continue to Search customer
        self.logger.info("******* Starting customer search by email **********")

        self.search_customer = Search_Customer_Page(self.driver)
        self.search_customer.enter_email("steve_gates@nopCommerce.com")
        self.search_customer.click_searchbutton()
        time.sleep(5)
        is_email_present = self.search_customer.search_customer_by_email("steve_gates@nopCommerce.com")
        if is_email_present == True:
            assert True
            self.logger.info("**************Test_04_Search_Customer_by_email test passed ******************")
            self.driver.close()
        else:
            self.logger.info("**************Test_04_Search_Customer_by_email test failed ******************")
            self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_email.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
            self.driver = setup
            self.driver.implicitly_wait(10)
            self.driver.get(self.admin_page_url)
            self.driver.maximize_window()
            self.logger.info("******* Login Page *********")

            # Login
            self.admin_lp = Login_Admin_Page(self.driver)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()

            self.logger.info("******* Login Page successfull *********")

            # Handle "Verify you are human" page
            if "Verify you are human" in self.driver.page_source:
                self.logger.warning("Human verification page detected — skipping automation.")
                pytest.skip("Skipping test — Captcha present on page")

            self.logger.info("******* navigating to customer search Page **********")
            self.add_customer = Add_Customer_Page(self.driver)
            self.add_customer.click_customers()
            self.add_customer.click_customer_menu()

            # Continue to Search customer
            self.logger.info("******* Starting customer search by name **********")

            self.search_customer = Search_Customer_Page(self.driver)
            self.search_customer.enter_firstname("Steve")
            self.search_customer.enter_lastname("Gates")
            self.search_customer.click_searchbutton()
            time.sleep(5)
            is_name_present = self.search_customer.search_customer_by_name("Steve Gates")
            if is_name_present == True:
                assert True
                self.logger.info("**************Test_04_Search_Customer_by_name test passed ******************")
                self.driver.close()
            else:
                self.logger.info("**************Test_04_Search_Customer_by_name test failed ******************")
                self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_name.png")
                self.driver.close()
                assert False

    @pytest.mark.regression
    def test_search_customer_by_companyname(self, setup):
                self.driver = setup
                self.driver.implicitly_wait(10)
                self.driver.get(self.admin_page_url)
                self.driver.maximize_window()
                self.logger.info("******* Login Page *********")

                # Login
                self.admin_lp = Login_Admin_Page(self.driver)
                self.admin_lp.enter_username(self.username)
                self.admin_lp.enter_password(self.password)
                self.admin_lp.click_login()

                self.logger.info("******* Login Page successfull *********")

                # Handle "Verify you are human" page
                if "Verify you are human" in self.driver.page_source:
                    self.logger.warning("Human verification page detected — skipping automation.")
                    pytest.skip("Skipping test — Captcha present on page")

                self.logger.info("******* navigating to customer search Page **********")
                self.add_customer = Add_Customer_Page(self.driver)
                self.add_customer.click_customers()
                self.add_customer.click_customer_menu()

                # Continue to Search customer
                self.logger.info("******* Starting customer search by companyname **********")

                self.search_customer = Search_Customer_Page(self.driver)
                self.search_customer.enter_companyname("Feds")
                self.search_customer.click_searchbutton()
                time.sleep(5)
                is_companyname_present = self.search_customer.search_customer_by_companyname("Feds")
                if is_companyname_present == True:
                    assert True
                    self.logger.info("**************Test_04_Search_Customer_by_companyname test passed ******************")
                    self.driver.close()
                else:
                    self.logger.info("**************Test_04_Search_Customer_by_companyname test failed ******************")
                    self.driver.save_screenshot(".\\screenshots\\test_search_customer_by_companyname.png")
                    self.driver.close()
                    assert False


    # # Validation
    # success_text = driver.find_element(By.XPATH, "//*[@id="customers-grid"]/tbody/tr/td[2]").text
    # assert "steve_gates@nopCommerce.com." in success_text
    # self.logger.info("**************************Customer added successfully!**************************")









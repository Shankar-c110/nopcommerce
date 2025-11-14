import random
import string

import pytest
import time

from selenium.webdriver.common.by import By

from nopcommerce.Utilities.custom_logger import Log_Maker
from nopcommerce.Utilities.read_properties import Read_Config
from nopcommerce.base_pages.Add_Customer_Page import Add_Customer_Page
from nopcommerce.base_pages.Login_Admin_Page import Login_Admin_Page

#
# def generate_random_email():
#     username ="".join(random.choices(string.ascii_lowercase+string.digits, k=8)) # 8 Characters username
#     domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com', 'example.com']) #choose from precedence
#     return f'{username}@{domain}'


# class Test_03_Add_New_Customer:
#     admin_page_url = Read_Config.get_admin_page_url()
#     username = Read_Config.get_username()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_add_new_customer(self, setup):
#         self.logger.info("***********************Test_03_Add_New_customer started*************************")
#         self.driver = setup
#         self.driver.implicitly_wait(20)
#         self.driver.get(self.admin_page_url)
#         self.admin_lp = Login_Admin_Page(self.driver)
#         self.admin_lp.enter_username(self.username)
#         self.admin_lp.enter_password(self.password)
#         self.admin_lp.click_login()
#         self.driver.maximize_window()
#         self.logger.info("***************Login Completed**********************")
#         self.logger.info("***************starting add customer test *******************")
#         moment_text_xpath="/html/body/div[1]/div/h1/img"
#         text="admin-demo.nopcommerce.com"
#         if text in self.driver.page_source("view-source:https://admin-demo.nopcommerce.com/"):
#             self.driver.close()
#             self.driver.minimize_window()
#         else:
#             self.add_customer = Add_Customer_Page(self.driver)
#             popup_text=self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[4]/div[1]/div/div[1]/h4")
#             if self.popup_text:
#                 self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[4]/div[1]/div/div[3]/span").click()
#             else:
#                 self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[4]/div[1]/div/div[3]/span").click()
#
#             # self.add_customer.close_all_info_popups()
#         self.add_customer.click_customers()
#         self.add_customer.click_customer_menu()
#         self.add_customer.click_addnew()
#         self.logger.info("*****************Providing customer info started ***************************")
#         email=generate_random_email()
#         self.add_customer.enter_email(email)
#         self.add_customer.enter_password("Test@123")
#         self.add_customer.enter_firstname("Jack")
#         self.add_customer.enter_lastname("Shrew")
#         self.add_customer.select_gender("Male")
#         self.add_customer.enter_company("MyCompany")
#         self.add_customer.select_tax_exempt()
#         self.logger.info("*****************************Customer role ************************")
#         self.add_customer.select_customer_role("Guests")
#         self.add_customer.select_manager_of_vendor("Vendor 1")
#         self.add_customer.enter_admin_comment("Test admin comment")
#         self.add_customer.click_save()
#         time.sleep(5)
#
#         self.logger.info("**********************customer details saved*******************")
#         customer_add_success_text = "The new customer has been added successfully."
#         success_text=self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[1]/div/span")
#
#         if customer_add_success_text in success_text:
#             assert True
#             self.logger.info("*************************Test_03_Add_customer test passed***************************")
#             self.driver.close()
#         else:
#             self.logger.info("**************************Test_03_Add_customer test failed**************************")
#             self.driver.save_screenshot("nopcommerce//screenshots//test_add_new_customer.png")
#             self.driver.close()
#             assert False


import pytest
import random, string, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from nopcommerce.Utilities.custom_logger import Log_Maker
from nopcommerce.Utilities.read_properties import Read_Config
from nopcommerce.base_pages.Add_Customer_Page import Add_Customer_Page
from nopcommerce.base_pages.Login_Admin_Page import Login_Admin_Page


def generate_random_email():
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "example.com"])
    return f"{username}@{domain}"


class Test_03_Add_New_Customer:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_add_new_customer(self, setup):
        driver = setup
        driver.implicitly_wait(20)
        driver.get(self.admin_page_url)
        driver.maximize_window()
        self.logger.info("******* Login Page *********")

        # Login
        admin_lp = Login_Admin_Page(driver)
        admin_lp.enter_username(self.username)
        admin_lp.enter_password(self.password)
        admin_lp.click_login()

        # Handle "Verify you are human" page
        if "Verify you are human" in driver.page_source:
            self.logger.warning("Human verification page detected — skipping automation.")
            pytest.skip("Skipping test — Captcha present on page")

        # Handle popups gracefully
        try:
            wait = WebDriverWait(driver, 5)
            popups = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[contains(@class,'modal') and contains(@class,'show')]")
                )
            )
            for popup in popups:
                try:
                    close_btn = popup.find_element(By.XPATH, ".//button[contains(text(),'×') or contains(text(),'OK') or contains(text(),'Close')]")
                    ActionChains(driver).move_to_element(close_btn).click().perform()
                    self.logger.info("Closed one popup.")
                except Exception:
                    continue
        except Exception:
            self.logger.info("No popups appeared.")

        # Continue to add customer
        add_customer = Add_Customer_Page(driver)
        add_customer.click_customers()
        add_customer.click_customer_menu()
        add_customer.click_addnew()

        email = generate_random_email()
        add_customer.enter_email(email)
        add_customer.enter_password("Test@123")
        add_customer.enter_firstname("Jack")
        add_customer.enter_lastname("Shrew")
        add_customer.select_gender("Male")
        add_customer.enter_company("MyCompany")
        add_customer.select_tax_exempt()
        # add_customer.clear_and_select_customer_role("Guests")
        # add_customer.select_customer_role("Guests")
        # add_customer.select_manager_of_vendor("Vendor 1")

        # # For Vendor
        add_customer.clear_and_select_customer_role("Guests")
        add_customer.select_manager_of_vendor("Vendor 1")
        add_customer.enter_admin_comment("Testing new customer with admin comment")
        add_customer.click_save()

        # Validation
        success_text = driver.find_element(By.XPATH, "//div[contains(@class,'alert-success')]").text
        assert "The new customer has been added successfully." in success_text
        self.logger.info("Customer added successfully!")

        driver.close()



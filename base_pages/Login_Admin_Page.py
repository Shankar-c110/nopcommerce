# # # Locators of loginpage
# import time
#
# from selenium.common import TimeoutException, ElementClickInterceptedException, NoAlertPresentException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class Login_Admin_Page:
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     btn_login_xpath = "//button[@type='submit']"
#     btn_logout_xpath = "/html/body/div[3]/nav/div/ul/li[3]/a"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def enter_username(self, username):
#         """Wait for username field before entering data"""
#         wait = WebDriverWait(self.driver, 10)
#         username_field = wait.until(
#             EC.visibility_of_element_located((By.ID, self.textbox_username_id))
#         )
#         username_field.clear()
#         username_field.send_keys(username)
#
#     def enter_password(self, password):
#         wait = WebDriverWait(self.driver, 10)
#         password_field = wait.until(
#             EC.visibility_of_element_located((By.ID, self.textbox_password_id))
#         )
#         password_field.clear()
#         password_field.send_keys(password)
#
#     def click_login(self):
#         wait = WebDriverWait(self.driver, 10)
#         login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_login_xpath)))
#         login_btn.click()
#
#     def click_logout(self):
#         wait = WebDriverWait(self.driver, 10)
#
#         # 1️⃣ Handle alert popup (e.g., "Failed to load statistics", "Ajax error")
#         try:
#             WebDriverWait(self.driver, 3).until(EC.alert_is_present())
#             alert = self.driver.switch_to.alert
#             print("Alert detected:", alert.text)
#             alert.accept()
#             print("Alert accepted.")
#         except NoAlertPresentException:
#             pass
#
#         # 2️⃣ Wait for 'loading' overlay (if exists)
#         try:
#             wait.until(EC.invisibility_of_element_located((By.ID, "loadCustomerStatisticsAlert-action-alert")))
#         except TimeoutException:
#             pass
#
#         # 3️⃣ Try clicking logout (with retry)
#         for _ in range(2):
#             try:
#                 logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
#                 logout_btn.click()
#                 print("Logout successful.")
#                 return
#             except ElementClickInterceptedException:
#                 print("Logout click intercepted. Retrying...")
#                 time.sleep(2)
#         print("Logout click failed after retries.")
#











from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login_Admin_Page:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath="//button[@type='submit']"
    btn_logout_xpath = "//a[@href='/logout']"

    # creating constructor which gets invoke when we create object for our class
    # driver is passing as an argument send by test class
    def __init__(self, driver):
        self.driver = driver

    # 3 action methods are
    # username is sent by test class
    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def click_logout(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.invisibility_of_element_located((By.ID, "loadCustomerStatisticsAlert-action-alert")))
        except TimeoutException:
            pass  # ignore if it didn’t appear
            logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_logout_xpath)))
            logout_btn.click()
            # 2️⃣ Wait until logout button is clickable
        # logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Logout']")))
        # logout_btn.click()
        # self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()



import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Add_Customer_Page:
    link_customer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    link_customer_menuoption_xpath="/html/body/div[3]/aside/div/nav/ul/li[4]/ul/li[1]/a/i"
    link_addnew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    text_email_id="Email"
    text_password_id="Password"
    text_firstname_id="FirstName"
    text_lastname_id="LastName"
    rdo_gender_male_id="Gender_Male"
    rdo_gender_female_id = "Gender_Female"
    text_companyname_id="Company"
    chbx_taxexempt_id="IsTaxExempt"
    custrole_css_Selector = "select2-selection.select2-selection--multiple"
    cusrole_guest_xpath="//li[contains(text(),'Guests')]"
    cusrole_adminstrators_xpath="//li[contains(text(),'Administrators')]"
    cusrole_forummoderators_xpath="//li[contains(text(),'Forum Moderators')]"
    cusrole_registered_xpath="//li[contains(text(),'Registered')]"
    cusrole_vendors_xpath="//li[contains(text(),'Vendors')]"
    drpdwn_mngrofvendor_id = "VendorId"
    text_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def click_customers(self):
        element1=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.link_customer_menu_xpath)))
        element1.click()

    def click_customer_menu(self):
        element2=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.link_customer_menuoption_xpath)))
        element2.click()
    def click_addnew(self):
        self.driver.find_element(By.XPATH,self.link_addnew_xpath).click()

    def enter_email(self,email):
        self.driver.find_element(By.ID,self.text_email_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def enter_firstname(self,firstname):
        self.driver.find_element(By.ID, self.text_firstname_id).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.ID, self.text_lastname_id).send_keys(lastname)

    def select_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rdo_gender_male_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdo_gender_female_id).click()
        else:
            self.driver.find_element(By.ID,self.rdo_gender_female_id).click()

    def enter_company(self,companyname):
        self.driver.find_element(By.ID, self.text_companyname_id).send_keys(companyname)

    def select_tax_exempt(self):
        self.driver.find_element(By.ID, self.chbx_taxexempt_id).click()
        time.sleep(3)

    def select_customer_role(self, role):
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, custrole_css_selector))
        # )
        # element.click()
        elements=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.custrole_css_Selector)))
        elements.click()
        cusrole_field = elements[1]
        cusrole_field.click()
        time.sleep(3)
        if role =="Guests":
            self.driver.find_element(By.XPATH, self.cusrole_registered_xpath).click() #to unselect the default selected registered option
            time.sleep(3)
            cusrole_field.click()
            self.driver.find_element(By.XPATH, self.cusrole_guest_xpath) #to select the guest option
        elif role == "Administrators":
            self.driver.find_element(By.XPATH, self.cusrole_adminstrators_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.cusrole_forummoderators_xpath).click()
        elif role == "Registered":
            pass
        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.cusrole_vendors_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.cusrole_adminstrators_xpath).click()

    def select_manager_of_vendor(self, value):
        drp_dwn=Select(self.driver.find_element(By.ID, self.drpdwn_mngrofvendor_id))
        drp_dwn.select_by_visible_text(value)

    def enter_admin_comment(self, admincomments):
        self.driver.find_element(By.ID, self.text_admincomment_id).send_keys(admincomments)

    def click_save(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def close_all_info_popups(self):
        """
        Closes any visible 'Failed to load statistics' popup(s) that block interaction.
        Works for multiple stacked modals.
        """
        print("Checking for info popups...")
        try:
            wait = WebDriverWait(self.driver, 15)

            # Wait for modal overlay to appear (if any)
            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.modal.fade.show"))
            )
            time.sleep(1)  # allow DOM to stabilize

            while True:
                modals = self.driver.find_elements(By.CSS_SELECTOR, "div.modal.fade.show")
                if not modals:
                    break

                for modal in modals:
                    try:
                        ok_button = modal.find_element(By.XPATH, ".//button[text()='Ok']")
                        self.driver.execute_script("arguments[0].click();", ok_button)
                        print("Clicked OK button to close popup.")
                        time.sleep(1)
                    except Exception as e:
                        print(f"Could not click OK in one popup: {e}")
                        pass

                # short wait before re-checking (handles multiple stacked modals)
                time.sleep(1)

                modals = self.driver.find_elements(By.CSS_SELECTOR, "div.modal.fade.show")
                if not modals:
                    print("All info popups closed.")
                    break

        except TimeoutException:
            print("No info popup appeared within wait time.")

    def clear_and_select_customer_role(self, role_name):
        """
        Clears existing customer roles and selects a new role.
        Handles mutually exclusive logic in nopCommerce.
        """
        import time

        # 1. Click dropdown
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".select2-selection.select2-selection--multiple")
        dropdown.click()
        time.sleep(0.3)

        # 2. Remove any pre-selected roles
        selected_roles = self.driver.find_elements(By.CSS_SELECTOR, ".select2-selection__choice")
        for role in selected_roles:
            remove_btn = role.find_element(By.CSS_SELECTOR, "span.select2-selection__choice__remove")
            remove_btn.click()
            time.sleep(0.2)

        # 3. Click dropdown again to make sure options are visible
        dropdown.click()
        time.sleep(0.3)

        # 4. Find all available options
        options = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.select2-results__options li"))
        )

        # 5. Select the desired role
        for option in options:
            if option.text.strip() == role_name:
                option.click()
                time.sleep(0.3)
                break

        # 6. Click outside to close the dropdown
        self.driver.execute_script("arguments[0].blur();", dropdown)
        time.sleep(0.2)
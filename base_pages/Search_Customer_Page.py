import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search_Customer_Page:
    link_customer_option_xpath = "//p[contains(text(),'Customers')]/ancestor::a"
    link_customer_menu_xpath = "//ul[@class='nav nav-treeview']//p[normalize-space()='Customers']"
    text_email_field_id = "SearchEmail"
    text_first_name_id = "SearchFirstName"
    text_last_name_id = "SearchLastName"
    text_company_name_id = "SearchCompany"
    click_search_button_id = "search-customers"

    rows_table_xpath="//table[@id='customers-grid']/tbody//tr"
    columns_table_xpath = "//table[@id='customers-grid']/tbody//tr/td"

    def __init__(self, driver):
        self.driver = driver

    # def click_customer(self):
    #     """Expand the main Customers menu"""
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, self.link_customer_option_xpath))
    #     ).click()
    #       # small pause to ensure submenu appears
    #
    # def click_customer_menu(self):
    #     """Click the Customers submenu"""
    #     self.click_customer()
    #     WebDriverWait(self.driver, 15).until(
    #         EC.element_to_be_clickable((By.XPATH, self.link_customer_menu_xpath))
    #     ).click()



    def enter_email(self, email):
        self.driver.find_element(By.ID, self.text_email_field_id).clear()
        self.driver.find_element(By.ID, self.text_email_field_id).send_keys(email)

    def enter_firstname(self, firstname):
        self.driver.find_element(By.ID, self.text_first_name_id).clear()
        self.driver.find_element(By.ID, self.text_first_name_id).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(By.ID, self.text_last_name_id).clear()
        self.driver.find_element(By.ID, self.text_last_name_id).send_keys(lastname)

    def enter_companyname(self, companyname):
        self.driver.find_element(By.ID, self.text_company_name_id).clear()
        self.driver.find_element(By.ID, self.text_company_name_id).send_keys(companyname)

    def click_searchbutton(self):
        self.driver.find_element(By.ID, self.click_search_button_id).click()

    def got_results_table_rows(self):
        return len(self.driver.find_element(By.XPATH,self.rows_table_xpath))

    def got_results_table_columns(self):
        return len(self.driver.find_elements(By.XPATH,self.rows_table_xpath))

    def search_customer_by_email(self,email):
        email_present_flag = False #initializing boolean variable as false
        for r in range(1, self.get_results_table_rows()+1):
            cus_email = self.driver.find_element(By.XPATH,"//table[@id='customers-grid'/tbody//tr["+str(r)+"]/td[2]") #dynamic xpath for email
            if cus_email == email:
                email_present_flag = True
                break
        return email_present_flag

    def search_customer_by_name(self,name):
        name_present_flag = False #initializing boolean variable as false
        for r in range(1, self.get_results_table_rows()+1):
            cus_name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid'/tbody//tr["+str(r)+"]/td[3]")  #dynamic xpath for name
            if cus_name == name:
                name_present_flag = True
                break
        return name_present_flag

    def search_customer_by_companyname(self,companyname):
        companyname_present_flag = False #initializing boolean variable as false
        for r in range(1, self.get_results_table_rows()+1):
            cus_companyname = self.driver.find_element(By.XPATH,"//table[@id='customers-grid'/tbody//tr["+str(r)+"]/td[5]")  #dynamic xpath for companyname
            if cus_companyname == companyname:
                companyname_present_flag = True
                break
        return companyname_present_flag

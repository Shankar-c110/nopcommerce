import pytest
# import undetected_chromedriver as uc
from selenium import webdriver
from pytest_metadata.plugin import metadata_key



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser:")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser.lower() == "chrome":
        driver=webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver=webdriver.Firefox()
    elif browser.lower() == "edge":
        driver=webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()


from pytest_metadata.plugin import metadata_key
############for pytest html reports ##########
#hook for adding environment info in html report
# def pytest_configure(config):
#     # Get or create metadata dictionary from pytest-html
#     metadata = config.stash.get(metadata_key, {})
#     metadata['Project Name']='Ecommerce Project, nopcommerce'
#     metadata['Test Module Name']='Admin Login Tests'
#     metadata['Tester name']='Shankar'
#     # Save metadata back to stash
#     config.stash[metadata_key] = metadata
#
# #hook for delete/modify environment info in html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME',None) #deletes the JAVA_HOME detail in html report
#     metadata.pop('Plugins',None) #deletes the Plugins detail in html report
#
# @pytest.mark.optionalhook
# def pytest_html_report_title(report):
#     report.title = "nopCommerce Automation Test Report"
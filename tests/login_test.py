from selenium import webdriver
import pytest
import allure
import moment
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            # assert x == "abc"
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/PythonAutomation/AutomationFramework_1/screenshots/"
                                          + screenshot_name + ".png")
            raise

        except:
            print("There was an exception")

            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)

            raise

        else:
            print("No exception occurred")

        finally:
            print("I am inside finally block")

# C:\PythonAutomation\AutomationFramework_1>python -m pytest

# C:\PythonAutomation\AutomationFramework_1>python -m pytest --html=reports/report_name.html --self-contained-html

# C:\PythonAutomation\AutomationFramework_1>python -m pytest --browser chrome

# C:\PythonAutomation\AutomationFramework_1>python -m pytest --browser firefox


# C:\PythonAutomation\AutomationFramework_1>python -m pytest --alluredir=reports/allure-reports
# C:\PythonAutomation\AutomationFramework_1>allure serve reports/allure-reports

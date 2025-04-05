
"""
Headless_Task.py contains the selenium automation methods
https://www.guvi.in/

Validating the username text box
Validating the password text box
Validating the sign in url
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class GuviData:
    # Test Data
    url = "https://www.guvi.in"
    login_url="https://www.guvi.in/sign-in/"
    dashboard_url = "https://www.guvi.in/courses/?current_tab=myCourses"
    username = "manojsekar.6696@gmail.com"
    password = "Lucky@96"

class GuviLocators:
    # Test Locators
    Main_page_login_button_locator='//*[@id="login-btn"]'#Xpath locator
    username_input_locator = 'email' #Id locator
    password_input_locator = 'password' #Id locator
    login_button_locator = 'login-btn' # Id locator


class HeadlessTesting:
    def __init__(self, url):
        self.url = url

        # enable headless browsing using chrome browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        # webdriver headless chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    def start(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(4)
            return True
        except Exception as error:
            print("ERROR : Automation Failed!", error)
            return False

    def shutdown(self):
        self.driver.quit()
        return None

    def validate_username_input_box(self):
        username_input_box = self.driver.find_element(by=By.ID, value=GuviLocators.username_input_locator)
        if username_input_box.is_displayed():
            return True
        else:
            return False

    def validate_password_input_box(self):
        password_input_box = self.driver.find_element(by=By.ID, value=GuviLocators.password_input_locator)
        if password_input_box.is_displayed():
            return True
        else:
            return False

    def validate_login_button(self):
        login_button = self.driver.find_element(by=By.ID, value=GuviLocators.login_button_locator)
        if login_button.is_displayed():
            return True
        else:
            return False

    def validate_Guvi_login(self):
        try:
            self.driver.find_element(by=By.XPATH, value=GuviLocators.Main_page_login_button_locator).click()
            sleep(4)
            if self.driver.current_url == GuviData.login_url:
                return self.driver.current_url
            else:
                return False

        except Exception as error:
            print("ERROR : Login Failed", error)


    def validate_login(self):
        try:
            self.driver.find_element(by=By.ID, value=GuviLocators.username_input_locator).send_keys(GuviData.username)
            sleep(2)
            self.driver.find_element(by=By.ID, value=GuviLocators.password_input_locator).send_keys(GuviData.password)
            sleep(2)
            self.driver.find_element(by=By.ID, value=GuviLocators.login_button_locator).click()
            sleep(4)
            if self.driver.current_url == GuviData.dashboard_url:
                return self.driver.current_url
            else:
                return False

        except Exception as error:
            print("ERROR : Login Failed", error)

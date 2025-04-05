"""
Test_Guvi_site.py contains all the test cases
"""

from Headless_Task import HeadlessTesting
from Headless_Task import GuviData

# create object from HeadlessTesting Class
myChrome = HeadlessTesting(GuviData.url)

def test_start():
    assert myChrome.start() == True
    print("SUCCESS: Automation Started!")


# create function for sign in url validation

def test_validate_sign_in_login():
    assert myChrome.validate_Guvi_login() == GuviData.login_url
    print("SUCCESS : Visited Sign in!")


# create function for username validation

def test_validate_username_input_box():
    assert myChrome.validate_username_input_box() == True
    print("SUCCESS : Username Input Box is visible!")

# create function for password validation

def test_validate_password_input_box():
    assert myChrome.validate_password_input_box() == True
    print("SUCCESS : Password Input Box is visible!")

# create function for login button is visible or not validation

def test_validate_login_button():
    assert myChrome.validate_login_button() == True
    print("SUCCESS : Login Button is visible!")


# create function for login url validation

def test_validate_Homepage_login():
    assert myChrome.validate_login() == GuviData.dashboard_url
    print("SUCCESS : Homepage_Logged in!")

# create function for shutdown the automation

def test_shutdown():
    assert myChrome.shutdown() == None
    print("SUCCESS : Automation Closed!")
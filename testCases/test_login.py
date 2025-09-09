import pytest
from selenium import webdriver
from pageObjects.loginPage import Login

class Test_Logins:
    BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_valid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.BaseUrl)
        login_Page=Login(driver)
        login_Page.enter_username("Admin")
        login_Page.enter_password("admin123")
        login_Page.click_login()
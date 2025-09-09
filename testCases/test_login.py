import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from testCases import conftest

class Test_Logins:
    BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_valid_login(self,setup):
        driver=setup
        driver.get(self.BaseUrl)
        login_Page=Login(driver)
        login_Page.enter_username("Admin")
        login_Page.enter_password("admin123")
        login_Page.click_login()
        assert "dashboard" in driver.current_url
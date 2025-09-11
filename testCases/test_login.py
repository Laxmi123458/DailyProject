import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
from testCases import conftest
from utilies.readProperties import ReadConfig
from utilies.customLogger import LogGen

class TestLogin:
    BaseUrl = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()  # instantiate logger once

    @pytest.mark.parametrize("username,password", [("Admin","admin123")])
    def test_valid_login(self, setup, username, password):
        self.logger.info("TestLogin")
        self.logger.info("Verifying the valid login")
        driver = setup
        driver.get(self.BaseUrl)
        driver.save_screenshot(".\\screenshots\\login.png")
        login_Page = Login(driver)
        login_Page.enter_username(username)
        login_Page.enter_password(password)
        login_Page.click_login()
        assert "dashboard" in driver.current_url.lower() or "Dashboard" in driver.page_source
        self.logger.info("Successfully loggedin")


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    Username_field="username"
    Password_field="password"
    login_button = "button[type='submit']"

    def __init__(self, driver):
        self.driver = driver  # Webdriver instance
        self.wait = WebDriverWait(driver, 10)  # Explicit wait with a 10-second timeout

    # Method for actions with explicit wait
    def enter_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.Username_field)))
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, self.Password_field)))
        password_field.send_keys(password)

    def click_login(self):
        login_buttons = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))
        login_buttons.click()
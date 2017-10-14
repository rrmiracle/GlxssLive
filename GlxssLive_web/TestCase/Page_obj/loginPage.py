from selenium.webdriver.common.by import By
from .Page import Page
import time


class login(Page):
    '''用户登录页面'''

    url = '/index.html'

    def verify(self):
        return self.on_page()

    login_username_loc = (By.NAME, "usernamee")
    login_password_loc = (By.NAME, "password")
    login_code_loc = (By.NAME, "codee")
    login_button_loc = (By.XPATH, ".//*[@id='loginForm']/button")

    # Action
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_code(self, code):
        self.find_element(*self.login_code_loc).send_keys(code)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login(self, username="", password="", code=""):
        self.login_username(username)
        self.login_password(password)
        self.login_code(code)
        time.sleep(10)
        self.login_button()
        time.sleep(2)

    error_hint_loc = (By.XPATH, ".//*[@id='loginForm']/h4")
    pop_error_loc = (By.CSS_SELECTOR, ".layui-layer-content")

    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    def pop_error_hint(self):
        return self.find_element(*self.pop_error_loc).text
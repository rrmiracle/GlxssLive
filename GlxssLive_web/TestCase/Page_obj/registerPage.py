from selenium.webdriver.common.by import By
from .Page import Page
import time


class register(Page):
    '''用户注册页面'''
    url = "/mailSend.html"

    def verify_page(self):
        return self.on_page()

    open_link_loc = (By.LINK_TEXT, "立即注册»")

    def goto_register(self):
        self.find_element(*self.open_link_loc).click()
        time.sleep(3)

    register_bscode_loc = (By.NAME, "businessCode")
    register_email_loc = (By.NAME, "email")
    register_username_loc = (By.NAME, "username")
    register_password_loc = (By.NAME, "password")
    register_confirmpsd_loc = (By.NAME, "ok")
    register_code_loc = (By.NAME, "captcha")
    register_button_loc = (By.XPATH, ".//*[@id='registerForm']/button")

    # Action
    def register_bscode(self, bscode):
        self.find_element(*self.register_bscode_loc).send_keys(bscode)

    def register_email(self, email):
        self.find_element(*self.register_email_loc).send_keys(email)

    def register_username(self, username):
        self.find_element(*self.register_username_loc).send_keys(username)

    def register_password(self, password):
        self.find_element(*self.register_password_loc).send_keys(password)

    def register_confirmpsd(self, confirmpsd):
        self.find_element(*self.register_confirmpsd_loc).send_keys(confirmpsd)

    def register_code(self, code):
        self.find_element(*self.register_code_loc).send_keys(code)

    def register_button(self):
        self.find_element(*self.register_button_loc).click()

    def register(self, bscode="", email="", username="", password="", confirmpsd="", code=""):
        self.register_bscode(bscode)
        self.register_email(email)
        self.register_username(username)
        self.register_password(password)
        self.register_confirmpsd(confirmpsd)
        # self.register_code(code)
        # time.sleep(10)
        self.register_button()

    error_hint_loc = (By.XPATH, ".//*[@id='registerForm']/h4")
    pop_error_loc = (By.CSS_SELECTOR, ".layui-layer-content")

    def error_hint(self):
        return self.find_element(*self.error_hint_loc).text

    def pop_error_hint(self):
        return self.find_element(*self.pop_error_loc).text
from selenium.webdriver.common.by import By
from .registerPage import register
import time


class forgotpassword(register):
    '''忘记密码页面'''
    url = "/retrievePassword.html"

    def verify_page(self):
        return self.on_page()

    open_link_loc = (By.LINK_TEXT, "忘记密码»")

    def goto_forgotpassword(self):
        self.find_element(*self.open_link_loc).click()
        time.sleep(3)

    forgotpassword_email_loc = (By.NAME, "email")
    forgotpassword_code_loc = (By.XPATH, ".//*[@id='registerForm']/div[2]/input")
    forgotpassword_new_loc = (By.NAME, "password")
    forgotpassword_confirm_loc = (By.NAME, "ok")
    forgotpassword_send_button_loc = (By.XPATH, ".//*[@id='registerForm']/div[2]/button")

    def forgot_password(self, email, password="", confirmpsd="", code=""):
        self.find_element(*self.forgotpassword_email_loc).send_keys(email)
        self.find_element(*self.forgotpassword_new_loc).send_keys(password)
        self.find_element(*self.forgotpassword_confirm_loc).send_keys(confirmpsd)
        # self.find_element(*self.forgotpassword_code_loc).send_keys(code)

    def save(self):
        self.register_button()
        time.sleep(1)

    def send_code(self):
        self.find_element(*self.forgotpassword_send_button_loc).click()
        time.sleep(30)

    result_loc = (By.XPATH, "html/body/div[3]/p")

    def success(self):
        return self.find_element(*self.result_loc).get_attribute("innerText") == "修改成功！请点击确认按钮跳转到登录页面"



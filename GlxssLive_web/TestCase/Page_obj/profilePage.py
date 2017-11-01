from selenium.webdriver.common.by import By
from .sidemenuPage import sidemenu
import time


class profile(sidemenu):
    '''个人信息页面'''

    def switch_to_frame(self):
        self.driver.switch_to.frame(1)

    profile_loc = (By.XPATH, ".//*[@id='side-menu']/li[1]/div[1]/ul/li[1]/a")

    def open_profile(self):
        self.expand()
        self.drop_down_menu()
        self.find_element(*self.profile_loc).click()
        time.sleep(1)
        self.switch_to_frame()
        time.sleep(2)

    avatar_loc = (By.XPATH, ".//*[@id='personalForm']/div[1]/div/div[2]/p[2]/input")
    name_loc = (By.NAME, "username")
    tagname_loc = (By.XPATH, ".//*[@id='perapp']/div/div/div/div[1]/h5")

    def verify(self):
        return self.tagname() == "个人中心"

    def profile_avetar(self):
        self.find_element(*self.avatar_loc).click()
        time.sleep(3)

    def profile_name(self, name):
        self.find_element(*self.name_loc).send_keys(name)

    def clear(self):
        self.find_element(*self.name_loc).clear()
        time.sleep(1)

    save_button_loc = (By.XPATH, ".//*[@id='personalForm']/div[6]/div/div[2]/button")
    modify_button_loc = (By.XPATH, ".//*[@id='personalForm']/div[3]/div/div[2]/p[3]/a")

    def profile_save(self):
        self.find_element(*self.save_button_loc).click()

    def profile_modify(self):
        self.find_element(*self.modify_button_loc).click()
        time.sleep(2)

    password_save_button_loc = (By.XPATH, ".//*[@id='passwordForm']/div[5]/div/button[1]")
    password_back_button_loc = (By.XPATH, ".//*[@id='passwordForm']/div[5]/div/a")
    password_old_loc = (By.NAME, "password")
    password_new_loc = (By.NAME, "newpassword")
    password_confirm_loc = (By.NAME, "confirm")

    def password_save(self):
        self.find_element(*self.password_save_button_loc).click()
        time.sleep(2)

    def password_back(self):
        self.find_element(*self.password_back_button_loc).click()
        time.sleep(2)

    def password_modify(self, oldpassword, newpassword, confirmpsd):
        self.find_element(*self.password_old_loc).send_keys(oldpassword)
        self.find_element(*self.password_new_loc).send_keys(newpassword)
        self.find_element(*self.password_confirm_loc).send_keys(confirmpsd)

    OK_button_loc = (By.XPATH, "html/body/div[3]/div[7]/button[2]")

    def OK(self):
        self.find_element(*self.OK_button_loc).click()
        time.sleep(2)

    error_hint_name_loc = (By.ID, "username-error")
    error_hint_password_old_loc = (By.ID, "password-error")
    error_hint_password_new_loc = (By.ID, "newPsd-error")
    error_hint_password_confirm_loc = (By.ID, "confirm-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_old_password(self):
        return self.find_element(*self.error_hint_password_old_loc).text

    def error_new_password(self):
        return self.find_element(*self.error_hint_password_new_loc).text

    def error_confirm_password(self):
        return self.find_element(*self.error_hint_password_confirm_loc).text


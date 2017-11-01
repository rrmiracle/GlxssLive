from selenium.webdriver.common.by import By
from .usermanagePage import usermanage
import time


class rolemanage(usermanage):
    '''用户管理页面'''

    def verify(self):
        return self.tagname() == "角色管理"

    usermanage_loc = (By.LINK_TEXT, "用户管理")
    role_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[3]/ul/li[2]/a")

    def open_rolemanage(self):
        self.expand()
        self.find_element(*self.usermanage_loc).click()
        time.sleep(1)
        self.find_element(*self.role_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    role_add_name_loc = (By.NAME, "userRole.roleName")
    role_add_remark_loc = (By.NAME, "userRole.remark")

    def _name(self, name):
        self.find_element(*self.role_add_name_loc).send_keys(name)

    def clear_name(self):
        self.find_element(*self.role_add_name_loc).clear()

    def _remark(self, remark):
        self.find_element(*self.role_add_remark_loc).send_keys(remark)

    def clear_remark(self):
        self.find_element(*self.role_add_remark_loc).clear()

    def add_role(self, name, remark):
        self._name(name)
        self._remark(remark)

    add_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/a")
    #我的会话checkbox
    role_menu_checkbox_loc = (By.XPATH, ".//*[@id='commentForm']/div[5]/div[1]/ul/li[1]/a/label/span")

    def change_role_menu(self):
        self.find_element(*self.role_menu_checkbox_loc).click()
        time.sleep(1)

    list_name_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[3]/div/table/tbody/tr[1]/td[2]/span")

    def name_list(self):
        return self.find_element(*self.list_name_loc).get_attribute("innerText")

    error_hint_name_loc = (By.ID, "userRole.roleName-error")
    error_hint_remark_loc = (By.ID, "userRole.remark-error")

    def error_remark(self):
        return self.find_element(*self.error_hint_remark_loc).text





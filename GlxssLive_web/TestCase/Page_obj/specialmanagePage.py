from selenium.webdriver.common.by import By
from .devicemanagePage import devicemanage
import time


class specialmanage(devicemanage):

    def verify(self):
        return self.tagname() == "专业管理"

    special_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[4]/ul/li[4]/a")

    def open_specialmanage(self):
        self.expand()
        self.find_element(*self.bsmanage_loc).click()
        time.sleep(1)
        self.find_element(*self.special_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    special_add_name_loc = (By.NAME, "bssBusinessSpecialty.specialtyName")

    def _name(self, name):
        self.find_element(*self.special_add_name_loc).send_keys(name)

    def name_clear(self):
        self.find_element(*self.special_add_name_loc).clear()
        time.sleep(1)

    def add_special(self, name):
        self._name(name)
        time.sleep(1)

    add_save_button_loc = (By.XPATH, ".//*[@id='specialtyForm']/div[4]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='specialtyForm']/div[4]/div/a")

    modify_company_loc = (By.NAME, "bssBusinessSpecialty.bsName")

    list_name_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr/td[3]/span")

    def name_list(self):
        return self.find_element(*self.list_name_loc).get_attribute("innerText")

    error_hint_name_loc = (By.ID, "bssBusinessSpecialty.specialtyName-error")
    error_hint_company_loc = (By.ID, "bssDept-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_company(self):
        return self.find_element(*self.error_hint_company_loc).text




from selenium.webdriver.common.by import By
from .sidemenuPage import sidemenu
import time


class devicemanage(sidemenu):

    def verify(self):
        return self.tagname() == "设备管理"

    bsmanage_loc = (By.LINK_TEXT, "企业管理")
    device_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[4]/ul/li[2]/a")

    def open_devicemanage(self):
        self.expand()
        self.find_element(*self.bsmanage_loc).click()
        time.sleep(1)
        self.find_element(*self.device_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    add_button_loc =




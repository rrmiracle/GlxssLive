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

    add_button_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[1]/div/a[1]/i")
    modify_button_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[1]/div/a[2]/i")
    delete_button_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[1]/div/a[2]/i")

    checkbox_1_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span")
    checkbox_2_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span")

    device_add_name_loc = (By.NAME, "bssEquipment.name")
    device_add_version_loc = (By.NAME, "version")
    device_add_serial_loc = (By.NAME, "bssEquipment.serial")

    def _name(self, name):
        self.find_element(*self.device_add_name_loc).send_keys(name)

    def _version(self, version):
        self.find_element(*self.device_add_name_loc).send_keys(version)

    def _serial(self, serial):
        self.find_element(*self.device_add_name_loc).send_keys(serial)

    def add_device(self, name, version, serial):
        self._name(name)
        self._version(version)
        self._serial(serial)

    def name_clear(self):
        self.find_element(*self.device_add_name_loc).clear()

    def version_clear(self):
        self.find_element(*self.device_add_version_loc).clear()

    def serial_clear(self):
        self.find_element(*self.device_add_serial_loc).clear()

    add_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/a")

    list_serial_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]")

    def serial_list(self):
        return self.find_element(*self.list_serial_loc).get_attribute("innerText")






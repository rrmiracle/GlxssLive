import time


class DeviceManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_devicemanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("企业管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[4]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)

    def input(self, name, version, number):
        self.driver.find_element_by_name("bssEquipment.name").send_keys(name)
        self.driver.find_element_by_name("version").send_keys(version)
        self.driver.find_element_by_name("bssEquipment.serial").send_keys(number)

    def clear(self, type):
        if type == 1:
            self.driver.find_element_by_name("bssEquipment.name").clear()
        if type == 2:
            self.driver.find_element_by_name("version").clear()
        if type == 3:
            self.driver.find_element_by_name("bssEquipment.serial").clear()

    def status(self):
        q = self.driver.find_element_by_name("bssEquipment.bsName")
        return q.get_attribute("disabled")

    def table(self):
        q = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[5]"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def name(self):
        msg = self.driver.find_element_by_id("bssEquipment.name-error").text
        return msg

    def version(self):
        msg = self.driver.find_element_by_id("version-error").text
        return msg

    def number(self):
        msg = self.driver.find_element_by_id("bssEquipment.serial-error").text
        return msg

    def company(self):
        msg = self.driver.find_element_by_id("bssDept-error").text
        return msg

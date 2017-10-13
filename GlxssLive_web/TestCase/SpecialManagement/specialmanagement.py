import time


class SpecialManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_specialmanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("企业管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)

    def input(self, name):
        self.driver.find_element_by_name("bssBusinessSpecialty.specialtyName").send_keys(name)
        time.sleep(2)

    def clear(self):
        self.driver.find_element_by_name("bssBusinessSpecialty.specialtyName").clear()

    def status(self):
        q = self.driver.find_element_by_name("bssBusinessSpecialty.bsName")
        return q.get_attribute("disabled")

    def table(self):
        q = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr/td[3]/span"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='specialtyForm']/div[4]/div/button").click()
        time.sleep(1)

    def back(self):
        self.driver.find_element_by_xpath(".//*[@id='specialtyForm']/div[4]/div/a").click()
        time.sleep(1)


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def name(self):
        msg = self.driver.find_element_by_id("bssBusinessSpecialty.specialtyName-error").text
        return msg

    def company(self):
        msg = self.driver.find_element_by_id("bssDept-error").text
        return msg

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SessionManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_sessionmanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("工作管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[2]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)

    def input(self, name, keyword):
        self.driver.find_element_by_name("wmmManager.roomName").send_keys(name)
        self.driver.find_element_by_name("wmmManager.keyword").send_keys(keyword)
        time.sleep(2)

    def clear(self, type):
        if type == 1:
            time.sleep(1)
            js = "var q = document.getElementsByName('wmmManager.roomName')[0]; return q.value"
            q = len(self.driver.execute_script(js))
            for i in range(0, q):
                self.driver.find_element_by_name("wmmManager.roomName").send_keys(Keys.BACK_SPACE)
        elif type == 2:
            time.sleep(1)
            js = "var q = document.getElementsByName('wmmManager.keyword')[0]; return q.value"
            q = len(self.driver.execute_script(js))
            for i in range(0, q):
                self.driver.find_element_by_name("wmmManager.keyword").send_keys(Keys.BACK_SPACE)

    def status(self):
        q = self.driver.find_element_by_name("bssBusinessSpecialty.bsName")
        return q.get_attribute("disabled")

    def table(self):
        q = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='wssessionroomForm']/div[4]/div/button").click()
        time.sleep(1)

    def back(self):
        try:
            self.driver.find_element_by_xpath(".//*[@id='wssessionroomForm']/div[4]/div/a").click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[2]/div/div/div/a").click()
        time.sleep(1)

    def tagname(self):
        try:
            name = self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[1]/h5").text
            return name
        except NoSuchElementException:
            name = self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div[1]/h5").text
            return name

    def check(self):
        checkbox = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[1]/div/a[1]/i").click()
        time.sleep(2)

    def modify(self):
        checkbox = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(2)

    def delete(self):
        checkbox = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[1]/div/a[3]/i").click()
        time.sleep(2)

    def uncheck(self):
        self.driver.find_element_by_xpath(".//*[@id='wmmapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(2)

    def multi_select(self):
        checkbox1 = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        checkbox2 = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox1).click()
        self.driver.find_element_by_xpath(checkbox2).click()


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def name(self):
        msg = self.driver.find_element_by_id("wmmManager.roomName-error").text
        return msg

    def keyword(self):
        msg = self.driver.find_element_by_id("wmmManager.keyword-error").text
        return msg

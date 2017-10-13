import time
from selenium.webdriver.common.action_chains import ActionChains


class Session:
    def __init__(self, driver):
        self.driver = driver

    def wsnotification(self):
        msg = self.driver.find_element_by_id("gritter-item-1").get_attribute("innerText")
        return msg

    def status(self):
        msg = self.driver.find_element_by_class_name("drop1").get_attribute("innerText")
        return msg

    def changestatus(self):
        ActionChains(self.driver).click(self.driver.find_element_by_link_text("空闲中")).perform()
        time.sleep(1)
        self.driver.find_element_by_link_text("置忙").click()
        time.sleep(1)

    def send(self):
        element = self.driver.find_element_by_class_name("chat-form")
        element.find_elements_by_class_name("fa")[1].click()
        time.sleep(1)

    def alert(self):
        msg = self.driver.find_element_by_xpath(".//*[@id='myCue']/div/div/div[2]/strong").text
        return msg


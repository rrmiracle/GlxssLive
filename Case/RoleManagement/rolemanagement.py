import time
from selenium.common.exceptions import NoSuchElementException


class RoleManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_rolemanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("用户管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[3]/ul/li[2]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)

    def tagname(self):
        try:
            name = self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/h5").text
            return name
        except NoSuchElementException:
            name = self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div[1]/h5").text
            return name

    def add_role(self):
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[1]/i").click()
        time.sleep(2)

    def input(self, rolename, note):
        self.driver.find_element_by_name("userRole.roleName").send_keys(rolename)
        self.driver.find_element_by_name("userRole.remark").send_keys(note)

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[6]/div/button").click()

    def back(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[6]/div/a").click()

    def select_company(self):
        self.driver.find_element_by_xpath(".//*[@id='bsType_chosen']/a/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bsType_chosen']/div/ul/li").click()
        time.sleep(1)

    def modify_role(self):
        checkbox = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(2)

    def update_name(self, newname):
        self.driver.find_element_by_name("userRole.roleName").send_keys(newname)

    def clear(self, type):
        if type == 1:
            self.driver.find_element_by_name("userRole.roleName").clear()
        elif type == 2:
            self.driver.find_element_by_name("userRole.remark").clear()

    def checkbox(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[5]/div[1]/ul/ul/li/a/label/span").click()
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[5]/div[2]/ul/ul/li/a/label/span").click()
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[5]/div[3]/ul/ul/li/a/label/span").click()

    def delete_role(self):
        checkbox = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[3]/i").click()
        time.sleep(2)

    def table(self):
        q = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/span"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg

    def status(self):
        q = self.driver.find_element_by_id("bsType_chosen")
        return q.get_property("isContentEditable")


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def rolename(self):
        msg = self.driver.find_element_by_id("userRole.roleName-error").text
        return msg

    def company(self):
        msg = self.driver.find_element_by_id("bsType-error").text
        return msg

    def note(self):
        msg = self.driver.find_element_by_id("userRole.remark-error").text
        return msg
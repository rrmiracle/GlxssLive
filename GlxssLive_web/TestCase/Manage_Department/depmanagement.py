import time
from selenium.webdriver.support.select import Select


class DepartmentManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_depmanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("企业管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[4]/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[6]/div/button").click()
        time.sleep(1)

    def select(self):
        self.driver.find_element_by_xpath(".//*[@id='bssDept_chosen']/a/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bssDept_chosen']/div/ul/li").click()

    def input(self, name, number):
        self.driver.find_element_by_name("bssDept.name").send_keys(name)
        self.driver.find_element_by_name("bssDept.orderNum").send_keys(number)

    def back(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[6]/div/a").click()
        time.sleep(1)

    def clear(self, type):
        if type == 1:
            self.driver.find_element_by_name("bssDept.name").clear()
        if type == 2:
            self.driver.find_element_by_name("bssDept.orderNum").clear()

    def status(self):
        q = self.driver.find_element_by_id("bssDept_chosen")
        return q.get_property("isContentEditable")

    def dept(self):
        select = self.driver.find_element_by_name("bssDeptSelect.parentId")
        str = []
        for i in Select(select).options:
            str.append(i.get_attribute("innerText"))
        option = Select(select).all_selected_options
        if len(option) > 0:
            superior = option[0].get_attribute("innerText")
        else:
            superior = None
        curdept = self.driver.find_element_by_name("bssDept.name").get_attribute("value")
        q = list(filter(lambda x: x != curdept and x != superior, str))
        Select(select).select_by_visible_text(q[0])

    def setself(self):
        curdept = self.driver.find_element_by_name("bssDept.name").get_attribute("value")
        select = self.driver.find_element_by_name("bssDeptSelect.parentId")
        Select(select).select_by_visible_text(curdept)
        time.sleep(1)

    def deptstatus(self, type = 1):
        trs = self.driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        q = []
        p = []
        depname = []
        for tr in trs:
            tds = tr.find_elements_by_tag_name("td")
            depname.append(tds[2].text)
        for tr in trs:
            tds = tr.find_elements_by_tag_name("td")
            if tds[1].text not in depname and tds[4].text == "未删除":
                q.append(tr)
            if tds[1].text in depname and tds[4].text == "未删除":
                p.append(tr)
        if type == 1:
            if len(q) > 0:
                q[0].find_element_by_class_name("checkbox").click()
                time.sleep(1)
        if type == 2:
            if len(p) > 0:
                p[0].find_element_by_class_name("checkbox").click()
                time.sleep(1)
            else:
                print("Please set superior department first")


    def modify(self):
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(2)

    def table(self):
        q = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr/td[2]"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg

    def delete_dept(self):
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[3]/i").click()
        time.sleep(2)

    def multi_select(self):
        checkbox1 = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        checkbox2 = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox1).click()
        self.driver.find_element_by_xpath(checkbox2).click()


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def name(self):
        msg = self.driver.find_element_by_id("bssDept.name-error").text
        return msg

    def companyname(self):
        msg = self.driver.find_element_by_id("bssDept-error").text
        return msg

    def number(self):
        msg = self.driver.find_element_by_id("bssDept.orderNum-error").text
        return msg














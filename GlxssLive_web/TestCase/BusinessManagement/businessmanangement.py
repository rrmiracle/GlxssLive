import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class BusinessManagement:
    def __init__(self, driver):
        self.driver = driver

    def goto_businessmanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("企业管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(0)
        contact = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]"
        return self.driver.find_element_by_xpath(contact).text

    def tagname(self):
        try:
            name = self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/h5").text
            return name
        except NoSuchElementException:
            name = self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div[1]/h5").text
            return name

    def add_company(self):
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[1]/i").click()

    def modify_company(self):
        checkbox = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(1)

    def clear(self, type):
        if type == 1:
            self.driver.find_element_by_name("bssBusiness.name").clear()
        if type == 2:
            self.driver.find_element_by_name("bssBusiness.address").clear()
        if type == 3:
            self.driver.find_element_by_name("userLimit").clear()

    def input(self, bsname, bsaddress, limit):
        self.driver.find_element_by_name("bssBusiness.name").send_keys(bsname)
        self.driver.find_element_by_name("bssBusiness.address").send_keys(bsaddress)
        self.driver.find_element_by_name("userLimit").send_keys(limit)

    def select_trade(self, type=""):
        self.driver.find_element_by_id("trade_chosen").click()
        time.sleep(1)
        if type == 1:
            self.driver.find_element_by_xpath(".//*[@id='trade_chosen']/div/ul/li[1]").click()
            time.sleep(1)
        elif type == 2:
            self.driver.find_element_by_xpath(".//*[@id='trade_chosen']/div/ul/li[2]").click()
            time.sleep(1)
        elif type == 3:
            self.driver.find_element_by_xpath(".//*[@id='trade_chosen']/div/ul/li[3]").click()
            time.sleep(1)
        else:
            self.driver.find_element_by_xpath(".//*[@id='trade_chosen']/div/ul/li[4]").click()
            time.sleep(1)

    def select_type(self, type=""):
        self.driver.find_element_by_id("type_chosen").click()
        time.sleep(1)
        if type == 1:
            self.driver.find_element_by_xpath(".//*[@id='type_chosen']/div/ul/li[1]").click()
            time.sleep(1)
        elif type == 2:
            self.driver.find_element_by_xpath(".//*[@id='type_chosen']/div/ul/li[2]").click()
            time.sleep(1)
        elif type == 3:
            self.driver.find_element_by_xpath(".//*[@id='type_chosen']/div/ul/li[3]").click()
            time.sleep(1)
        elif type == 4:
            self.driver.find_element_by_xpath(".//*[@id='type_chosen']/div/ul/li[4]").click()
            time.sleep(1)
        else:
            self.driver.find_element_by_xpath(".//*[@id='type_chosen']/div/ul/li[5]").click()
            time.sleep(1)

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[8]/div/button").click()

    def back(self):
        self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[8]/div/a").click()
        time.sleep(1)

    def modify_trade(self):
        if self.driver.find_element_by_id("trade_chosen").text != "制作行业":
            self.select_trade("1")
        else:
            self.select_trade("2")

    def modify_type(self):
        if self.driver.find_element_by_id("type_chosen").text != "创业公司":
            self.select_type("1")
        else:
            self.select_type("1")

    def modify_contact(self, currentcontact):
        select = self.driver.find_element_by_name("selected")
        str = select.text
        q = str.split('\n')
        a = list(filter(lambda x:x!=currentcontact, q))
        if len(a) > 0:
            Select(select).select_by_visible_text(a[0])
        else:
            print("There is no other contact")
            Select(select).select_by_visible_text(currentcontact)

    def recovery(self, currentcontact):
        select = self.driver.find_element_by_name("selected")
        Select(select).select_by_visible_text(currentcontact)

    def delete_company(self):
        checkbox = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[3]/i").click()
        time.sleep(1)

    def table(self):
        q = ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr/td[7]"
        msg = self.driver.find_element_by_xpath(q).get_attribute("innerText")
        return msg

    def unselect(self):
        self.driver.find_element_by_xpath(".//*[@id='bssapp']/div/div/div/div[1]/div/a[2]/i").click()


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def companyname(self):
        msg = self.driver.find_element_by_id("bssBusiness.name-error").text
        return msg

    def address(self):
        msg = self.driver.find_element_by_id("bssBusiness.address-error").text
        return msg

    def trade(self):
        msg = self.driver.find_element_by_id("trade-error").text
        return msg

    def userlimit(self):
        msg = self.driver.find_element_by_id("userLimit-error").text
        return msg

    def type(self):
        msg = self.driver.find_element_by_id("type-error").text
        return msg





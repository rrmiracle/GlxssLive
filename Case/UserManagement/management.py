import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Management:
    def __init__(self, driver):
        self.driver = driver

    def goto_usermanagement(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("用户管理").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[3]/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.switch_to.frame(1)

    def add_user(self):
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[1]/i").click()

    def modify_user(self):
        checkbox = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[2]/i").click()
        time.sleep(2)

    def delete_user(self):
        checkbox = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[3]/i").click()
        time.sleep(2)

    def unselect(self):
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[2]/i").click()

    def multiselect(self):
        checkbox1 = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        checkbox2 = ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span"
        self.driver.find_element_by_xpath(checkbox1).click()
        self.driver.find_element_by_xpath(checkbox2).click()
        self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/div/a[2]/i").click()

    def tagname(self):
        try:
            name = self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[1]/h5").text
            return name
        except NoSuchElementException:
            name = self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div[1]/h5").text
            return name

    def input(self, username, password="", comfirmpassword="", email="", mobile="", description=""):
        self.driver.find_element_by_name("userManager.username").send_keys(username)
        self.driver.find_element_by_name("userManager.introduce").send_keys(description)
        try:
            self.driver.find_element_by_name("password").send_keys(password)
            self.driver.find_element_by_name("confirm").send_keys(comfirmpassword)
            self.driver.find_element_by_name("userManager.email").send_keys(email)
            self.driver.find_element_by_name("phone").send_keys(mobile)
        except NoSuchElementException as e:
            pass

    def select_type(self, type):
        self.driver.find_element_by_xpath(".//*[@id='userType_chosen']/a/span").click()
        time.sleep(1)
        if type == 1:
            self.driver.find_element_by_xpath(".//*[@id='userType_chosen']/div/ul/li[1]").click()
        elif type == 2:
            self.driver.find_element_by_xpath(".//*[@id='userType_chosen']/div/ul/li[2]").click()
        else:
            self.driver.find_element_by_xpath(".//*[@id='userType_chosen']/div/ul/li[3]").click()
        time.sleep(1)

    def select_company(self):
        self.driver.find_element_by_xpath(".//*[@id='bsType_chosen']/a/span").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='bsType_chosen']/div/ul/li[1]").click()
        time.sleep(1)

    def type(self):
        q = self.driver.find_element_by_xpath(".//*[@id='userType_chosen']/a/span").get_attribute("innerText")
        print(q)
        if q == "非专家":
            self.select_type(2)
            if self.driver.find_element_by_name("specialtyCheckList").is_selected():
                pass
            else:
                self.driver.find_element_by_name("specialtyCheckList").click()
        elif q == "坐席专家":
            self.select_type(1)
        elif q == "非坐席专家":
            self.select_type(2)

    def department(self):
        q = self.driver.find_element_by_xpath(".//*[@id='deptType_chosen']/a/span")
        if q.get_attribute("innerText") == "选择所属部门":
            q.click()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath(".//*[@id='deptType_chosen']/div/ul/li[1]").click()
            except NoSuchElementException:
                print("No department")
        else:
            q.click()
            time.sleep(1)
            p = self.driver.find_element_by_xpath(".//*[@id='deptType_chosen']/div/ul/li[1]")
            if q.get_attribute("innerText") == p.get_attribute("innerText"):
                try:
                    self.driver.find_element_by_xpath(".//*[@id='deptType_chosen']/div/ul/li[2]").click()
                except NoSuchElementException:
                    print("No other department")
            else:
                p.click()

    def role(self):
        self.driver.find_element_by_name("userCheckList").click()

    def special(self):
        try:
            q = self.driver.find_elements_by_name("specialtyCheckList")
            if len(q) > 1:
                if q[0].is_selected():
                    if q[1].is_selected():
                        q[0].click()
                    else:
                        q[0].click()
                        q[1].click()
                else:
                    if q[1].is_selected():
                        q[0].click()
                        q[1].click()
                    else:
                        q[0].click()
            else:
                if q[0].is_selected():
                    print("Can't change special")
                else:
                    q[0].click()
        except NoSuchElementException:
            p = self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[9]/div/ul/li/div/span")
            if p.get_attribute("innerText") == "暂无数据":
                print("No special defined")

    def clear(self, mark):
        if mark == 1:
            self.driver.find_element_by_name("userManager.username").clear()
        elif mark == 2:
            time.sleep(1)
            js = "var q = document.getElementsByName('userManager.introduce')[0]; return q.value"
            q = len(self.driver.execute_script(js))
            for i in range(0, q):
                self.driver.find_element_by_name("userManager.introduce").send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def save(self):
        try:
            self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[13]/div/button").click()
        except NoSuchElementException:
            self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[11]/div/button").click()

    def back(self):
        try:
            self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[13]/div/a").click()
            time.sleep(1)
        except NoSuchElementException:
            self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[11]/div/a").click()
            time.sleep(1)

    def confirm(self):
        self.driver.find_element_by_xpath("html/body/div[3]/div[7]/button[2]").click()

    def cancel(self):
        self.driver.find_element_by_xpath("html/body/div[3]/div[7]/button[1]").click()

    def table(self):
        q = self.driver.find_element_by_xpath(".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[7]")
        email = q.get_attribute("innerText")
        return email

    def status(self):
        bsname = self.driver.find_element_by_name("userManager.bsName")
        email = self.driver.find_element_by_name("userManager.email")
        phone = self.driver.find_element_by_name("phone")
        return bsname.get_attribute("disabled"), email.get_attribute("disabled"), phone.get_attribute("disabled")

    def specialuncheck(self):
        try:
            q = self.driver.find_element_by_xpath(".//*[@id='commentForm']/div[9]/div/ul/li/div/span").text
            if q == "暂无数据":
                print("There is no special")
        except NoSuchElementException:
            m = self.driver.find_elements_by_name("specialtyCheckList")
            for i in range(0, len(m)):
                if m[i].is_selected() is True:
                    m[i].click()


class Errormsg:
    def __init__(self, driver):
        self.driver = driver

    def username(self):
        msg = self.driver.find_element_by_id("userManager.username-error").text
        return msg

    def type(self):
        msg = self.driver.find_element_by_id("userType-error").text
        return msg

    def company(self):
        msg = self.driver.find_element_by_id("bsType-error").text
        return msg

    def password(self):
        msg = self.driver.find_element_by_id("psd-error").text
        return msg

    def confirmpsd(self):
        msg = self.driver.find_element_by_id("confirm-error").text
        return msg

    def email(self):
        msg = self.driver.find_element_by_id("userManager.email-error").text
        return msg

    def mobile(self):
        msg = self.driver.find_element_by_id("phone-error").text
        return msg










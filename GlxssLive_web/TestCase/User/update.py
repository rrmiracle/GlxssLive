import os
import time
from selenium.common.exceptions import NoSuchElementException
from Case.User.Data import Data


class Update:
    def __init__(self, driver):
        self.driver = driver

    def goto_profile(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[1]/div[1]/a/span/span[2]/b").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[1]/div[1]/ul/li[1]/a").click()
        time.sleep(3)
        self.driver.switch_to.frame(0)

    def tagname(self):
        try:
            msg = self.driver.find_element_by_xpath(".//*[@id='perapp']/div/div/div/div[1]/h5").text
            return msg
        except NoSuchElementException:
            try:
                msg1 = self.driver.find_element_by_xpath(".//*[@id='perapp']/div/div/div[1]/h5").text
                return msg1
            except NoSuchElementException:
                print("no such element")

    def update_avatar(self):
        element = self.driver.find_element_by_xpath(".//*[@id='personalForm']/div[1]/div/div[2]/p[2]/input")
        element.click()
        time.sleep(3)
        os.system("D:\\upload.exe")

    def update_name(self):
        u = Data
        self.clear()
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(u.email)

    def update_password(self, oldpassword, newpassword, confirmpassword):
        self.modifypassword()
        time.sleep(2)
        self.driver.find_element_by_name("password").send_keys(oldpassword)
        self.driver.find_element_by_name("newpassword").send_keys(newpassword)
        self.driver.find_element_by_name("confirm").send_keys(confirmpassword)
        self.modify()
        time.sleep(2)

    def clear(self):
        self.driver.find_element_by_name("username").clear()

    def errormsg(self):
        try:
            msg = self.driver.find_element_by_id("username-error").text
            return msg
        except NoSuchElementException:
            try:
                msg1 = self.driver.find_element_by_id("password-error").text
                msg2 = self.driver.find_element_by_id("newPsd-error").text
                msg3 = self.driver.find_element_by_id("confirm-error").text
                return msg1, msg2, msg3
            except NoSuchElementException:
                try:
                    msg3 = self.driver.find_element_by_id("confirm-error").text
                    return msg3
                except NoSuchElementException:
                    msg2 = self.driver.find_element_by_id("newPsd-error").text
                    return msg2

    def save(self):
        self.driver.find_element_by_xpath(".//*[@id='personalForm']/div[6]/div/div[2]/button").click()
        time.sleep(2)

    def confirm(self):
        self.driver.find_element_by_xpath("html/body/div[3]/div[7]/button[2]").click()
        time.sleep(2)

    def result(self):
        return self.driver.find_element_by_xpath("html/body/div[3]/h2").text

    def modifypassword(self):
        self.driver.find_element_by_xpath(".//*[@id='personalForm']/div[3]/div/div[2]/p[3]/a").click()
        time.sleep(2)

    def modify(self):
        self.driver.find_element_by_xpath(".//*[@id='passwordForm']/div[5]/div/button[1]").click()

    def OK(self):
        time.sleep(2)
        self.driver.find_element_by_class_name("confirmClick").click()
        time.sleep(2)


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        u = Data
        self.driver.get(u.url)
        time.sleep(5)
        uap = UsernameAndPassword(self.driver)
        uap.input(u.username, u.password)
        time.sleep(10)
        #手动输入验证码
        uap.confirm()


class UsernameAndPassword:
    def __init__(self, driver):
        self.driver = driver

    def input(self, username, password, code=""):
        self.driver.find_element_by_name("usernamee").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("codee").send_keys(code)

    def inputr(self, businesscode, email, username, password, passwordcfm, code=""):
        self.driver.find_element_by_name("businessCode").send_keys(businesscode)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("ok").send_keys(passwordcfm)
        self.driver.find_element_by_name("captcha").send_keys(code)

    def inputf(self, email, password="", passwordcfm="", code=""):
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("ok").send_keys(passwordcfm)
        self.driver.find_element_by_xpath(".//*[@id='registerForm']/div[2]/input").send_keys(code)

    def confirm(self):
        u = Data
        if self.driver.current_url == u.login_url:
            self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        elif self.driver.current_url == u.register_url or self.driver.current_url == u.fpassword_url:
            self.driver.find_element_by_xpath(".//*[@id='registerForm']/button").click()
        else:
            return print("can not find the button")

    def send(self):
        self.driver.find_element_by_xpath(".//*[@id='registerForm']/div[2]/button").click()

    def errormsg(self):
        u = Data
        if self.driver.current_url == u.login_url:
            msg = self.driver.find_element_by_xpath(".//*[@id='loginForm']/h4").text
            return msg
        elif self.driver.current_url == u.register_url or self.driver.current_url == u.fpassword_url:
            msg = self.driver.find_element_by_xpath(".//*[@id='registerForm']/h4").text
            return msg
        else:
            return print("can not find the text")

    def popmsg(self):
        msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        return msg

    def notification(self):
        msg = self.driver.find_element_by_xpath("html/body/div[3]/p").get_attribute("innerText")
        return msg

    def clear(self):
        self.driver.find_element_by_name("email").clear()

    def refresh(self):
        self.driver.find_element_by_class_name("form-code").click()

    def gotoregister(self):
        self.driver.find_element_by_link_text("立即注册»").click()

    def gotofp(self):
        self.driver.find_element_by_link_text("忘记密码»").click()

    def logout(self):
        self.driver.find_element_by_xpath(".//*[@id='page-wrapper']/div[1]/nav/div/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[1]/div[1]/a/span/span[2]/b").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(".//*[@id='side-menu']/li[1]/div[1]/ul/li[3]/a").click()
        time.sleep(3)
import time
import unittest
from selenium import webdriver
import random
import os


class Login:
    def __init__(self, driver):
        self.driver = driver

    def input(self, username, password, code=""):
        self.driver.find_element_by_name("usernamee").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("codee").send_keys(code)

    def confirm(self):
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()

    def login(self):
        self.driver.get("https://jdev.llvision.com")
        time.sleep(5)
        self.input("zhuanjia3@qq.com", "123456")
        time.sleep(10)
        #手动输入验证码
        self.confirm()


class test_stability(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("start")

    def tearDown(self):
        # self.driver.quit()
        print("finish")

    def test_stability(self):
        l = Login(self.driver)
        l.login()
        time.sleep(20)
        xpath = ".//*[@id='content-main']/div/div/div/div/div/div/div[2]/div/div[1]/h5"
        q = self.driver.find_element_by_xpath(xpath)
        while q.get_attribute("innerText") != "未接入会话":
            m = ".//*[@id='content-main']/div/div/div/div/div/div/div[2]/div/div[3]/form/div[1]/textarea"
            seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
            s = []
            for i in range(8):
                s.append(random.choice(seed))
            self.driver.find_element_by_xpath(m).send_keys(s)
            t = ".//*[@id='content-main']/div/div/div/div/div/div/div[2]/div/div[3]/form/div[2]/a[2]/i"
            self.driver.find_element_by_xpath(t).click()
            time.sleep(60)
            p = ".//*[@id='content-main']/div/div/div/div/div/div/div[2]/div/div[3]/form/div[2]/a[1]/input"
            self.driver.find_element_by_xpath(p).click()
            time.sleep(3)
            os.system("D:\\upload1.exe")
            time.sleep(57)


if __name__ == "__main__":
    unittest.main()




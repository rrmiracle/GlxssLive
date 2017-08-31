# coding=utf-8
from selenium import webdriver
import unittest
from .Data import Data
import time


class Test004_loginerror3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_loginerror3(self):
        u = Data
        self.driver.get(u.url)
        time.sleep(3)
        self.driver.find_element_by_name("usernamee").send_keys(u.username)
        self.driver.find_element_by_name("passwordd").send_keys(u.password)
        self.driver.find_element_by_name("codee").send_keys("aaaaa")
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath(".//*[@id='loginForm']/h4").text
        self.assertEqual(message, "登录：验证码不正确")
        # self.assertEqual(self.driver.current_url, "http://dev.llvision.com:25008/index.html")

if __name__ == "__main__":
    unittest.main()
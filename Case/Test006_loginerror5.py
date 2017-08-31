# coding=utf-8
from selenium import webdriver
import unittest
from .Data import Data
import time


class Test006_loginerror5(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_loginerror5(self):
        u = Data
        self.driver.get(u.url)
        time.sleep(3)
        self.driver.find_element_by_name("usernamee").send_keys(u.username_deleted)
        self.driver.find_element_by_name("passwordd").send_keys(u.password_deleted)
        time.sleep(10)
        # 手动输入验证码
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath(".//*[@id='loginForm']/h4").text
        self.assertEqual(message, "登录：账号已被锁定,请联系管理员")

if __name__ == "__main__":
    unittest.main()
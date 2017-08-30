# coding=utf-8
from selenium import webdriver
import unittest
from Case import Data
import time


class Test001_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_Case1(self):
        u = Data.Data
        self.driver.get(u.url)
        time.sleep(3)
        self.driver.find_element_by_name("usernamee").send_keys(u.username)
        self.driver.find_element_by_name("passwordd").send_keys(u.password)
        time.sleep(5)
        # 手动输入验证码
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        time.sleep(3)
        # try:
        #     self.assertEqual(self.driver.current_url, "http://dev.llvision.com:25008/index.html")
        #     print("Test Pass")
        # except Exception as e:
        #     print("Test Fail", format(e))
        self.assertEqual(self.driver.current_url, "http://dev.llvision.com:25008/index.html")

if __name__ == "__main__":
    unittest.main()
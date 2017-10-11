# coding=utf-8
import time
import unittest

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test001_Loginandlogout(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.url)
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_login(self):
        u = Data
        time.sleep(5)
        uap = UsernameAndPassword(self.driver)
        uap.input(u.username, u.password)
        time.sleep(10)
        # 手动输入验证码
        uap.confirm()
        time.sleep(3)
        # try:
        #     self.assertEqual(self.driver.current_url, "http://dev.llvision.com:25008/index.html")
        #     print("Test Pass")
        # except Exception as e:
        #     print("Test Fail", format(e))
        self.assertEqual(self.driver.current_url, u.main_url)
        uap.logout()
        self.assertEqual(self.driver.current_url, u.login_url)



if __name__ == "__main__":
    unittest.main()
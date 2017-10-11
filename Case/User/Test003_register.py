# coding=utf-8
import time
import unittest

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test003_Register(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.url)
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_register(self):
        u = Data
        time.sleep(5)
        uap = UsernameAndPassword(self.driver)
        uap.gotoregister()
        time.sleep(3)
        self.assertEqual(self.driver.current_url, u.register_url)
        uap.inputr(u.businesscode, u.email, u.name, u.password, u.password)
        time.sleep(10)
        uap.confirm()
        time.sleep(3)
        self.assertEqual(self.driver.current_url, u.sendemail_url)


if __name__ == "__main__":
    unittest.main()
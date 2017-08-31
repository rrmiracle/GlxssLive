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
        self.driver.find_element_by_link_text("立即注册»").click()
        time.sleep(3)
        self.assertEqual(self.driver.current_url, u.register_url)

if __name__ == "__main__":
    unittest.main()
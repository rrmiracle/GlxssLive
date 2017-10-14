from .driver import browser
import unittest
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.Page_obj.loginPage import login
import time


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(Data.url)
        time.sleep(5)
        print("Start=====")

    def tearDown(self):
        self.driver.quit()
        print("=====Finish")


class MyTest_login(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(Data.url)
        time.sleep(5)
        l = login(self.driver)
        l.login(Data.username, Data.password)
        print("Start=====")

    def tearDown(self):
        self.driver.quit()
        print("=====Finish")
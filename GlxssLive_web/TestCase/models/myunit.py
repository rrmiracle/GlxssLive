from .driver import browser
import unittest
from GlxssLive_web.Data.Data import Data


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(Data.url)
        self.driver.implicitly_wait(5)
        print("Start=====")

    def tearDown(self):
        self.driver.quit()
        print("=====Finish")
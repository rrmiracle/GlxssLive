from selenium import webdriver
from Case.User.update import Login
import unittest
from .sessionmanangement import SessionManagement
import time


class Test046_Check(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_check(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        self.assertEqual(man.tagname(), "会话管理")
        man.check()
        self.assertEqual(man.tagname(), "资源管理")
        time.sleep(5)
        man.back()
        self.assertEqual(man.tagname(), "会话管理")


if __name__ == "__main__":
    unittest.main()



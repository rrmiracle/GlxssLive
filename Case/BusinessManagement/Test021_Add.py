from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login, UsernameAndPassword
import unittest
from .businessmanangement import BusinessManagement


class Test021_Add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_add(self):
        u = Data
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        self.assertEqual(man.tagname(), "企业管理")
        man.add_company()
        self.assertEqual(man.tagname(), "企业管理-新增")
        man.input(u.name, u.name, "9999")
        man.select_trade()
        man.select_type()
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "您不能添加企业")

    def test_back(self):
        u = Data
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.add_company()
        man.input(u.name, u.name, "9999")
        man.select_trade()
        man.select_type()
        man.back()
        self.assertEqual(man.tagname(), "企业管理")


if __name__ == "__main__":
    unittest.main()



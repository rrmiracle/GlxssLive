from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login
import unittest
from .businessmanangement import BusinessManagement, Errormsg
import random


class Test025_AddError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        self.assertEqual(man.tagname(), "企业管理")
        man.add_company()
        self.assertEqual(man.tagname(), "企业管理-新增")
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.companyname(), "不能为空哦")
        self.assertEqual(error.address(), "不能为空哦")
        self.assertEqual(error.trade(), "不能为空哦")
        self.assertEqual(error.userlimit(), "不能为空哦")
        self.assertEqual(error.type(), "不能为空哦")

    def test_invalid(self):
        u = Data
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.add_company()
        man.input(u.name, u.name, random.choice(["-1", "1.1", "A", "中文"]))
        man.select_type()
        man.select_trade()
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.userlimit(), "请以数字填写")


if __name__ == "__main__":
    unittest.main()



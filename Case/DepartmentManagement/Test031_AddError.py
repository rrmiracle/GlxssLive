from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .depmanagement import DepartmentManagement, Errormsg
from Case.BusinessManagement.businessmanangement import BusinessManagement
from Case.User.Data import Data
import random


class Test031_AddError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "部门管理")
        man1.add_company()
        self.assertEqual(man1.tagname(), "部门管理-新增")
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")
        self.assertEqual(error.companyname(), "不能为空哦")
        self.assertEqual(error.number(), "不能为空哦")

    def test_exist(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input("1", "1")
        man.select()
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "数据库中已存在该记录")

    def test_invalid(self):
        u = Data
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input(u.depname, random.choice(["1.1", "中文"]))
        man.select()
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "未知异常，请联系管理员")


if __name__ == "__main__":
    unittest.main()



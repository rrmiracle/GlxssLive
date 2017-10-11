from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login, Update
import unittest
from .depmanagement import DepartmentManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test027_Add(unittest.TestCase):
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
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "部门管理")
        man1.add_company()
        self.assertEqual(man1.tagname(), "部门管理-新增")
        man.input(u.depname, "1")
        man.select()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input(u.depname, "1")
        man.select()
        man.back()
        self.assertEqual(man1.tagname(), "部门管理")


if __name__ == "__main__":
    unittest.main()



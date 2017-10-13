from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login, Update
import unittest
from Case.DepartmentManagement.depmanagement import DepartmentManagement
from .specialmanagement import SpecialManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test040_Add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_add(self):
        u = Data()
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "专业管理")
        man1.add_company()
        self.assertEqual(man1.tagname(), "企业专业表-新增")
        man.input(u.specialname)
        man2 = DepartmentManagement(self.driver)
        man2.select()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data()
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input(u.specialname)
        man2 = DepartmentManagement(self.driver)
        man2.select()
        man.back()
        self.assertEqual(man1.tagname(), "专业管理")


if __name__ == "__main__":
    unittest.main()



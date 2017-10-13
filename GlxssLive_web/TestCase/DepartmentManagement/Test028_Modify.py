from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .depmanagement import DepartmentManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test028_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "部门管理")
        man1.modify_company()
        self.assertEqual(man1.tagname(), "部门管理-修改")
        man.clear(1)
        man.input("update", "")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifynumber(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        man.clear(2)
        man.input("", "2")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifydept(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man.deptstatus()
        man.modify()
        man.dept()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        self.assertEqual(man.status(), False)
        man.back()
        self.assertEqual(man1.tagname(), "部门管理")


if __name__ == "__main__":
    unittest.main()



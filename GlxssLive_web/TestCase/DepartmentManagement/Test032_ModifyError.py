from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .depmanagement import DepartmentManagement, Errormsg
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test032_ModifyError(unittest.TestCase):
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
        man1.modify_company()
        self.assertEqual(man1.tagname(), "部门管理-修改")
        man.clear(1)
        man.clear(2)
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")
        self.assertEqual(error.number(), "不能为空哦")

    def test_exist(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        man.clear(1)
        man.input("1", "")
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "数据库中已存在该记录")

    def test_setself(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man.deptstatus()
        man.modify()
        man.setself()
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "不可以指定本部门为上级部门")

    def test_hasbranch(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man.deptstatus(2)
        man.modify()
        man.dept()
        man.save()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "该部门有子部门，无法修改上级部门")


if __name__ == "__main__":
    unittest.main()



from selenium import webdriver
from Case.User.update import Login
import unittest
from .rolemanagement import RoleManagement, Errormsg


class Test019_AddError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        man.add_role()
        self.assertEqual(man.tagname(), "角色管理-新增")
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.rolename(), "不能为空哦")
        self.assertEqual(error.company(), "不能为空哦")
        self.assertEqual(error.note(), "不能为空哦")


if __name__ == "__main__":
    unittest.main()



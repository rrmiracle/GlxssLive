from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login, Update
import unittest
from .rolemanagement import RoleManagement


class Test015_Add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_addrole(self):
        u = Data
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        man.add_role()
        self.assertEqual(man.tagname(), "角色管理-新增")
        man.input(u.rolename, "备注")
        man.select_company()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        man.add_role()
        self.assertEqual(man.tagname(), "角色管理-新增")
        man.input(u.rolename, "备注")
        man.select_company()
        man.back()
        self.assertEqual(man.tagname(), "角色管理")


if __name__ == "__main__":
    unittest.main()



from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .rolemanagement import RoleManagement


class Test016_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        man.modify_role()
        self.assertEqual(man.tagname(), "角色管理-修改")
        man.clear(1)
        man.input("update", "")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifydescription(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        man.modify_role()
        man.clear(2)
        man.input("", "update")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifytype(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        man.modify_role()
        man.checkbox()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        man.modify_role()
        man.clear(1)
        man.clear(2)
        man.back()
        self.assertEqual(man.tagname(), "角色管理")


if __name__ == "__main__":
    unittest.main()



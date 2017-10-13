from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .rolemanagement import RoleManagement
from Case.UserManagement.management import Management


class Test017_Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_deleterole(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        man.delete_role()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.confirm()
        self.assertEqual(up.result(), "删除成功")

    def test_cancle(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        self.assertEqual(man.tagname(), "角色管理")
        a = man.table()
        man.delete_role()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.cancel()
        self.assertEqual(a, man.table())


if __name__ == "__main__":
    unittest.main()



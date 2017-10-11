from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .rolemanagement import RoleManagement
from Case.UserManagement.management import Management


class Test018_ListError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_unselect(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        man1 = Management(self.driver)
        man1.unselect()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "请选择一条数据")

    def test_multiselect(self):
        man = RoleManagement(self.driver)
        man.goto_rolemanagement()
        man1 = Management(self.driver)
        man1.multiselect()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "只能选择一条数据")


if __name__ == "__main__":
    unittest.main()



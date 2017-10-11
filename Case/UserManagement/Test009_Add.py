from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login, Update
import unittest
from .management import Management


class Test009_Add(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_adduser(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        self.assertEqual(man.tagname(), "用户管理")
        man.add_user()
        self.assertEqual(man.tagname(), "用户管理-新增")
        man.input(u.name, u.password, u.password, u.email, u.mobile, "test description")
        man.select_type(1)
        man.select_company()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        self.assertEqual(man.tagname(), "用户管理-新增")
        man.input(u.name, u.password, u.password, u.email, u.mobile, "test description")
        man.select_type(1)
        man.select_company()
        man.back()
        self.assertEqual(man.tagname(), "用户管理")


if __name__ == "__main__":
    unittest.main()



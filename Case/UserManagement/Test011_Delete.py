from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .management import Management


class Test011_Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_deleteuser(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        self.assertEqual(man.tagname(), "用户管理")
        man.delete_user()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man.confirm()
        self.assertEqual(up.result(), "删除成功")

    def test_cancle(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        self.assertEqual(man.tagname(), "用户管理")
        a = man.table()
        man.delete_user()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man.cancel()
        self.assertEqual(a, man.table())


if __name__ == "__main__":
    unittest.main()



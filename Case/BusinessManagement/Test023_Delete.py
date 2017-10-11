from selenium import webdriver
from Case.User.update import Login, Update, UsernameAndPassword
import unittest
from .businessmanangement import BusinessManagement
from Case.UserManagement.management import Management


class Test023_Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_deleterole(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        self.assertEqual(man.tagname(), "企业管理")
        man.delete_company()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.confirm()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "您不能删除企业")

    def test_cancle(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        self.assertEqual(man.tagname(), "企业管理")
        a = man.table()
        man.delete_company()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.cancel()
        self.assertEqual(a, man.table())


if __name__ == "__main__":
    unittest.main()



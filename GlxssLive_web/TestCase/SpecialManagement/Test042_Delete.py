from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .specialmanagement import SpecialManagement
from Case.UserManagement.management import Management
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test042_Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_deletedept(self):
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "专业管理")
        man1.delete_company()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.confirm()
        self.assertEqual(up.result(), "删除成功")

    def test_cancle(self):
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        a = man.table()
        man1 = BusinessManagement(self.driver)
        man1.delete_company()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.cancel()
        self.assertEqual(a, man.table())


if __name__ == "__main__":
    unittest.main()



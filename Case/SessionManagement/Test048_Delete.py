from selenium import webdriver
from Case.User.update import Login, Update, UsernameAndPassword
from Case.UserManagement.management import Management
import unittest
from .sessionmanangement import SessionManagement


class Test048_Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_delete(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        self.assertEqual(man.tagname(), "会话管理")
        man.delete()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.confirm()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "无权删除")

    def test_cancle(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        a = man.table()
        man.delete()
        man1 = Management(self.driver)
        man1.cancel()
        self.assertEqual(man.table(), a)


if __name__ == "__main__":
    unittest.main()



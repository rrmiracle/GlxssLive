from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .sessionmanangement import SessionManagement


class Test049_ListError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_unselect(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        man.uncheck()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "请选择一条数据")

    def test_multiselect(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        man.multi_select()
        man.uncheck()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "只能选择一条数据")


if __name__ == "__main__":
    unittest.main()



from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .businessmanangement import BusinessManagement


class Test024_ListError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_unselect(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.unselect()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "请选择一条数据")


if __name__ == "__main__":
    unittest.main()



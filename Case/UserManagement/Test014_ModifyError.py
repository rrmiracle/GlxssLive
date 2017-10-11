from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .management import Management, Errormsg
import time


class Test014_ModifyError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.clear(1)
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.username(), "不能为空哦")

    def test_nospecial(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.select_type(2)
        man.specialuncheck()
        man.save()
        uap = UsernameAndPassword(self.driver)
        time.sleep(1)
        self.assertEqual(uap.notification(), "专业不能为空！")


if __name__ == "__main__":
    unittest.main()



from selenium import webdriver
from Case.User.update import Login
import unittest
from .sessionmanangement import SessionManagement, Errormsg


class Test050_ModifyError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        self.assertEqual(man.tagname(), "会话管理")
        man.modify()
        self.assertEqual(man.tagname(), "会话管理-修改")
        man.clear(1)
        man.clear(2)
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")
        self.assertEqual(error.keyword(), "不能为空哦")


if __name__ == "__main__":
    unittest.main()



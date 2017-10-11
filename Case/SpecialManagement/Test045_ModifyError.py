from selenium import webdriver
from Case.User.update import Login
import unittest
from .specialmanagement import SpecialManagement, Errormsg
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test039_ModifyError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_blank(self):
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "专业管理")
        man1.modify_company()
        self.assertEqual(man1.tagname(), "企业专业表-修改")
        man.clear()
        man.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")


if __name__ == "__main__":
    unittest.main()



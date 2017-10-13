from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .specialmanagement import SpecialManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test041_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "专业管理")
        man1.modify_company()
        self.assertEqual(man1.tagname(), "企业专业表-修改")
        man.clear()
        man.input("update")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        man = SpecialManagement(self.driver)
        man.goto_specialmanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        self.assertEqual(man.status(), 'true')
        man.back()
        self.assertEqual(man1.tagname(), "专业管理")


if __name__ == "__main__":
    unittest.main()



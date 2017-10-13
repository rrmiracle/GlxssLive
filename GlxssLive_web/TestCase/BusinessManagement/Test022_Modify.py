from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .businessmanangement import BusinessManagement


class Test022_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        self.assertEqual(man.tagname(), "企业管理")
        man.modify_company()
        self.assertEqual(man.tagname(), "企业管理-修改")
        man.clear(1)
        man.input("update", "", "")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifyaddress(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.modify_company()
        man.clear(2)
        man.input("", "update", "")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifylimit(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.modify_company()
        man.clear(3)
        man.input("", "", "1111")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifytrade(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.modify_company()
        man.modify_trade()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifytype(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.modify_company()
        man.modify_type()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifycontact(self):
        man = BusinessManagement(self.driver)
        contact = man.goto_businessmanagement()
        man.modify_company()
        man.modify_contact(contact)
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")
        up.OK()
        man.modify_company()
        man.recovery(contact)
        man.save()

    def test_back(self):
        man = BusinessManagement(self.driver)
        man.goto_businessmanagement()
        man.modify_company()
        man.back()
        self.assertEqual(man.tagname(), "企业管理")


if __name__ == "__main__":
    unittest.main()



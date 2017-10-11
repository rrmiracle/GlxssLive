from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .management import Management


class Test010_Modify(unittest.TestCase):
    def setUp(self):
        # profile = r'C:\Users\rongrong\AppData\Roaming\Mozilla\Firefox\Profiles\guv0jxrf.default-1462336392420'
        # self.driver = webdriver.Firefox(profile)
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        self.assertEqual(man.tagname(), "用户管理")
        man.modify_user()
        self.assertEqual(man.tagname(), "用户管理-修改")
        self.assertEqual(man.status(), ('true', 'true', 'true'))
        man.clear(1)
        man.input("update")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifydescription(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.clear(2)
        man.input("", "", "", "", "", "update decription")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifytype(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.type()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifydepartment(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        self.assertEqual(man.tagname(), "用户管理")
        man.modify_user()
        man.department()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifyrole(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.role()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifyspecial(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.special()
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.modify_user()
        man.special()
        man.back()
        self.assertEqual(man.tagname(), "用户管理")


if __name__ == "__main__":
    unittest.main()



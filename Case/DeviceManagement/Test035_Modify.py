from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .devicemanagement import DeviceManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement
from Case.DepartmentManagement.depmanagement import DepartmentManagement


class Test035_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "设备管理")
        man1.modify_company()
        self.assertEqual(man1.tagname(), "设备管理-修改")
        man.clear(1)
        man.input("update", "", "")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifyversion(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        man.clear(2)
        man.input("", "1a", "")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifynumber(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        man.clear(3)
        man.input("", "", "update")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        self.assertEqual(man.status(), 'true')
        man2 = DepartmentManagement(self.driver)
        man2.back()
        self.assertEqual(man1.tagname(), "设备管理")


if __name__ == "__main__":
    unittest.main()



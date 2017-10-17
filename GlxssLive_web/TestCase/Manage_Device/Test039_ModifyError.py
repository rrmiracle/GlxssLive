from selenium import webdriver
from Case.User.update import Login
import unittest
from .devicemanagement import DeviceManagement, Errormsg
from Case.BusinessManagement.businessmanangement import BusinessManagement
from Case.DepartmentManagement.depmanagement import DepartmentManagement


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
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "设备管理")
        man1.modify_company()
        self.assertEqual(man1.tagname(), "设备管理-修改")
        man.clear(1)
        man.clear(2)
        man.clear(3)
        man2 = DepartmentManagement(self.driver)
        man2.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")
        self.assertEqual(error.number(), "不能为空哦")
        self.assertEqual(error.version(), "不能为空哦")

    def test_invalid(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.modify_company()
        man.clear(2)
        man.input("", "中文", "")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.version(), "数字和字母组合")


if __name__ == "__main__":
    unittest.main()



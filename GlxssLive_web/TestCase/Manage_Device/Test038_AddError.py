from selenium import webdriver
from Case.User.Data import Data
from Case.User.update import Login
import unittest
from Case.DepartmentManagement.depmanagement import DepartmentManagement
from .devicemanagement import DeviceManagement, Errormsg
from Case.BusinessManagement.businessmanangement import BusinessManagement


class Test038_AddError(unittest.TestCase):
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
        man1.add_company()
        self.assertEqual(man1.tagname(), "设备管理-新增")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.name(), "不能为空哦")
        self.assertEqual(error.company(), "不能为空哦")
        self.assertEqual(error.number(), "不能为空哦")
        self.assertEqual(error.version(), "不能为空哦")

    def test_invalid(self):
        u = Data
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input(u.devicename, "中文", "1")
        man2 = DepartmentManagement(self.driver)
        man2.save()
        error = Errormsg(self.driver)
        self.assertEqual(error.version(), "数字和字母组合")


if __name__ == "__main__":
    unittest.main()



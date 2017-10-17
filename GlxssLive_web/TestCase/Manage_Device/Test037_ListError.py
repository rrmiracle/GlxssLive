from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword
import unittest
from .devicemanagement import DeviceManagement
from Case.DepartmentManagement.depmanagement import DepartmentManagement


class Test037_ListError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_unselect(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = DepartmentManagement(self.driver)
        man1.modify()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "请选择一条数据")

    def test_multiselect(self):
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = DepartmentManagement(self.driver)
        man1.multi_select()
        man1.modify()
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "只能选择一条数据")


if __name__ == "__main__":
    unittest.main()



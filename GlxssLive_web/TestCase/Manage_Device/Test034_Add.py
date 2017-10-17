from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test034_Device_Add_P1(myunit.MyTest_login):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_add(self):
        u = Data()
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "设备管理")
        man1.add_company()
        self.assertEqual(man1.tagname(), "设备管理-新增")
        man.input(u.devicename, ''.join(u.version()), "1")
        man2 = DepartmentManagement(self.driver)
        man2.select()
        man2.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data()
        man = DeviceManagement(self.driver)
        man.goto_devicemanagement()
        man1 = BusinessManagement(self.driver)
        man1.add_company()
        man.input(u.devicename, ''.join(u.version()), "1")
        man2 = DepartmentManagement(self.driver)
        man2.select()
        man2.back()
        self.assertEqual(man1.tagname(), "设备管理")


if __name__ == "__main__":
    unittest.main()



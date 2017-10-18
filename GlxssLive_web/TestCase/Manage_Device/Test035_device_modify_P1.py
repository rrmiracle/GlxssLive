from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test035_Device_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改设备名称'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.name_clear()
        d.add_device("Update", "", "")
        self.assertEqual(d.company_status(), False)
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_device_name.jpg")

    def test_modify_version(self):
        '''修改设备版本号'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.version_clear()
        d.add_device("", "1a", "")
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_device_version.jpg")

    def test_modify_serial(self):
        '''修改设备序列号'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.serial_clear()
        d.add_device("", "", "Update")
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_device_serial.jpg")

    def test_back(self):
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.serial_clear()
        d.add_device("", "", "Update")
        d.add_back()
        self.assertEqual(d.verify(), True)
        function.screenshot(self.driver, "modify_device_back.jpg")


if __name__ == "__main__":
    unittest.main()



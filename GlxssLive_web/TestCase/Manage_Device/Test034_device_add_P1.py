from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test034_Device_Add_P1(myunit.MyTest_login):

    def test_device_add(self):
        '''添加设备'''
        D = Data()
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "设备管理-新增")
        d.add_device(Data.devicename, ''.join(D.version()), "1")
        d.select_company()
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "add_device.jpg")

    def test_device_add_back(self):
        '''添加设备并返回'''
        D = Data()
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "设备管理-新增")
        d.add_device(D.devicename, ''.join(D.version()), "1")
        d.select_company()
        d.add_back()
        self.assertEqual(d.verify(), True)
        function.screenshot(self.driver, "add_device_back.jpg")


if __name__ == "__main__":
    unittest.main()



from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test038_Device_Add_Error(myunit.MyTest_login):

    def test_device_add_error1(self):
        '''输入为空'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "设备管理-新增")
        d.add_save()
        self.assertEqual(d.error_name(), "不能为空哦")
        self.assertEqual(d.error_company(), "不能为空哦")
        self.assertEqual(d.error_serial(), "不能为空哦")
        self.assertEqual(d.error_version(), "不能为空哦")
        function.screenshot(self.driver, "add_device_blank.jpg")

    def test_device_add_error2(self):
        '''版本号输入无效'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "设备管理-新增")
        d.add_device(Data.devicename, "中文", "1")
        d.select_company()
        d.add_save()
        self.assertEqual(d.error_version(), "数字或字母")
        function.screenshot(self.driver, "add_device_serial_invalid.jpg")


if __name__ == "__main__":
    unittest.main()



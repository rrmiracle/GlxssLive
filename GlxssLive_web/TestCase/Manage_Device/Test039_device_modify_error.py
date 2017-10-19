from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test039_Device_Modify_Error(myunit.MyTest_login):

    def test_device_modify_error1(self):
        '''输入为空'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.name_clear()
        d.serial_clear()
        d.version_clear()
        d.add_save()
        self.assertEqual(d.error_name(), "不能为空哦")
        self.assertEqual(d.error_serial(), "不能为空哦")
        self.assertEqual(d.error_version(), "不能为空哦")
        function.screenshot(self.driver, "modify_device_blank.jpg")

    def test_device_modify_error2(self):
        '''版本号输入无效'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "设备管理-修改")
        d.serial_clear()
        d.add_device("", "中文", "")
        d.add_save()
        self.assertEqual(d.error_version(), "数字或字母")
        function.screenshot(self.driver, "modify_device_serial_invalid.jpg")


if __name__ == "__main__":
    unittest.main()



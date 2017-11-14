from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test036_Device_Delete_P1(myunit.MyTest_login):

    def test_delete(self):
        '''删除设备'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.delete_obj()
        self.assertEqual(d.result(), "您确定要删除这条信息吗")
        d.confirm()
        self.assertEqual(d.result(), "删除成功")
        function.screenshot(self.driver, "delete_device.jpg")

    def test_cancle(self):
        '''取消删除'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        s = d.serial_list()
        d.delete_obj()
        self.assertEqual(d.result(), "您确定要删除这条信息吗")
        d.cancel()
        self.assertEqual(d.serial_list(), s)
        function.screenshot(self.driver, "delete_device_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



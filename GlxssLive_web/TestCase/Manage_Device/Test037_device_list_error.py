from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.devicemanagePage import devicemanage
import unittest


class Test037_Device_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何设备'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.delete()
        self.assertEqual(d.reason(), "请选择一条数据")
        function.screenshot(self.driver, "device_unselect.jpg")

    def test_multiselect(self):
        '''选择两个设备'''
        d = devicemanage(self.driver)
        d.open_devicemanage()
        self.assertEqual(d.verify(), True)
        d.multi_select()
        d.modify()
        self.assertEqual(d.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "device_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()



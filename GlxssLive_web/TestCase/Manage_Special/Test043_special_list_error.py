from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest



class Test043_Special_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何专业'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.delete()
        self.assertEqual(s.reason(), "请选择一条数据")
        function.screenshot(self.driver, "spcial_unselect.jpg")

    def test_multiselect(self):
        '''选择两个专业'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.multi_select()
        s.modify()
        self.assertEqual(s.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "special_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()



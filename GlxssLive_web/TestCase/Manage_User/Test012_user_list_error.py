from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test012_User_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何用户'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.delete()
        self.assertEqual(u.reason(), "请选择一条数据")
        function.screenshot(self.driver, "user_unselect.jpg")

    def test_multiselect(self):
        '''选择两个用户'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.multi_select()
        u.modify()
        self.assertEqual(u.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "user_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()
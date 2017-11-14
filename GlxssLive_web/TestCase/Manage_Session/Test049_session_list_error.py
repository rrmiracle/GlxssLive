from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionmanagePage import sessionmanage
import unittest


class Test049_Session_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何会话'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.check()
        self.assertEqual(s.reason(), "请选择一条数据")
        function.screenshot(self.driver, "session_unselect.jpg")

    def test_multiselect(self):
        '''选择两条会话'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.multi_select()
        s.delete()
        self.assertEqual(s.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "session_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()



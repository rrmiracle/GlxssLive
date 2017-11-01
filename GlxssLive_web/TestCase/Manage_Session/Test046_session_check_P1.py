from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionmanagePage import sessionmanage
import unittest


class Test046_Session_Check_P1(myunit.MyTest_login):

    def test_session_check(self):
        '''查看会话详情'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.session_check()
        self.assertEqual(s.tagname(), "会话详情")
        function.screenshot(self.driver, "session_detail.jpg")
        s.check_back()
        self.assertEqual(s.verify(), True)
        function.screenshot(self.driver, "session_manage.jpg")


if __name__ == "__main__":
    unittest.main()



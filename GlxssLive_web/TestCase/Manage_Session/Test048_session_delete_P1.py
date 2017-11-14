from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionmanagePage import sessionmanage
import unittest


class Test048_Session_Delete_P1(myunit.MyTest_login):

    def test_session_delete(self):
        '''删除会话'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.delete_obj()
        self.assertEqual(s.result(), "您确定要删除这条信息吗")
        s.confirm()
        self.assertEqual(s.result(), "删除成功")
        function.screenshot(self.driver, "session_delete.jpg")

    def test_session_delete_cancle(self):
        '''取消删除会话'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        n = s.name_list()
        s.delete_obj()
        self.assertEqual(s.result(), "您确定要删除这条信息吗")
        s.cancel()
        self.assertEqual(s.name_list(), n)
        function.screenshot(self.driver, "session_delete_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



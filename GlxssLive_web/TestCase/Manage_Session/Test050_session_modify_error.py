from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionmanagePage import sessionmanage
import unittest


class Test050_Session_Modify_Error(myunit.MyTest_login):

    def test_blank(self):
        '''输入为空'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "会话管理-修改")
        s.name_clear()
        s.keyword_clear()
        s.modify_save()
        self.assertEqual(s.error_name(), "不能为空哦")
        self.assertEqual(s.error_keyword(), "不能为空哦")
        function.screenshot(self.driver, "session_modify_blank.jpg")


if __name__ == "__main__":
    unittest.main()



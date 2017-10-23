from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionmanagePage import sessionmanage
import unittest


class Test047_Sission_Modify_P1(myunit.MyTest_login):

    def test_session_modify_name(self):
        '''修改会话名称'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "会话管理-修改")
        s.name_clear()
        s.session_modify(Data.roomname, "Update")
        s.modify_save()
        self.assertEqual(s.success(), True)
        function.screenshot(self.driver, "session_modify_name.jpg")

    def test_session_modify_keyword(self):
        '''修改关键词'''
        u = Data()
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "会话管理-修改")
        s.keyword_clear()
        s.session_modify("", ''.join(u.version()))
        s.modify_save()
        self.assertEqual(s.success(), True)
        function.screenshot(self.driver, "session_modify_keyword.jpg")

    def test_back(self):
        '''修改并返回'''
        s = sessionmanage(self.driver)
        s.open_sessionmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "会话管理-修改")
        s.modify_back()
        self.assertEqual(s.verify(), True)
        function.screenshot(self.driver, "session_modify_back.jpg")


if __name__ == "__main__":
    unittest.main()



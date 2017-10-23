from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.sessionPage import session
import unittest


class Test051_Session_Status_P1(myunit.MyTest_login):

    def test_online(self):
        '''上线通知'''
        s = session(self.driver)
        self.assertEqual(s.websocket_notification(), "GLXSSLive\n您已上线，状态为空闲中!")
        function.screenshot(self.driver, "online.jpg")

    def test_status(self):
        '''专家状态修改'''
        s = session(self.driver)
        self.assertEqual(s.status(), "空闲中")
        function.screenshot(self.driver, "status_free.jpg")
        s.change_status()
        self.assertEqual(s.status(), "忙线中")
        function.screenshot(self.driver, "status_busy.jpg")

    def test_send(self):
        '''未建立会话时发送文字消息'''
        s = session(self.driver)
        s.send()
        self.assertEqual(s.alert(), "连接尚未建立，发送失败！")


if __name__ == "__main__":
    unittest.main()



# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.forgotpasswordPage import forgotpassword
import unittest


class Test006_ForgotPassword_P1(myunit.MyTest):

    def test_forgotpassword(self):
        '''重置密码'''
        r = forgotpassword(self.driver)
        r.goto_forgotpassword()
        self.assertEqual(r.verify_page(), True)
        r.forgot_password(Data.realemail, Data.password, Data.password)
        r.send_code()
        self.assertEqual(r.error_hint(), "忘记密码：发送成功")
        r.save()
        self.assertEqual(r.success(), True)
        function.screenshot(self.driver, "retrieve_success.jpg")


if __name__ == "__main__":
    unittest.main()
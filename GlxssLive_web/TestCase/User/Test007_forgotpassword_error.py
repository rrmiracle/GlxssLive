# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.forgotpasswordPage import forgotpassword
import unittest


class Test007_ForgotPassword_Error(myunit.MyTest):

    def test_forgot_password_error1(self):
        '''邮箱地址为空'''
        f = forgotpassword(self.driver)
        f.goto_forgotpassword()
        f.send_code()
        self.assertEqual(f.error_hint(), "忘记密码：请输入正确的邮箱地址")
        function.screenshot(self.driver, "forgot_password_email_invalid.jpg")

    def test_forgot_password_error2(self):
        '''其他输入为空'''
        f = forgotpassword(self.driver)
        f.goto_forgotpassword()
        f.forgot_password(Data.realemail)
        f.save()
        self.assertEqual(f.pop_error_hint(), "不能为空哦")
        function.screenshot(self.driver, "forgot_password_blank.jpg")

    def test_forgot_password_error3(self):
        '''验证码错误'''
        f = forgotpassword(self.driver)
        f.goto_forgotpassword()
        f.forgot_password(Data.realemail, Data.password, Data.password, "111111")
        f.save()
        self.assertEqual(f.error_hint(), "忘记密码：验证码错误")
        function.screenshot(self.driver, "forgot_password_code_incorrect.jpg")

    def test_forgot_password_error4(self):
        '''密码不足6位'''
        f = forgotpassword(self.driver)
        f.goto_forgotpassword()
        f.forgot_password(Data.realemail, "1", "1", "111111")
        f.save()
        self.assertEqual(f.pop_error_hint(), "最少 6 个字")
        function.screenshot(self.driver, "forgot_password_new_less.jpg")

    def test_forgot_password_error5(self):
        '''确认密码不符'''
        f = forgotpassword(self.driver)
        f.goto_forgotpassword()
        f.forgot_password(Data.realemail, Data.password, "1", "111111")
        f.save()
        self.assertEqual(f.pop_error_hint(), "你的输入不相同")
        function.screenshot(self.driver, "forgot_password_confirm_diff.jpg")

    # def test_forgot_password_error6(self):
    #     '''用户不存在'''
    #     f = forgotpassword(self.driver)
    #     f.goto_forgotpassword()
    #     f.forgot_password("0000@test.com")
    #     f.send_code()
    #     self.assertEqual(f.error_hint(), "忘记密码：用户不存在")
    #     function.screenshot(self.driver, "forgot_password_user_notexist.jpg")

    # def test_forgot_password_error7(self):
    #     '''邮箱地址不正确'''
    #     f = forgotpassword(self.driver)
    #     f.goto_forgotpassword()
    #     f.forgot_password("1111")
    #     f.send_code()
    #     self.assertEqual(f.error_hint(), "忘记密码：请输入正确的邮箱地址")


if __name__ == "__main__":
    unittest.main()
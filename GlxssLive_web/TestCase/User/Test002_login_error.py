# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.loginPage import login
import unittest


class Test002_Login_Error(myunit.MyTest):

    def test_login_error1(self):
        '''账号格式错误'''
        l = login(self.driver)
        l.login("1", Data.password)
        self.assertEqual(l.error_hint(), "登录：账号格式错误")
        function.screenshot(self.driver, "username_invalid.jpg")

    def test_login_error2(self):
        '''账号密码不正确'''
        l = login(self.driver)
        l.login(Data.username, "111111")
        self.assertEqual(l.error_hint(), "登录：账号或密码不正确")
        function.screenshot(self.driver, "account_invalid.jpg")

    # def test_login_error3(self):
    #     '''验证码不正确'''
    #     l = login(self.driver)
    #     l.login(Data.username, Data.password,"aaaaa")
    #     self.assertEqual(l.error_hint(), "登录：验证码不正确")
    #     function.screenshot(self.driver, "code_invalid.jpg")

    def test_login_error4(self):
        '''用户被删除'''
        l = login(self.driver)
        l.login(Data.username_deleted, Data.password_deleted)
        self.assertEqual(l.error_hint(), "登录：账号或密码不正确")
        function.screenshot(self.driver, "account_deleted.jpg")

    def test_login_error5(self):
        '''输入为空'''
        l = login(self.driver)
        l.login()
        self.assertEqual(l.pop_error_hint(), "不能为空哦")
        function.screenshot(self.driver, "blank.jpg")

    def test_login_error6(self):
        ''' 密码不足6位'''
        l = login(self.driver)
        l.login(Data.username, "1")
        self.assertEqual(l.pop_error_hint(), "最少 6 个字")
        function.screenshot(self.driver, "blank.jpg")

    # def test_login_error7(self):
    #     self.assertEqual(l.error_hint(), "登录：验证码已失效")


if __name__ == "__main__":
    unittest.main()
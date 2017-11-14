# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.registerPage import register
import unittest


class Test004_Register_Error(myunit.MyTest):

    def test_register_error1(self):
        '''企业不存在'''
        r = register(self.driver)
        r.goto_register()
        r.register("1", Data.email, Data.name, Data.password, Data.password)
        self.assertEqual(r.error_hint(), "注册：企业不存在")
        function.screenshot(self.driver, "bs_notexist.jpg")

    def test_register_error2(self):
        '''邮箱重复'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode, Data.username, Data.name, Data.password, Data.password)
        self.assertEqual(r.error_hint(), "注册：数据库中已存在该记录")
        function.screenshot(self.driver, "email_exist.jpg")

    # def test_register_error3(self):
    #     '''验证码不正确'''
    #     r = register(self.driver)
    #     r.goto_register()
    #     r.register(Data.businesscode, Data.email, Data.name, Data.password, Data.password, "aaaaa")
    #     self.assertEqual(r.error_hint(), "注册：验证码不正确")
    #     function.screenshot(self.driver, "code_incorrect.jpg")

    def test_register_error4(self):
        '''输入为空'''
        r = register(self.driver)
        r.goto_register()
        r.register()
        self.assertEqual(r.pop_error_hint(), "不能为空哦")
        function.screenshot(self.driver, "register_blank.jpg")

    def test_register_error5(self):
        '''Email地址无效'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode, "1", Data.name, Data.password, Data.password)
        self.assertEqual(r.pop_error_hint(), "请输入有效的电子邮件")
        function.screenshot(self.driver, "email_invalid.jpg")

    def test_register_error6(self):
        '''密码不足6位'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode, Data.email, Data.name, "1", "1")
        self.assertEqual(r.pop_error_hint(), "最少 6 个字")
        function.screenshot(self.driver, "password_less.jpg")

    def test_register_error7(self):
        '''确认密码不符'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode, Data.email, Data.name, Data.password, "1")
        self.assertEqual(r.pop_error_hint(), "你的输入不相同")
        function.screenshot(self.driver, "password_diff.jpg")

    def test_loginerror8(self):
        '''用户超出限制'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode_only, Data.email, Data.name, Data.password, Data.password)
        self.assertEqual(r.error_hint(), "注册：用户数超出限制")
        function.screenshot(self.driver, "user_morethanlimit.jpg")

    # def test_register_error8(self):
    #     self.assertEqual(r.error_hint(), "注册：验证码已失效")

if __name__ == "__main__":
    unittest.main()

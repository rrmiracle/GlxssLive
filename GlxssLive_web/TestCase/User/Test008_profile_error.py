# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.profilePage import profile
import unittest


class Test008_Profile_Error(myunit.MyTest_login):

    def test_modify_name_error(self):
        '''用户姓名为空'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.clear()
        p.profile_save()
        self.assertEqual(p.error_name(), "不能为空哦")
        function.screenshot(self.driver, "profile_name_blank.jpg")

    def test_modify_password_error1(self):
        '''输入为空'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_save()
        self.assertEqual(p.error_old_password(), "不能为空哦")
        self.assertEqual(p.error_new_password(), "不能为空哦")
        self.assertEqual(p.error_confirm_password(), "不能为空哦")
        function.screenshot(self.driver, "profile_password_blank.jpg")

    def test_modify_password_error2(self):
        '''确认密码不一致'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_modify(Data.password, Data.password, "1")
        p.password_save()
        self.assertEqual(p.error_confirm_password(), "你的输入不相同")
        function.screenshot(self.driver, "profile_password_confirmpsd_diff.jpg")

    def test_modify_password_error3(self):
        '''新密码不足6位'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_modify(Data.password, "1", "1")
        p.password_save()
        self.assertEqual(p.error_new_password(), "最少 6 个字")
        function.screenshot(self.driver, "profile_password_newpsd_less.jpg")

    def test_modify_password_error4(self):
        '''原密码不正确'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_modify("1", Data.password, Data.password)
        p.password_save()
        self.assertEqual(p.reason(), "原密码不正确")
        function.screenshot(self.driver, "profile_password_old_incorrect.jpg")


if __name__ == "__main__":
    unittest.main()
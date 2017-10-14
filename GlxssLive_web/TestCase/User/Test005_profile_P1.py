# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.profilePage import profile
import unittest
import os


class Test005_Profile_P1(myunit.MyTest_login):

    def test_update_avatar(self):
        '''更新头像'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_avetar()
        os.system("D:\\upload.exe")
        p.profile_save()
        self.assertEqual(p.success(), True)
        function.screenshot(self.driver, "profile_avetar.jpg")

    def test_update_name(self):
        '''更新姓名'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.clear()
        p.profile_name("Update")
        p.profile_save()
        self.assertEqual(p.success(), True)
        function.screenshot(self.driver, "profile_name.jpg")

    def test_update_password(self):
        '''更新密码'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_modify(Data.password, Data.password, Data.password)
        p.password_save()
        self.assertEqual(p.success(), True)
        function.screenshot(self.driver, "modify_password_success.jpg")
        p.OK()
        self.assertEqual(p.verify_page(), True)

    def test_back(self):
        '''返回到个人信息页面'''
        p = profile(self.driver)
        p.open_profile()
        self.assertEqual(p.verify(), True)
        p.profile_modify()
        p.password_modify(Data.password, Data.password, Data.password)
        p.password_back()
        self.assertEqual(p.verify(), True)
        function.screenshot(self.driver, "backto_profile.jpg")


if __name__ == "__main__":
    unittest.main()






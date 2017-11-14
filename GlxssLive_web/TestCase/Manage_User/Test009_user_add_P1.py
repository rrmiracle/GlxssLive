from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test009_User_Add_P1(myunit.MyTest_login):

    def test_add_user(self):
        '''添加用户'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, Data.password, Data.password, Data.mobile)
        u.type()
        u.select_company()
        u.add_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "add_user.jpg")

    def test_back(self):
        '''添加用户并返回'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, Data.password, Data.password, Data.mobile)
        u.type()
        u.select_company()
        u.add_back()
        self.assertEqual(u.verify(), True)
        function.screenshot(self.driver, "add_user_back.jpg")


if __name__ == "__main__":
    unittest.main()


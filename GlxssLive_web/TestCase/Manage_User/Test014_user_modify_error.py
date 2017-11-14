from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test014_User_Modify_Error(myunit.MyTest_login):

    def test_user_modify_error1(self):
        '''输入为空'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        self.assertEqual(u.sub_tagname(), "用户管理-修改")
        u.name_clear()
        u.modify_save()
        self.assertEqual(u.error_name(), "不能为空哦")
        function.screenshot(self.driver, "modify_user_blank.jpg")

    def test_user_modify_error2(self):
        '''没有专业'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        self.assertEqual(u.sub_tagname(), "用户管理-修改")
        u.type(2)
        u.special_uncheck()
        u.modify_save()
        self.assertEqual(u.reason(), "专业不能为空！")
        function.screenshot(self.driver, "modify_user_special_notexist.jpg")


if __name__ == "__main__":
    unittest.main()


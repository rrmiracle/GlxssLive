from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test020_Role_Modify_Error(myunit.MyTest_login):

    def test_role_modify_error(self):
        '''输入为空'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.modify_user()
        self.assertEqual(u.sub_tagname(), "角色管理-修改")
        u.clear_name()
        u.clear_remark()
        u.add_save()
        self.assertEqual(u.error_name(), "不能为空哦")
        self.assertEqual(u.error_remark(), "不能为空哦")
        function.screenshot(self.driver, "modify_role_error.jpg")


if __name__ == "__main__":
    unittest.main()



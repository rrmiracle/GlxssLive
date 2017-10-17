from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test019_Role_Add_Error(myunit.MyTest_login):

    def test_role_add_error(self):
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "角色管理-新增")
        u.add_save()
        self.assertEqual(u.error_name(), "不能为空哦")
        self.assertEqual(u.error_company(), "不能为空哦")
        self.assertEqual(u.error_remark(), "不能为空哦")
        function.screenshot(self.driver, "add_role_error.jpg")


if __name__ == "__main__":
    unittest.main()



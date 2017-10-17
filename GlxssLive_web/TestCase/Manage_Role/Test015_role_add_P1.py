from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test015_Role_Add_P1(myunit.MyTest_login):

    def test_add_role(self):
        '''添加角色'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "角色管理-新增")
        u.add_role(Data.rolename, "备注")
        u.select_company()
        u.add_save()
        self.assertEqual(u.result(), "操作成功")
        function.screenshot(self.driver, "add_role.jpg")

    def test_add_role_back(self):
        '''添加角色并返回'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "角色管理-新增")
        u.add_role(Data.rolename, "备注")
        u.select_company()
        u.add_back()
        self.assertEqual(u.verify(), True)
        function.screenshot(self.driver, "add_role_back.jpg")


if __name__ == "__main__":
    unittest.main()



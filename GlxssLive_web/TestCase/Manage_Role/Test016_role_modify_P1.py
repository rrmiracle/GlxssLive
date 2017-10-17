from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test016_Role_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改角色名称'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.modify_user()
        self.assertEqual(u.sub_tagname(), "角色管理-修改")
        u.clear_name()
        u.add_role("Update", "")
        self.assertEqual(u.company_status(), False)
        u.add_save()
        self.assertEqual(u.result(), "操作成功")
        function.screenshot(self.driver, "modify_role_name.jpg")

    def test_modify_description(self):
        '''修改角色备注'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.modify_user()
        self.assertEqual(u.sub_tagname(), "角色管理-修改")
        u.clear_remark()
        u.add_role("", "Update")
        u.add_save()
        self.assertEqual(u.result(), "操作成功")
        function.screenshot(self.driver, "modify_role_remark.jpg")

    def test_modifytype(self):
        '''修改角色类型'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.modify_user()
        self.assertEqual(u.sub_tagname(), "角色管理-修改")
        u.change_role_menu()
        u.add_save()
        self.assertEqual(u.result(), "操作成功")
        function.screenshot(self.driver, "modify_role_menu.jpg")

    def test_back(self):
        '''修改角色并返回'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.modify_user()
        self.assertEqual(u.sub_tagname(), "角色管理-修改")
        u.clear_name()
        u.clear_remark()
        u.add_back()
        self.assertEqual(u.verify(), True)
        function.screenshot(self.driver, "modify_role_back.jpg")


if __name__ == "__main__":
    unittest.main()



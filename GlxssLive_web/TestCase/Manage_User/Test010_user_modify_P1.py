from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test010_User_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改用户姓名'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        self.assertEqual(u.sub_tagname(), "用户管理-修改")
        u.status()
        self.assertEqual(u.status(), ("true", "true", "true"))
        u.name_clear()
        u.modify_user_input("update")
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_name.jpg")

    def test_modify_description(self):
        '''修改用户描述'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.description_clear()
        u.modify_user_input("", "update")
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_description.jpg")

    def test_modify_type(self):
        '''修改用户类型'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.change_type()
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_type.jpg")

    def test_modify_department(self):
        '''修改用户部门'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.change_department()
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_department.jpg")

    def test_modify_role(self):
        '''修改用户角色'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.role()
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_role.jpg")

    def test_modify_special(self):
        '''修改用户专业'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.change_special()
        u.modify_save()
        self.assertEqual(u.success(), True)
        function.screenshot(self.driver, "modify_special.jpg")

    def test_back(self):
        '''修改用户信息并返回'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.modify_obj()
        u.role()
        u.modify_back()
        self.assertEqual(u.verify(), True)
        function.screenshot(self.driver, "modify_back.jpg")


if __name__ == "__main__":
    unittest.main()
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test018_Role_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何角色'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.delete()
        self.assertEqual(u.reason(), "请选择一条数据")
        function.screenshot(self.driver, "role_unselect.jpg")

    def test_multiselect(self):
        '''选择两个角色'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.multi_select()
        u.modify()
        self.assertEqual(u.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "role_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()



from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.rolemanagePage import rolemanage
import unittest


class Test017_Role_Delete_P1(myunit.MyTest_login):

    def test_delete_role(self):
        '''删除角色'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        u.delete_user()
        self.assertEqual(u.result(), "您确定要删除这条信息吗")
        u.confirm()
        self.assertEqual(u.result(), "删除成功")
        function.screenshot(self.driver, "delete_role.jpg")

    def test_delete_cancle(self):
        '''取消删除角色'''
        u = rolemanage(self.driver)
        u.open_rolemanage()
        self.assertEqual(u.verify(), True)
        n = u.name_list()
        u.delete_user()
        self.assertEqual(u.result(), "您确定要删除这条信息吗")
        u.cancel()
        self.assertEqual(u.name_list(), n)
        function.screenshot(self.driver, "delete_role_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test011_User_Delete_P1(myunit.MyTest_login):

    def test_delete(self):
        '''删除用户'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.delete_user()
        self.assertEqual(u.result(), "您确定要删除这条信息吗")
        u.confirm()
        self.assertEqual(u.result(), "删除成功")
        function.screenshot(self.driver, "delete_user.jpg")

    def test_cancle(self):
        '''取消删除用户'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        email = u.email_list()
        u.delete_user()
        self.assertEqual(u.result(), "您确定要删除这条信息吗")
        u.cancel()
        self.assertEqual(u.email_list(), email)
        function.screenshot(self.driver, "cancle_delete_user.jpg")


if __name__ == "__main__":
    unittest.main()

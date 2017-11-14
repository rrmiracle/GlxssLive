from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest


class Test042_Special_Delete_P1(myunit.MyTest_login):

    def test_special_delete(self):
        '''删除专业'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.delete_obj()
        self.assertEqual(s.result(), "您确定要删除这条信息吗")
        s.confirm()
        self.assertEqual(s.result(),  "删除成功")
        function.screenshot(self.driver, "delete_special.jpg")

    def test_special_delete_cancle(self):
        '''取消删除专业'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        a = s.name_list()
        s.delete_obj()
        self.assertEqual(s.result(), "您确定要删除这条信息吗")
        s.cancel()
        self.assertEqual(s.name_list(),  a)
        function.screenshot(self.driver, "delete_special_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



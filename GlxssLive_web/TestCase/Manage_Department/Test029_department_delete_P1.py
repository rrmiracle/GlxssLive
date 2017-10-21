from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test029_Department_Delete_P1(myunit.MyTest_login):

    def test_department_delete(self):
        '''删除部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.deptstatus()
        d.delete()
        self.assertEqual(d.result(), "您确定要删除这条信息吗")
        d.confirm()
        self.assertEqual(d.result(), "删除成功")
        function.screenshot(self.driver, "delete_department.jpg")

    def test_department_cancle(self):
        '''取消删除部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        n = d.name_list()
        d.deptstatus()
        d.delete()
        self.assertEqual(d.result(), "您确定要删除这条信息吗")
        d.cancel()
        self.assertEqual(d.name_list(), n)
        function.screenshot(self.driver, "delete_department_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



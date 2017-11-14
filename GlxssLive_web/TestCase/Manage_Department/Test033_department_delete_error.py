from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test033_Department_Delete_Error(myunit.MyTest_login):

    def test_department_delete_error(self):
        '''删除有子部门的部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.deptstatus(2)
        d.delete()
        self.assertEqual(d.result(), "您确定要删除这条信息吗")
        d.confirm()
        self.assertEqual(d.result(), "删除失败")
        self.assertEqual(d.reason(),"请先删除子部门")
        function.screenshot(self.driver, "department_delete_parent.jpg")


if __name__ == "__main__":
    unittest.main()



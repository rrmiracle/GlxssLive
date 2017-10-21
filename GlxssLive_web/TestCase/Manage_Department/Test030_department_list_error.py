from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test030_Deparment_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.delete()
        self.assertEqual(d.reason(), "请选择一条数据")
        function.screenshot(self.driver, "department_unselect.jpg")

    def test_multiselect(self):
        '''选择两个部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.multi_select()
        d.modify()
        self.assertEqual(d.reason(), "只能选择一条数据")
        function.screenshot(self.driver, "department_multiselect.jpg")


if __name__ == "__main__":
    unittest.main()



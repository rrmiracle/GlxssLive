from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test028_Department_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改部门名称'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "部门管理-修改")
        d.name_clear()
        d.add_department(Data.depname+"Update", "")
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_department_name.jpg")

    def test_modify_number(self):
        '''修改排序号'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "部门管理-修改")
        d.order_clear()
        d.add_department("", "111")
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_department_order.jpg")

    def test_modify_dept(self):
        '''修改上级部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "部门管理-修改")
        d.change_dept()
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "modify_department_dept.jpg")

    def test_modify_back(self):
        '''修改部门并返回'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        self.assertEqual(d.sub_tagname(), "部门管理-修改")
        d.add_back()
        self.assertEqual(d.verify(), True)
        function.screenshot(self.driver, "modify_department_back.jpg")


if __name__ == "__main__":
    unittest.main()



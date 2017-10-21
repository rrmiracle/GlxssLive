from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test027_Department_Add_P1(myunit.MyTest_login):

    def test_department_add(self):
        '''添加部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "部门管理-新增")
        d.select_company()
        d.add_department(Data.depname, "1")
        d.add_save()
        self.assertEqual(d.success(), True)
        function.screenshot(self.driver, "add_department.jpg")

    def test_department_add_back(self):
        '''添加部门并返回'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.add()
        self.assertEqual(d.sub_tagname(), "部门管理-新增")
        d.select_company()
        d.add_department(Data.depname, "1")
        d.add_back()
        self.assertEqual(d.verify(), True)
        function.screenshot(self.driver, "add_department_back.jpg")


if __name__ == "__main__":
    unittest.main()



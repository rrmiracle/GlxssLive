from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest


class Test032_Department_Modify_Error(myunit.MyTest_login):

    def test_department_modify_error1(self):
        '''输入为空'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        d.name_clear()
        d.order_clear()
        d.add_save()
        self.assertEqual(d.error_name(), "不能为空哦")
        self.assertEqual(d.error_order(), "不能为空哦")
        function.screenshot(self.driver, "department_modify_blank.jpg")

    def test_department_modify_error2(self):
        '''部门名称已存在'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        d.name_clear()
        d.add_department("2", "")
        d.add_save()
        self.assertEqual(d.reason(), "数据库中已存在该记录")
        function.screenshot(self.driver, "department_modify_name_exist.jpg")

    def test_department_modify_error3(self):
        '''把本部门设为上级部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.modify_obj()
        d.setself()
        d.add_save()
        self.assertEqual(d.reason(), "不可以指定本部门为上级部门")
        function.screenshot(self.driver, "department_modify_self.jpg")

    def test_department_modify_error4(self):
        '''修改有子部门的部门'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.deptstatus(2)
        d.modify()
        d.change_dept()
        d.add_save()
        self.assertEqual(d.reason(), "该部门有子部门，无法修改上级部门")
        function.screenshot(self.driver, "department_modify_parent.jpg")


if __name__ == "__main__":
    unittest.main()



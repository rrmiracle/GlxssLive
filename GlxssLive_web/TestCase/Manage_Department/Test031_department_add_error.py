from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.departmentmanagePage import departmentmanage
import unittest
import random


class Test031_Department_Add_Error(myunit.MyTest_login):

    def test_department_add_error1(self):
        '''输入为空'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.add()
        d.add_save()
        self.assertEqual(d.error_name(), "不能为空哦")
        self.assertEqual(d.error_company(), "不能为空哦")
        self.assertEqual(d.error_order(), "不能为空哦")
        function.screenshot(self.driver, "add_department_blank.jpg")

    def test_department_add_error2(self):
        '''部门名称已存在'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.add()
        d.add_department("1", "1")
        d.select_company()
        d.add_save()
        self.assertEqual(d.reason(), "数据库中已存在该记录")
        function.screenshot(self.driver, "add_department_name_exist.jpg")

    def test_department_add_error3(self):
        '''排序码无效'''
        d = departmentmanage(self.driver)
        d.open_departmentmanage()
        self.assertEqual(d.verify(), True)
        d.add()
        d.select_company()
        d.add_department(Data.depname, random.choice(["1.1", "中文"]))
        d.add_save()
        self.assertEqual(d.error_order(), "请以数字填写")
        function.screenshot(self.driver, "add_department_number_invalid.jpg")


if __name__ == "__main__":
    unittest.main()



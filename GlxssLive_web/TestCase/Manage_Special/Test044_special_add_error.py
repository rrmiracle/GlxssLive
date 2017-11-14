from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest


class Test044_Special_Add_Error(myunit.MyTest_login):

    def test_special_add_error(self):
        '''输入为空'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.add()
        self.assertEqual(s.sub_tagname(), "企业专业表-新增")
        s.add_save()
        self.assertEqual(s.error_name(), "不能为空哦")
        self.assertEqual(s.error_company(), "不能为空哦")
        function.screenshot(self.driver, "add_special_blank.jpg")


if __name__ == "__main__":
    unittest.main()



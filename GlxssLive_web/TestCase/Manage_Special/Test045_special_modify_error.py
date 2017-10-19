from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest


class Test045_Special_Modify_Error(myunit.MyTest_login):

    def test_special_modify_error(self):
        '''输入为空'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "企业专业表-修改")
        s.name_clear()
        s.add_save()
        self.assertEqual(s.error_name(), "不能为空哦")
        function.screenshot(self.driver, "modify_special_blank.jpg")


if __name__ == "__main__":
    unittest.main()



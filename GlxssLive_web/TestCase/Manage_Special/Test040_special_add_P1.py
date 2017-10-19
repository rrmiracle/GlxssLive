from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest


class Test040_Special_Add_P1(myunit.MyTest_login):

    def test_special_add(self):
        '''添加专业'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.add()
        self.assertEqual(s.sub_tagname(), "企业专业表-新增")
        s.add_special(Data.specialname)
        s.select_company()
        s.add_save()
        function.screenshot(self.driver, "add_special.jpg")

    def test_special_add_back(self):
        '''添加专业并返回'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.add()
        self.assertEqual(s.sub_tagname(), "企业专业表-新增")
        s.add_special(Data.specialname)
        s.select_company()
        s.add_back()
        function.screenshot(self.driver, "add_special_back.jpg")


if __name__ == "__main__":
    unittest.main()



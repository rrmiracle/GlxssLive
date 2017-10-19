from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.specialmanagePage import specialmanage
import unittest


class Test041_Special_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改专业名'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "企业专业表-修改")
        self.assertEqual(s.company_status(), False)
        s.name_clear()
        s.add_special("Updaate")
        s.add_save()
        function.screenshot(self.driver, "modify_special_name.jpg")

    def test_back(self):
        '''修改专业并返回'''
        s = specialmanage(self.driver)
        s.open_specialmanage()
        self.assertEqual(s.verify(), True)
        s.modify_obj()
        self.assertEqual(s.sub_tagname(), "企业专业表-修改")
        s.name_clear()
        s.add_special("Updaate")
        s.add_back()
        function.screenshot(self.driver, "modify_special_back.jpg")


if __name__ == "__main__":
    unittest.main()



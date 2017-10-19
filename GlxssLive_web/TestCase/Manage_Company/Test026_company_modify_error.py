from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest
import random


class Test026_Company_Modify_Error(myunit.MyTest_login):

    def test_company_modify_error1(self):
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.name_clear()
        c.address_clear()
        c.server_clear()
        c.limit_clear()
        c.add_save()
        self.assertEqual(c.error_name(), "不能为空哦")
        self.assertEqual(c.error_server(), "不能为空哦")
        self.assertEqual(c.error_limit(), "不能为空哦")
        self.assertEqual(c.error_address(), "不能为空哦")
        function.screenshot(self.driver, "modify_company_blank.jpg")

    def test_company_modify_error2(self):
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.limit_clear()
        c.add_company("", "", "", random.choice(["-1", "1.1", "A", "中文"]))
        c.add_save()
        self.assertEqual(c.error_limit(), "请以数字填写")
        function.screenshot(self.driver, "modify_company_blank.jpg")


if __name__ == "__main__":
    unittest.main()



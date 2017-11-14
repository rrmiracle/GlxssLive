from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest
import random


class Test025_Company_Add_Error(myunit.MyTest_login):

    def test_company_add_error1(self):
        '''输入为空'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.add()
        self.assertEqual(c.sub_tagname(), "企业管理-新增")
        c.add_save()
        self.assertEqual(c.error_name(), "不能为空哦")
        self.assertEqual(c.error_type(), "不能为空哦")
        self.assertEqual(c.error_trade(), "不能为空哦")
        self.assertEqual(c.error_server(), "不能为空哦")
        self.assertEqual(c.error_limit(), "不能为空哦")
        self.assertEqual(c.error_address(), "不能为空哦")
        function.screenshot(self.driver, "add_company_blank.jpg")

    def test_company_add_error2(self):
        '''人数上限输入无效'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.add()
        self.assertEqual(c.sub_tagname(), "企业管理-新增")
        c.add_company(Data.name, Data.name, Data.name, random.choice(["-1", "1.1", "A", "中文"]))
        c.add_save()
        self.assertEqual(c.error_limit(), "请以数字填写")
        function.screenshot(self.driver, "add_company_limit_invalid.jpg")


if __name__ == "__main__":
    unittest.main()



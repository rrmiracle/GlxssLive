from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest


class Test021_Company_Add_P1(myunit.MyTest_login):

    def test_company_add(self):
        '''添加企业'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.add()
        self.assertEqual(c.sub_tagname(), "企业管理-新增")
        c.add_company(Data.name, Data.name, Data.name, "9999")
        c.select_trade()
        c.select_type()
        c.add_save()
        self.assertEqual(c.reason(), "您不能添加企业")
        function.screenshot(self.driver, "add_company.jpg")

    def test_company_add_back(self):
        '''添加企业并返回'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.add()
        self.assertEqual(c.sub_tagname(), "企业管理-新增")
        c.add_company(Data.name, Data.name, Data.name, "9999")
        c.select_trade()
        c.select_type()
        c.add_back()
        self.assertEqual(c.verify(), True)
        function.screenshot(self.driver, "add_company_back.jpg")


if __name__ == "__main__":
    unittest.main()



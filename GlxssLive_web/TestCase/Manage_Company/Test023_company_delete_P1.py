from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest


class Test023_Company_Delete_P1(myunit.MyTest_login):

    def test_company_delete(self):
        '''删除企业'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.delete_obj()
        self.assertEqual(c.result(), "您确定要删除这条信息吗")
        c.confirm()
        self.assertEqual(c.reason(), "您不能删除企业")
        function.screenshot(self.driver, "delete_company.jpg")

    def test_cancle(self):
        '''取消删除企业'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        business = c.businesscode_list()
        c.delete_obj()
        self.assertEqual(c.result(), "您确定要删除这条信息吗")
        c.cancel()
        self.assertEqual(c.businesscode_list(), business)
        function.screenshot(self.driver, "delete_company_cancle.jpg")


if __name__ == "__main__":
    unittest.main()



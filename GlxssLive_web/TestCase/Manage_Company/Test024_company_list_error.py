from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest


class Test024_Company_List_Error(myunit.MyTest_login):

    def test_unselect(self):
        '''不选择任何企业'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.delete()
        self.assertEqual(c.reason(), "请选择一条数据")
        function.screenshot(self.driver, "company_unselect.jpg")


if __name__ == "__main__":
    unittest.main()



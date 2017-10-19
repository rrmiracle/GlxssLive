from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.companymanagePage import companymanage
import unittest


class Test022_Company_Modify_P1(myunit.MyTest_login):

    def test_modify_name(self):
        '''修改企业名称'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.name_clear()
        c.add_company("Update", "", "", "")
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_name.jpg")

    def test_modify_server(self):
        '''修改企业存储服务器地址'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.server_clear()
        c.add_company("", "Update", "", "")
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_server.jpg")

    def test_modify_address(self):
        '''修改企业地址'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.address_clear()
        c.add_company("", "", "Update", "")
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_address.jpg")

    def test_modify_limit(self):
        '''修改企业人数上限'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.limit_clear()
        c.add_company("", "", "", "1111")
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_limit.jpg")

    def test_modify_trade(self):
        '''修改企业行业'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.modify_trade()
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_trade.jpg")

    def test_modify_type(self):
        '''修改企业类型'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.modify_type()
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_type.jpg")

    def test_modify_contact(self):
        '''修改企业联系人'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        contact = c.current_contact()
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.modify_contact(contact)
        c.add_save()
        self.assertEqual(c.success(), True)
        function.screenshot(self.driver, "modify_company_contact.jpg")
        c.confirm()
        c.modify_obj()
        c.recovery(contact)
        c.add_save()

    def test_modify_back(self):
        '''修改企业并返回'''
        c = companymanage(self.driver)
        c.open_companymanage()
        self.assertEqual(c.verify(), True)
        c.modify_obj()
        self.assertEqual(c.sub_tagname(), "企业管理-修改")
        c.add_back()
        self.assertEqual(c.verify(), True)
        function.screenshot(self.driver, "modify_company_back.jpg")


if __name__ == "__main__":
    unittest.main()



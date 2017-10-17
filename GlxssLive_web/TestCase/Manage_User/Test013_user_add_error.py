from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest


class Test013_User_Add_Error(myunit.MyTest_login):

    def test_user_add_error1(self):
        '''用户输入为空'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_save()
        self.assertEqual(u.error_name(), "不能为空哦")
        self.assertEqual(u.error_type(), "不能为空哦")
        self.assertEqual(u.error_company(), "不能为空哦")
        self.assertEqual(u.error_password(), "不能为空哦")
        self.assertEqual(u.error_confirmpsd(), "不能为空哦")
        self.assertEqual(u.error_email(), "不能为空哦")
        self.assertEqual(u.error_phone(), "不能为空哦")
        function.screenshot(self.driver, "add_user_blank.jpg")

    def test_user_add_error2(self):
        '''密码不足6位'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, "1", "1", Data.mobile)
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_password(), "最少 6 个字")
        function.screenshot(self.driver, "add_user_password_less.jpg")

    def test_user_add_error3(self):
        '''确认密码不符'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, Data.password, "1", Data.mobile)
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_confirmpsd(), "你的输入不相同")
        function.screenshot(self.driver, "add_user_password_diff.jpg")

    def test_user_add_error4(self):
        '''邮箱不足6位'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, "Test", Data.password, Data.password, Data.mobile)
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_email(), "最少 6 个字")
        function.screenshot(self.driver, "add_user_email_less.jpg")

    def test_user_add_error5(self):
        '''手机号码不足11位'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, Data.password, Data.password, "1")
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_phone(), "最少 11 个字")
        function.screenshot(self.driver, "add_user_phone_less.jpg")

    def test_user_add_error6(self):
        '''手机号码格式不正确'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.email, Data.password, Data.password, "11111111111")
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_phone(), "请正确填写您的手机号码")
        function.screenshot(self.driver, "add_user_phone_incorrect.jpg")

    def test_user_add_error7(self):
        '''用户邮箱已存在'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.username, Data.password, Data.password, Data.mobile)
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.reason(), "数据库中已存在该记录")
        function.screenshot(self.driver, "add_user_email_exist.jpg")

    def test_user_add_error8(self):
        '''电话号码已存在'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.username, Data.password, Data.password, "13100000000")
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.reason(), "数据库中已存在该记录")
        function.screenshot(self.driver, "add_user_phone_exist.jpg")

    def test_user_add_error9(self):
        '''专业为空'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, Data.username, Data.password, Data.password, Data.mobile)
        u.select_company()
        u.type(2)
        u.add_save()
        self.assertEqual(u.reason(),"专业不能为空！")
        function.screenshot(self.driver, "add_user_special_notexist.jpg")

    def test_user_add_error10(self):
        '''邮箱格式不正确'''
        u = usermanage(self.driver)
        u.open_usermanage()
        self.assertEqual(u.verify(), True)
        u.add()
        self.assertEqual(u.sub_tagname(), "用户管理-新增")
        u.add_user(Data.name, "Test", Data.password, Data.password, Data.mobile)
        u.select_company()
        u.type()
        u.add_save()
        self.assertEqual(u.error_email(), "请输入有效的邮箱地址")
        function.screenshot(self.driver, "add_user_email_incorrect.jpg")


if __name__ == "__main__":
    unittest.main()
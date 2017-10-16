from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.usermanagePage import usermanage
import unittest



class Test013_User_Add_Error(myunit.MyTest_login):

    def test_blank(self):
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.username(), "不能为空哦")
        self.assertEqual(error.type(), "不能为空哦")
        self.assertEqual(error.company(), "不能为空哦")
        self.assertEqual(error.password(), "不能为空哦")
        self.assertEqual(error.confirmpsd(), "不能为空哦")
        self.assertEqual(error.email(), "不能为空哦")
        self.assertEqual(error.mobile(), "不能为空哦")

    def test_passwordless(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", "1", "1", u.email, u.mobile)
        man.select_type(1)
        man.select_company()
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.password(), "最少 6 个字")

    def test_passwordiff(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, "111111", u.email, u.mobile)
        man.select_type(1)
        man.select_company()
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.confirmpsd(), "你的输入不相同")

    def test_emailincorrect(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, "1", u.mobile)
        man.select_type(1)
        man.select_company()
        man.save()
        uap = UsernameAndPassword(self.driver)
        time.sleep(1)
        self.assertEqual(uap.notification(), "邮箱格式不正确")

    def test_mobileless(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, u.email, "1")
        man.select_type(1)
        man.select_company()
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.mobile(), "最少 11 个字")

    def test_mobileincorrect(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, u.email, "11111111111")
        man.select_type(1)
        man.select_company()
        man.save()
        error = Errormsg(self.driver)
        time.sleep(1)
        self.assertEqual(error.mobile(), "请正确填写您的手机号码")

    def test_emailexist(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, u.username, u.mobile)
        man.select_type(1)
        man.select_company()
        man.save()
        uap = UsernameAndPassword(self.driver)
        time.sleep(1)
        self.assertEqual(uap.notification(), "数据库中已存在该记录")

    def test_mobileexist(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, u.email, "13100000000")
        man.select_type(1)
        man.select_company()
        man.save()
        uap = UsernameAndPassword(self.driver)
        time.sleep(1)
        self.assertEqual(uap.notification(), "数据库中已存在该记录")

    def test_nospecial(self):
        u = Data
        man = Management(self.driver)
        man.goto_usermanagement()
        man.add_user()
        man.input("test", u.password, u.password, u.email, u.mobile)
        man.select_type(2)
        man.select_company()
        man.save()
        uap = UsernameAndPassword(self.driver)
        time.sleep(1)
        self.assertEqual(uap.notification(), "专业不能为空！")

if __name__ == "__main__":
    unittest.main()
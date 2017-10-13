import unittest

from selenium import webdriver

from Case.User.update import Login, Update
from GlxssLive_web.Data.Data import Data


class Test005_Profile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.close()
        print("finish")

    def test_updateavatar(self):
        up = Update(self.driver)
        up.goto_profile()
        self.assertEqual(up.tagname(), "个人中心")
        up.update_avatar()
        up.save()
        self.assertEqual(up.result(), "操作成功")

    def test_updatename(self):
        up = Update(self.driver)
        up.goto_profile()
        self.assertEqual(up.tagname(), "个人中心")
        up.update_name()
        up.save()
        self.assertEqual(up.result(), "操作成功")

    def test_updatepassword(self):
        u = Data
        up = Update(self.driver)
        up.goto_profile()
        self.assertEqual(up.tagname(), "个人中心")
        up.update_password(u.password, u.password, u.password)
        self.assertEqual(up.result(), "操作成功")
        up.confirm()
        self.assertEqual(self.driver.current_url, u.login_url)


if __name__ == "__main__":
    unittest.main()






# coding=utf-8
import time
import unittest

from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.loginPage import login


class Test001_loginandout_P1(myunit.MyTest):

    def test_login(self):
        '''登录成功并登出'''
        # u = Data.Data
        # time.sleep(5)
        # uap = UsernameAndPassword(self.driver)
        # uap.input(u.username, u.password)
        # time.sleep(10)
        # # 手动输入验证码
        # uap.confirm()
        # time.sleep(3)
        # self.assertEqual(self.driver.current_url, u.main_url)
        # function.screenshot(self.driver, "mainpage.jpg")
        # uap.logout()
        # self.assertEqual(self.driver.current_url, u.login_url)
        l = login(self.driver)
        l.login(Data.username, Data.password)
        time.sleep(3)
        self.assertEqual(l.verify(), True)
        function.screenshot(self.driver, "mainpage.jpg")


if __name__ == "__main__":
    unittest.main()
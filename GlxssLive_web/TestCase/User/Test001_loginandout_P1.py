# coding=utf-8
import time
import unittest

from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj import loginPage, sidemenuPage


class Test001_LoginAndOut_P1(myunit.MyTest):

    def test_login(self):
        '''登录成功并登出'''
        l = loginPage.login(self.driver)
        l.login(Data.username, Data.password)
        time.sleep(3)
        self.assertEqual(l.verify(), True)
        function.screenshot(self.driver, "mainpage.jpg")
        s = sidemenuPage.sidemenu(self.driver)
        s.logout()
        self.assertEqual(s.verify_page(), True)
        function.screenshot(self.driver, "loginpage.jpg")


if __name__ == "__main__":
    unittest.main()
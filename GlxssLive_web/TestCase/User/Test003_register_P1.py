# coding=utf-8
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import function, myunit
from GlxssLive_web.TestCase.Page_obj.registerPage import register
import unittest
import time


class Test003_Register_P1(myunit.MyTest):

    def test_register(self):
        '''注册成功'''
        r = register(self.driver)
        r.goto_register()
        r.register(Data.businesscode, Data.email, Data.name, Data.password, Data.password)
        time.sleep(3)
        # self.assertEqual(r.verify_page(), True)
        function.screenshot(self.driver, "register_success.jpg")


if __name__ == "__main__":
    unittest.main()
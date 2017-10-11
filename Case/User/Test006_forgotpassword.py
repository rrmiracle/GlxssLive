import time
import unittest

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test006_forgotpassword(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.url)
        time.sleep(5)
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_forgotpassword(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.gotofp()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, u.fpassword_url)
        uap.inputf(u.realemail)
        uap.send()
        time.sleep(3)
        self.assertEqual(uap.errormsg(), "忘记密码：发送成功")
        uap.clear()
        uap.inputf(u.realemail, u.password, u.password)
        time.sleep(40)
        uap.confirm()
        time.sleep(3)
        self.assertEqual(uap.notification(), "修改成功！请点击确认按钮跳转到登录页面")


if __name__ == "__main__":
    unittest.main()
import time
import unittest

from selenium import webdriver

from Case.User.Data import Data
from .update import UsernameAndPassword


class Test007_fperror(unittest.TestCase):
    def setUp(self):
        u = Data
        self.driver = webdriver.Firefox()
        self.driver.get(u.fpassword_url)
        time.sleep(5)
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_fperror1(self):
        uap = UsernameAndPassword(self.driver)
        uap.send()
        self.assertEqual(uap.errormsg(), "忘记密码：请输入正确的邮箱地址")

    def test_fperror2(self):
        uap = UsernameAndPassword(self.driver)
        uap.confirm()
        self.assertEqual(uap.popmsg(), "不能为空哦")

    def test_fperror3(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputf(u.email, u.password, u.password, "aaaaa")
        uap.confirm()
        self.assertEqual(uap.errormsg(), "忘记密码：验证码错误")

    def test_fperror4(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputf(u.email, "1", "1", "aaaaa")
        uap.confirm()
        self.assertEqual(uap.popmsg(), "最少 6 个字")

    def test_fperror5(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputf(u.email, u.password, "1", "aaaaa")
        uap.confirm()
        self.assertEqual(uap.popmsg(), "你的输入不相同")

    def test_fperror6(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputf("0000@test.com")
        uap.send()
        self.assertEqual(uap.errormsg(), "忘记密码：用户不存在")

    def test_fperror7(self):
        u = Data
        uap = UsernameAndPassword(self.driver)
        uap.inputf("1")
        uap.send()
        self.assertEqual(uap.errormsg(), "忘记密码：请输入正确的邮箱地址")

if __name__ == "__main__":
    unittest.main()
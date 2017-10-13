import time
import unittest

from selenium import webdriver

from Case.User.update import Login, Update, UsernameAndPassword
from GlxssLive_web.Data.Data import Data


class Test008_profileerror(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        up = Update(self.driver)
        up.goto_profile()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_usernameblank(self):
        time.sleep(3)
        up = Update(self.driver)
        up.clear()
        up.save()
        self.assertEqual(up.errormsg(), "不能为空哦")

    def test_modifypassword1(self):
        time.sleep(3)
        up = Update(self.driver)
        up.modifypassword()
        time.sleep(2)
        self.assertEqual(up.tagname(), "修改密码")
        up.modify()
        self.assertEqual(up.errormsg(), ('不能为空哦', '不能为空哦', '不能为空哦'))

    def test_modifypassword2(self):
        u = Data
        time.sleep(3)
        up = Update(self.driver)
        up.update_password(u.password, u.password, "1")
        self.assertEqual(up.tagname(), "修改密码")
        up.modify()
        self.assertEqual(up.errormsg(), "你的输入不相同")

    def test_modifypassword3(self):
        u = Data
        time.sleep(3)
        up = Update(self.driver)
        up.update_password(1, u.password, u.password)
        self.assertEqual(up.tagname(), "修改密码")
        up.modify()
        self.assertEqual(up.result(), "操作失败")
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "原密码不正确")

    def test_modifypassword4(self):
        u = Data
        time.sleep(3)
        up = Update(self.driver)
        up.update_password(u.password, "1", "1")
        self.assertEqual(up.tagname(), "修改密码")
        up.modify()
        self.assertEqual(up.errormsg(), "最少 6 个字")


if __name__ == "__main__":
    unittest.main()
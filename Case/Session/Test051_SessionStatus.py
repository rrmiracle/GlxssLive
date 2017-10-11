from selenium import webdriver
from Case.User.update import Login
import unittest
from .Session import Session


class Test051_SessionStatus(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_online(self):
        man = Session(self.driver)
        self.assertEqual(man.wsnotification(), "GLXSSLive\n您已上线，状态为空闲中!")

    def test_status(self):
        man = Session(self.driver)
        self.assertEqual(man.status(), "空闲中")
        man.changestatus()
        self.assertEqual(man.status(), "忙线中")

    def test_send(self):
        man = Session(self.driver)
        man.send()
        self.assertEqual(man.alert(), "连接尚未建立，发送失败！")


if __name__ == "__main__":
    unittest.main()



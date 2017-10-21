from selenium import webdriver
from Case.User.update import Login, Update
import unittest
from .sessionmanangement import SessionManagement
from Case.User.Data import Data


class Test047_Modify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_modifyname(self):
        u = Data()
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        self.assertEqual(man.tagname(), "会话管理")
        man.modify()
        self.assertEqual(man.tagname(), "会话管理-修改")
        man.clear(1)
        man.input(u.roomname, "")
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_modifykeyword(self):
        u = Data()
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        man.modify()
        man.clear(2)
        man.input("", ''.join(u.version()))
        man.save()
        up = Update(self.driver)
        self.assertEqual(up.result(), "操作成功")

    def test_back(self):
        u = Data()
        man = SessionManagement(self.driver)
        man.goto_sessionmanagement()
        man.modify()
        man.back()
        up = Update(self.driver)
        self.assertEqual(man.tagname(), "会话管理")


if __name__ == "__main__":
    unittest.main()



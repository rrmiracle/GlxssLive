from selenium import webdriver
import random, os, time, unittest
from GlxssLive_web.Data.Data import Data
from GlxssLive_web.TestCase.models import myunit
from GlxssLive_web.TestCase.Page_obj import loginPage, sessionPage


class test_stability(myunit.MyTest):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Data.url)
        time.sleep(5)
        l = loginPage.login(self.driver)
        l.login("zhuanjia3@qq.com", "123456")
        print("Start=====")

    def test_stability(self):
        time.sleep(20)
        s = sessionPage.session(self.driver)
        while s.session_from() != "未接入会话":
            seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
            str = []
            for i in range(8):
                str.append(random.choice(seed))
            s.message(str)
            s.send()
            time.sleep(60)
            s.send_pic()
            os.system("D:\\upload1.exe")
            time.sleep(60)


if __name__ == "__main__":
    unittest.main()




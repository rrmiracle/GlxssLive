# coding=utf-8
from selenium import webdriver
import unittest
from .Data import Data
import time


class Test002_loginerror(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.maximize_window()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_loginerror1(self):
        u = Data
        self.driver.get(u.url)
        time.sleep(3)
        self.driver.find_element_by_name("usernamee").send_keys("1")
        self.driver.find_element_by_name("passwordd").send_keys("1")
        time.sleep(10)
        # 手动输入验证码
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        time.sleep(3)
        message = self.driver.find_element_by_xpath(".//*[@id='loginForm']/h4").text
        self.assertEqual(message, "登录：账号格式错误")
        # self.assertEqual(self.driver.current_url, "http://dev.llvision.com:25008/index.html")

if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestSuite
    # suite.addTest(Test002_loginerror("test_loginerror1"))
    # # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = "D:/搜狗高速下载/Python-master/Case/result.html"
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner(fp, "测试报告", "用例执行情况：")
    # runner.run(suite)
    # fp.close()
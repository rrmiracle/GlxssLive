import time
import unittest
from HTMLTestRunner import HTMLTestRunner


fr = 'D:/搜狗高速下载/Python-master/Case'
dicover = unittest.defaultTestLoader.discover(fr, pattern="Test009*.py")


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fp = open(fr+now+"result.html", 'wb')
    runner = HTMLTestRunner(fp, "GLXSS Live 测试报告", "用例执行情况：")
    runner.run(dicover)
    fp.close()
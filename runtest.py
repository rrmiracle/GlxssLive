import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import os


fr = os.getcwd()
fp = fr+'\GlxssLive_web\TestCase'
fp = fp.replace('\\', '/')
discover = unittest.defaultTestLoader.discover(fp, pattern="Test*.py")


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    fs = fr+'\GlxssLive_web\Report'
    fs = fs.replace('\\', '/')
    fs = open(fs + '/' + now + "result.html", 'wb')
    runner = HTMLTestRunner(stream=fs, title="GLXSS Live 测试报告",  description="用例执行情况：")
    runner.run(discover)
    fs.close()
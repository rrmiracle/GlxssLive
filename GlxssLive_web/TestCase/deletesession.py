import time
import unittest
from selenium import webdriver
from GlxssLive_web.TestCase.Page_obj.sidemenuPage import sidemenu
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def input(self, username, password, code=""):
        self.driver.find_element_by_name("usernamee").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_name("codee").send_keys(code)

    def confirm(self):
        self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()

    def login(self):
        self.driver.get("https://jdev.llvision.com")
        time.sleep(5)
        self.input("gongren3@qq.com", "123456")
        time.sleep(10)
        #手动输入验证码
        self.confirm()

class mysession(sidemenu):

    mysession_loc = (By.XPATH, ".//*[@id='side-menu']/li[2]/ul/li[1]/a")
    session_loc = (By.LINK_TEXT, "工作管理")
    OK_loc = (By.XPATH, "html/body/div[3]/div[7]/button[2]")

    def open_mysession(self):
        self.expand()
        self.find_element(*self.session_loc).click()
        self.find_element(*self.mysession_loc).click()
        time.sleep(1)
        self.driver.switch_to.frame(1)
        time.sleep(1)

    def makesure(self):
        self.confirm()
        time.sleep(1)
        self.find_element(*self.OK_loc).click()


class test_stability(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        print("start")

    def tearDown(self):
        # self.driver.quit()
        print("finish")

    def test_stability(self):
        l = Login(self.driver)
        l.login()
        m = mysession(self.driver)
        m.open_mysession()
        time.sleep(1)
        checkbox = ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span"
        while(True):
            self.driver.find_element_by_xpath(checkbox).click()
            self.driver.find_element(By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[1]/div/a[3]/i").click()
            time.sleep(1)
            m.makesure()
            time.sleep(1)


if __name__ == "__main__":
    unittest.main()
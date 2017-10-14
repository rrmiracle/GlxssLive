from selenium.webdriver.common.by import By
from .Page import Page
import time


class sidemenu(Page):
    '''侧边栏菜单'''

    url = "/login.html"

    def verify_page(self):
        return self.on_page()


    side_menu_loc = (By.XPATH, ".//*[@id='page-wrapper']/div[1]/nav/div/a")
    drop_down_loc = (By.XPATH, ".//*[@id='side-menu']/li[1]/div[1]/a/span/span[2]/b")
    logout_loc = (By.XPATH, ".//*[@id='side-menu']/li[1]/div[1]/ul/li[3]/a")
    profile_loc = (By.XPATH, ".//*[@id='side-menu']/li[1]/div[1]/ul/li[1]/a")

    def expand(self):
        self.find_element(*self.side_menu_loc).click()
        time.sleep(1)

    def drop_down_menu(self):
        self.find_element(*self.drop_down_loc).click()
        time.sleep(1)

    def open_profile(self):
        self.expand()
        self.drop_down_menu()
        self.find_element(*self.profile_loc).click()
        time.sleep(1)
        self.switch_to_frame()
        time.sleep(1)

    def logout(self):
        self.expand()
        self.drop_down_menu()
        self.find_element(*self.logout_loc).click()
        time.sleep(1)

    tagname_loc = (By.XPATH, ".//*[@id='perapp']/div/div/div/div[1]/h5")
    result_loc = (By.XPATH, "html/body/div[3]/h2")

    def tagname(self):
        return self.find_element(*self.tagname_loc).text

    def result(self):
        return self.find_element(*self.result_loc).text

    def success(self):
        return self.result() == "操作成功"

    reason_loc = (By.XPATH, "html/body/div[3]/p")

    def reason(self):
        return self.find_element(*self.reason_loc).get_attribute("innerText")


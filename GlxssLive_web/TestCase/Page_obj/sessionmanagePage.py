from selenium.webdriver.common.by import By
from .sidemenuPage import sidemenu
import time
from selenium.webdriver.common.keys import Keys


class sessionmanage(sidemenu):

    tagname_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[1]/h5")
    sub_tagname_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div[1]/h5")

    def verify(self):
        return self.tagname() == "会话管理"

    workmanage_loc = (By.LINK_TEXT, "工作管理")
    session_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[2]/ul/li[2]/a")

    def open_sessionmanage(self):
        self.expand()
        self.find_element(*self.workmanage_loc).click()
        time.sleep(1)
        self.find_element(*self.session_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    check_button_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[1]/div/a[1]/i")
    modify_button_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[1]/div/a[2]/i")
    delete_button_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[1]/div/a[3]/i")

    def check(self):
        self.find_element(*self.check_button_loc).click()
        time.sleep(1)

    checkbox_1_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span")
    checkbox_2_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span")

    def session_check(self):
        self.find_element(*self.checkbox_1_loc).click()
        time.sleep(1)
        self.check()
        time.sleep(1)

    check_back_button_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[2]/div/div/div/a")

    def check_back(self):
        self.find_element(*self.check_back_button_loc).click()
        time.sleep(1)

    session_modify_name_loc = (By.NAME, "wmmManager.roomName")
    session_modify_keyword_loc = (By.NAME, "wmmManager.keyword")

    def _name(self, name):
        self.find_element(*self.session_modify_name_loc).send_keys(name)

    def name_clear(self):
        js = "var q = document.getElementsByName('wmmManager.roomName')[0]; return q.value"
        q = len(self.driver.execute_script(js))
        for i in range(0, q):
            self._name(Keys.BACK_SPACE)

    def _keyword(self, keyword):
        self.find_element(*self.session_modify_name_loc).send_keys(keyword)

    def keyword_clear(self):
        js = "var q = document.getElementsByName('wmmManager.keyword')[0]; return q.value"
        q = len(self.driver.execute_script(js))
        for i in range(0, q):
            self._keyword(Keys.BACK_SPACE)

    def session_modify(self, name, keyword):
        self._name(name)
        self._keyword(keyword)

    modify_save_button_loc = (By.XPATH, ".//*[@id='wssessionroomForm']/div[4]/div/button")
    modify_back_button_loc = (By.XPATH, ".//*[@id='wssessionroomForm']/div[4]/div/a")

    list_name_loc = (By.XPATH, ".//*[@id='wmmapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[4]")

    def name_list(self):
        return self.find_element(*self.list_name_loc).get_attribute("innerText")

    error_hint_name_loc = (By.ID, "wmmManager.roomName-error")
    error_hint_keyword_loc = (By.ID, "wmmManager.keyword-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_keyword(self):
        return self.find_element(*self.error_hint_keyword_loc).text





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

    def expand(self):
        self.find_element(*self.side_menu_loc).click()
        time.sleep(1)

    def drop_down_menu(self):
        self.find_element(*self.drop_down_loc).click()
        time.sleep(1)

    def logout(self):
        self.expand()
        self.drop_down_menu()
        self.find_element(*self.logout_loc).click()
        time.sleep(1)

    result_loc = (By.XPATH, "html/body/div[3]/h2")

    def result(self):
        return self.find_element(*self.result_loc).text

    def success(self):
        return self.result() == "操作成功"

    reason_loc = (By.XPATH, "html/body/div[3]/p")

    def reason(self):
        return self.find_element(*self.reason_loc).get_attribute("innerText")

    company_loc = (By.ID, "bsType_chosen")
    my_company_loc = (By.XPATH, ".//*[@id='bsType_chosen']/div/ul/li[1]")

    def select_company(self):
        self.find_element(*self.company_loc).click()
        time.sleep(1)
        self.find_element(*self.my_company_loc).click()
        time.sleep(1)

    def company_status(self):
        return self.find_element(*self.company_loc).get_property("isContentEditable")

    confirm_button_loc = (By.XPATH, "html/body/div[3]/div[7]/button[2]")
    cancel_button_loc = (By.XPATH, "html/body/div[3]/div[7]/button[1]")

    def confirm(self):
        self.find_element(*self.confirm_button_loc).click()
        time.sleep(1)

    def cancel(self):
        self.find_element(*self.cancel_button_loc).click()
        time.sleep(1)

    tagname_loc = None
    sub_tagname_loc = None

    def tagname(self):
        return self.find_element(*self.tagname_loc).text

    def sub_tagname(self):
        return self.find_element(*self.sub_tagname_loc).text

    add_button_loc = None
    modify_button_loc = None
    delete_button_loc = None

    def add(self):
        self.find_element(*self.add_button_loc).click()
        time.sleep(1)

    def modify(self):
        self.find_element(*self.modify_button_loc).click()
        time.sleep(1)

    def delete(self):
        self.find_element(*self.delete_button_loc).click()
        time.sleep(1)

    checkbox_1_loc = None
    checkbox_2_loc = None

    def select(self):
        self.find_element(*self.checkbox_1_loc).click()
        time.sleep(1)

    def multi_select(self):
        self.find_element(*self.checkbox_1_loc).click()
        self.find_element(*self.checkbox_2_loc).click()
        time.sleep(1)

    def modify_obj(self):
        self.select()
        self.modify()

    def delete_obj(self):
        self.select()
        self.delete()

    add_save_button_loc = None
    add_back_button_loc = None

    def add_save(self):
        self.find_element(*self.add_save_button_loc).click()

    def add_back(self):
        self.find_element(*self.add_back_button_loc).click()

    modify_save_button_loc = None
    modify_back_button_loc = None

    def modify_save(self):
        self.find_element(*self.modify_save_button_loc).click()

    def modify_back(self):
        self.find_element(*self.modify_back_button_loc).click()




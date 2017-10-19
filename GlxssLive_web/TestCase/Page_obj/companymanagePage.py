from selenium.webdriver.common.by import By
from .devicemanagePage import devicemanage
import time
from selenium.webdriver.support.select import Select


class companymanage(devicemanage):

    def verify(self):
        return self.tagname() == "企业管理"

    company_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[4]/ul/li[3]/a")

    def open_companymanage(self):
        self.expand()
        self.find_element(*self.bsmanage_loc).click()
        time.sleep(1)
        self.find_element(*self.company_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    company_add_name_loc = (By.NAME, "bssBusiness.name")
    company_add_address_loc = (By.NAME, "bssBusiness.address")
    company_add_limit_loc = (By.NAME, "userLimit")
    company_add_server_loc = (By.NAME, "bssBusiness.resourceServer")
    company_add_trade_loc = (By.ID, "trade_chosen")
    company_add_type_loc = (By.ID, "type_chosen")

    def _name(self, name):
        self.find_element(*self.company_add_name_loc).send_keys(name)

    def name_clear(self):
        self.find_element(*self.company_add_name_loc).clear()

    def _server(self, server):
        self.find_element(*self.company_add_server_loc).send_keys(server)

    def server_clear(self):
        self.find_element(*self.company_add_server_loc).clear()

    def _address(self, address):
        self.find_element(*self.company_add_address_loc).send_keys(address)

    def address_clear(self):
        self.find_element(*self.company_add_address_loc).clear()

    def _limit(self, limit):
        self.find_element(*self.company_add_limit_loc).send_keys(limit)

    def limit_clear(self):
        self.find_element(*self.company_add_limit_loc).clear()

    def add_company(self, name, server, address, limit):
        self._name(name)
        self._server(server)
        self._address(address)
        self._limit(limit)
        time.sleep(1)

    company_add_trade_1_loc = (By.XPATH, ".//*[@id='trade_chosen']/div/ul/li[1]")
    company_add_trade_2_loc = (By.XPATH, ".//*[@id='trade_chosen']/div/ul/li[2]")
    company_add_trade_3_loc = (By.XPATH, ".//*[@id='trade_chosen']/div/ul/li[3]")
    company_add_trade_4_loc = (By.XPATH, ".//*[@id='trade_chosen']/div/ul/li[4]")

    def select_trade(self, type=1):
        self.find_element(*self.company_add_trade_loc).click()
        time.sleep(1)
        if type == 1:
            self.find_element(*self.company_add_trade_1_loc).click()
        elif type == 2:
            self.find_element(*self.company_add_trade_2_loc).click()
        elif type == 3:
            self.find_element(*self.company_add_trade_3_loc).click()
        elif type == 4:
            self.find_element(*self.company_add_trade_4_loc).click()
        time.sleep(1)

    company_add_type_1_loc = (By.XPATH, ".//*[@id='type_chosen']/div/ul/li[1]")
    company_add_type_2_loc = (By.XPATH, ".//*[@id='type_chosen']/div/ul/li[2]")
    company_add_type_3_loc = (By.XPATH, ".//*[@id='type_chosen']/div/ul/li[3]")
    company_add_type_4_loc = (By.XPATH, ".//*[@id='type_chosen']/div/ul/li[4]")
    company_add_type_5_loc = (By.XPATH, ".//*[@id='type_chosen']/div/ul/li[5]")

    def select_type(self, type=1):
        self.find_element(*self.company_add_type_loc).click()
        time.sleep(1)
        if type == 1:
            self.find_element(*self.company_add_type_1_loc).click()
        elif type == 2:
            self.find_element(*self.company_add_type_2_loc).click()
        elif type == 3:
            self.find_element(*self.company_add_type_3_loc).click()
        elif type == 4:
            self.find_element(*self.company_add_type_4_loc).click()
        elif type == 5:
            self.find_element(*self.company_add_type_5_loc).click()
        time.sleep(1)

    add_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[9]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[9]/div/a")

    def modify_trade(self):
        if self.find_element(*self.company_add_trade_loc).text != "制作行业":
            self.select_trade(1)
        else:
            self.select_trade(2)

    def modify_type(self):
        if self.find_element(*self.company_add_type_loc).text != "创业公司":
            self.select_type(1)
        else:
            self.select_type(2)

    company_modify_contact_loc = (By.NAME, "selected")

    def modify_contact(self, currentcontact):
        select = self.find_element(*self.company_modify_contact_loc)
        str = select.text
        q = str.split('\n')
        a = list(filter(lambda x: x != currentcontact, q))
        if len(a) > 0:
            Select(select).select_by_visible_text(a[0])
        else:
            print("There is no other contact")
            Select(select).select_by_visible_text(currentcontact)

    list_contact_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[9]")

    def current_contact(self):
        return self.find_element(*self.list_contact_loc).text

    def recovery(self, currentcontact):
        select = self.find_element(*self.company_modify_contact_loc)
        Select(select).select_by_visible_text(currentcontact)

    list_businesscode_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[2]/div/table/tbody/tr/td[7]")

    def businesscode_list(self):
        return self.find_element(*self.list_businesscode_loc).text

    error_hint_name_loc = (By.ID, "bssBusiness.name-error")
    error_hint_address_loc = (By.ID, "bssBusiness.address-error")
    error_hint_server_loc = (By.ID, "bssBusiness.resourceServer-error")
    error_hint_trade_loc = (By.ID, "trade-error")
    error_hint_limit_loc = (By.ID, "userLimit-error")
    error_hint_type_loc = (By.ID, "type-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_address(self):
        return self.find_element(*self.error_hint_address_loc).text

    def error_trade(self):
        return self.find_element(*self.error_hint_trade_loc).text

    def error_limit(self):
        return self.find_element(*self.error_hint_limit_loc).text

    def error_type(self):
        return self.find_element(*self.error_hint_type_loc).text

    def error_server(self):
        return self.find_element(*self.error_hint_server_loc).text






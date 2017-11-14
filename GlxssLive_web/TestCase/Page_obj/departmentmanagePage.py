from selenium.webdriver.common.by import By
from .devicemanagePage import devicemanage
import time
from selenium.webdriver.support.select import Select


class departmentmanage(devicemanage):

    def verify(self):
        return self.tagname() == "部门管理"

    department_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[4]/ul/li[1]/a")

    def open_departmentmanage(self):
        self.expand()
        self.find_element(*self.bsmanage_loc).click()
        time.sleep(1)
        self.find_element(*self.department_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    department_add_name_loc = (By.NAME, "bssDept.name")
    department_add_order_loc = (By.NAME, "orderNum")
    department_add_dept_loc = (By.NAME, "bssDeptSelect.parentId")

    def _name(self, name):
        self.find_element(*self.department_add_name_loc).send_keys(name)

    def name_clear(self):
        self.find_element(*self.department_add_name_loc).clear()

    def _order(self, number):
        self.find_element(*self.department_add_order_loc).send_keys(number)

    def order_clear(self):
        self.find_element(*self.department_add_order_loc).clear()

    def add_department(self, name, number):
        self._name(name)
        self._order(number)
        time.sleep(1)

    add_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[6]/div/a")

    def change_dept(self):
        select = self.find_element(*self.department_add_dept_loc)
        str = []
        for i in Select(select).options:
            str.append(i.get_attribute("innerText"))
        option = Select(select).all_selected_options
        if len(option) > 0:
            superior = option[0].get_attribute("innerText")
        else:
            superior = None
        curdept = self.find_element(*self.department_add_name_loc).get_attribute("value")
        q = list(filter(lambda x: x != curdept and x != superior, str))
        Select(select).select_by_visible_text(q[0])

    list_loc = (By.TAG_NAME, "tbody")
    list_row_loc = (By.TAG_NAME, "tr")
    list_column_loc = (By.TAG_NAME, "td")
    list_checkbox_loc = (By.CLASS_NAME, "lbl")

    def deptstatus(self, type = 1):
        trs = self.find_element(*self.list_loc).find_elements(*self.list_row_loc)
        q = []
        p = []
        depname = []
        # 所有有子部门的部门集合
        for tr in trs:
            tds = tr.find_elements(*self.list_column_loc)
            depname.append(tds[2].text)
        for tr in trs:
            tds = tr.find_elements(*self.list_column_loc)
            if tds[1].text not in depname and tds[4].text == "未删除":
                q.append(tr)
            if tds[1].text in depname and tds[4].text == "未删除":
                p.append(tr)
        # 没有子部门的部门集合
        if type == 1:
            if len(q) > 0:
                q[0].find_element(*self.list_checkbox_loc).click()
                time.sleep(1)
        # 有子部门的部门集合
        if type == 2:
            if len(p) > 0:
                p[0].find_element(*self.list_checkbox_loc).click()
                time.sleep(1)
            else:
                print("Please set superior department first")

    list_name_loc = (By.XPATH, ".//*[@id='bssapp']/div/div/div/div[3]/div/table/tbody/tr/td[2]")

    def name_list(self):
        return self.find_element(*self.list_name_loc).get_attribute("innerText")

    def setself(self):
        curdept = self.find_element(*self.department_add_name_loc).get_attribute("value")
        select = self.find_element(*self.department_add_dept_loc)
        Select(select).select_by_visible_text(curdept)
        time.sleep(1)

    error_hint_name_loc = (By.ID, "bssDept.name-error")
    error_hint_company_loc = (By.ID, "bssDept-error")
    error_hint_order_loc = (By.ID, "orderNum-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_company(self):
        return self.find_element(*self.error_hint_company_loc).text

    def error_order(self):
        return self.find_element(*self.error_hint_order_loc).text




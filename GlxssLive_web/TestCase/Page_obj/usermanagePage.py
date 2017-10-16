from selenium.webdriver.common.by import By
from .sidemenuPage import sidemenu
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class usermanage(sidemenu):
    '''用户管理页面'''

    def verify(self):
        return self.tagname() == "用户管理"

    usermanage_loc = (By.LINK_TEXT, "用户管理")
    user_management_loc = (By.XPATH, ".//*[@id='side-menu']/li[3]/ul/li[1]/a")

    def open_usermanage(self):
        self.expand()
        self.find_element(*self.usermanage_loc).click()
        time.sleep(1)
        self.find_element(*self.user_management_loc).click()
        self.switch_to_frame()
        time.sleep(1)

    tagname_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[1]/h5")
    sub_tagname_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div[1]/h5")

    def tagname(self):
        return self.find_element(*self.tagname_loc).text

    def sub_tagname(self):
        return self.find_element(*self.sub_tagname_loc).text

    add_button_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[1]/div/a[1]/i")
    modify_button_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[1]/div/a[2]/i")
    delete_button_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[1]/div/a[3]/i")

    checkbox_1_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[1]/label/span")
    checkbox_2_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[2]/td[1]/label/span")

    def add(self):
        self.find_element(*self.add_button_loc).click()
        time.sleep(1)

    def modify(self):
        self.find_element(*self.modify_button_loc).click()
        time.sleep(1)

    def delete(self):
        self.find_element(*self.delete_button_loc).click()
        time.sleep(1)

    def select(self):
        self.find_element(*self.checkbox_1_loc).click()
        time.sleep(1)

    def multi_select(self):
        self.find_element(*self.checkbox_1_loc).click()
        self.find_element(*self.checkbox_2_loc).click()
        time.sleep(1)

    def modify_user(self):
        self.select()
        self.modify()

    def delete_user(self):
        self.select()
        self.delete()

    user_add_name_loc = (By.NAME, "userManager.username")
    user_add_description_loc = (By.NAME, "userManager.introduce")
    user_add_password_loc = (By.NAME, "password")
    user_add_confirmpsd_loc = (By.NAME, "confirm")
    user_add_email_loc = (By.NAME, "email")
    user_add_phone_loc = (By.NAME, "phone")
    user_add_company_loc = (By.NAME, "userManager.bsName")
    user_add_department_loc = (By.ID, "deptType_chosen")
    user_add_role_loc = (By.NAME, "userCheckList")

    def name(self, name):
        self.find_element(*self.user_add_name_loc).send_keys(name)

    def name_clear(self):
        self.find_element(*self.user_add_name_loc).clear()
        time.sleep(1)

    def email(self, email):
        self.find_element(*self.user_add_email_loc).send_keys(email)

    def password(self, password):
        self.find_element(*self.user_add_password_loc).send_keys(password)

    def confirm_password(self, confirmpsd):
        self.find_element(*self.user_add_confirmpsd_loc).send_keys(confirmpsd)

    def phone(self, phone):
        self.find_element(*self.user_add_phone_loc).send_keys(phone)

    def department(self):
        return self.find_element(*self.user_add_department_loc)

    def description(self, description):
        self.find_element(*self.user_add_description_loc).send_keys(description)

    def description_clear(self):
        time.sleep(1)
        js = "var q = document.getElementsByName('userManager.introduce')[0]; return q.value"
        q = len(self.script(js))
        for i in range(0, q):
            self.find_element(*self.user_add_description_loc).send_keys(Keys.BACK_SPACE)
        time.sleep(1)

    def role(self):
        self.find_element(*self.user_add_role_loc).click()

    def add_user(self, name, email, password, confirmpsd, phone, description=""):
        self.name(name)
        self.email(email)
        self.password(password)
        self.confirm_password(confirmpsd)
        self.phone(phone)
        self.description(description)

    def modify_user_input(self, name, description=""):
        self.name(name)
        self.description(description)

    def status(self):
        bsname = self.find_element(*self.user_add_company_loc)
        email = self.find_element(*self.user_add_email_loc)
        phone = self.find_element(*self.user_add_phone_loc)
        return bsname.get_attribute("disabled"), email.get_attribute("disabled"), phone.get_attribute("disabled")

    user_add_department_1_loc = (By.XPATH, ".//*[@id='deptType_chosen']/div/ul/li[1]")
    user_add_department_2_loc = (By.XPATH, ".//*[@id='deptType_chosen']/div/ul/li[2]")

    def change_department(self):
        q = self.department().get_attribute("innerText")
        self.department().click()
        if q == "选择所属部门":
            try:
                self.find_element(*self.user_add_department_1_loc).click()
            except NoSuchElementException:
                print("No department in the company")
        elif q == self.find_element(*self.user_add_department_1_loc).get_attribute("innerText"):
            try:
                self.find_element(*self.user_add_department_2_loc).click()
            except NoSuchElementException:
                print("No other department in the company")
        else:
            self.find_element(*self.user_add_department_1_loc).click()

    user_add_type_loc = (By.XPATH, ".//*[@id='userType_chosen']/a/span")
    user_add_type_worker_loc = (By.XPATH, ".//*[@id='userType_chosen']/div/ul/li[1]")
    user_add_type_expert_loc = (By.XPATH, ".//*[@id='userType_chosen']/div/ul/li[2]")
    user_add_type_expert_un_loc = (By.XPATH, ".//*[@id='userType_chosen']/div/ul/li[3]")

    def type(self, type=1):
        self.find_element(*self.user_add_type_loc).click()
        time.sleep(1)
        if type == 1:
            self.find_element(*self.user_add_type_worker_loc).click()
        elif type == 2:
            self.find_element(*self.user_add_type_expert_loc).click()
        elif type == 3:
            self.find_element(*self.user_add_type_expert_un_loc).click()
        time.sleep(1)

    def change_type(self):
        q = self.find_element(*self.user_add_type_loc).get_attribute("innerText")
        if q == "非专家":
            try:
                p = self.find_elements(*self.user_add_special_checkbox_loc)
                print("============special")
                for i in p:
                    if i.is_selected() == False:
                        i.click()
                self.type(2)
            except NoSuchElementException:
                if self.find_element(*self.user_add_special_loc).get_attribute("innerText") == "暂无数据":
                    print("There is no special in the company, can't change user type")
                else:
                    print("Error")
        else:
            self.type(1)
        time.sleep(1)

    add_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[13]/div/button")
    add_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[13]/div/a")

    def add_save(self):
        self.find_element(*self.add_save_button_loc).click()

    def add_back(self):
        self.find_element(*self.add_back_button_loc).click()

    modify_save_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[11]/div/button")
    modify_back_button_loc = (By.XPATH, ".//*[@id='commentForm']/div[11]/div/a")

    def modify_save(self):
        self.find_element(*self.modify_save_button_loc).click()

    def modify_back(self):
        self.find_element(*self.modify_back_button_loc).click()

    user_add_special_checkbox_loc = (By.NAME, "specialtyCheckList")
    user_add_special_loc = (By.XPATH, ".//*[@id='commentForm']/div[9]/div/ul/li/div/span")

    def change_special(self):
        try:
            q = self.find_elements(*self.user_add_special_checkbox_loc)
            number = 0
            if len(q) > 1:
                # 专业数>1
                for i in q:
                    i.click()
                    if i.is_selected():
                        number = number+1
                if number == 0:
                    q[0].click()
            else:
                # 专业数=1
                if q[0].is_selected():
                    print("Can't change special")
                else:
                    q[0].click()
        except NoSuchElementException:
            if self.find_element(*self.user_add_special_loc).get_attribute("innerText") == "暂无数据":
                print("No special defined")
            else:
                print("Error")

    list_email_loc = (By.XPATH, ".//*[@id='userapp']/div/div/div/div[2]/div/table/tbody/tr[1]/td[7]")

    def email_list(self):
        return self.find_element(*self.list_email_loc).get_attribute("innerText")

    error_hint_name_loc = (By.ID, "userManager.username-error")
    error_hint_type_loc = (By.ID, "userType-error")
    error_hint_company_loc = (By.ID, "bsType-error")
    error_hint_password_loc = (By.ID, "psd-error")
    error_hint_confirmpsd_loc = (By.ID, "confirm-error")
    error_hint_email_loc = (By.ID, "userManager.email-error")
    error_hint_phone_loc = (By.ID, "phone-error")

    def error_name(self):
        return self.find_element(*self.error_hint_name_loc).text

    def error_type(self):
        return self.find_element(*self.error_hint_type_loc).text

    def error_company(self):
        return self.find_element(*self.error_hint_company_loc).text

    def error_password(self):
        return self.find_element(*self.error_hint_password_loc).text

    def error_confirmpsd(self):
        return self.find_element(*self.error_hint_confirmpsd_loc).text

    def error_email(self):
        return self.find_element(*self.error_hint_email_loc).text

    def error_phone(self):
        return self.find_element(*self.error_hint_phone_loc).text







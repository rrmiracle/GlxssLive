from selenium.webdriver.common.by import By
from .Page import Page
import time
from selenium.webdriver.common.action_chains import ActionChains


class session(Page):

    websocket_notification_loc = (By.ID, "gritter-item-1")

    def websocket_notification(self):
       return self.find_element(*self.websocket_notification_loc).get_attribute("innerText")

    status_dropdown_loc = (By.CLASS_NAME, "drop1")
    status_free_loc = (By.LINK_TEXT, "空闲中")
    status_busy_loc = (By.LINK_TEXT, "置忙")

    def status(self):
        return self.find_element(*self.status_dropdown_loc).get_attribute("innerText")

    def change_status(self):
        ActionChains(self.driver).click(self.find_element(*self.status_free_loc)).perform()
        time.sleep(1)
        self.find_element(*self.status_busy_loc).click()
        time.sleep(1)

    message_part_loc = (By.CLASS_NAME, "chat-form")
    send_button_loc = (By.CLASS_NAME, "fa")
    session_from_loc = (By.CLASS_NAME, "ibox-title")
    session_message_loc = (By.TAG_NAME, "textarea")
    send_picture_button_loc = (By.TAG_NAME, "input")

    def message(self, message):
        self.find_element(*self.message_part_loc).find_element(*self.session_message_loc).send_keys(message)

    def send(self):
        self.find_element(*self.message_part_loc).find_elements(*self.send_button_loc)[1].click()
        time.sleep(1)

    def session_from(self):
        return self.find_element(*self.session_from_loc).get_attribute("innerText")

    def send_pic(self):
        self.find_element(*self.message_part_loc).find_element(*self.send_picture_button_loc).click()

    alert_message_loc = (By.XPATH, ".//*[@id='myCue']/div/div/div[2]/strong")

    def alert(self):
        return self.find_element(*self.alert_message_loc).text


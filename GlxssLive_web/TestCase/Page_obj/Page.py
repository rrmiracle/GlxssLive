from GlxssLive_web.Data.Data import Data

class Page(object):
    '''基础类，用于所有页面的继承'''

    def __init__(self, driver, base_url=Data.url):
        self.driver = driver
        self.base_url = base_url

    def _open(self, url):
        self.url = self.base_url+url
        self.driver.get(url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        # print(self.url)
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.excute_script(src)

    def switch_to_frame(self):
        self.driver.switch_to.frame(0)
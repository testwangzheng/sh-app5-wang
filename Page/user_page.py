from Base.Base import Base
import Page


class User_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def get_mylike_text(self):
        return self.search_element(Page.my_like_id).text()

    def click_set_btn(self):
        self.click_element(Page.setting_btn_id)
from Base.Base import Base
import Page


class Zhuce_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_go_login(self):
        self.click_element(Page.exits_account_btn_id)

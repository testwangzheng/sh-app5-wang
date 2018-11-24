from Base.Base import Base
import Page


class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def exit(self,nu=1):
        self.huadong(1)
        self.click_element(Page.logout_btn_id)
        if nu == 1:
            self.click_element(Page.access_logout_btn_id)
        else:
            self.click_element(Page.dismiss_log_out_btn_id)

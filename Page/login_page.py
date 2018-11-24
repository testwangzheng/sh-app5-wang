from selenium.webdriver.common.by import By
from Base.Base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, phone, passwd):
        """登录 操作"""
        self.send_element(Page.login_name_id, phone)
        self.send_element(Page.login_passwd_id, passwd)
        self.click_element(Page.login_btn_id)

    def click_close(self):
        """退出 登录页"""
        self.click_element()

    def get_login_text(self):
        return self.search_element(Page.dismiss_log_out_btn_id).text()
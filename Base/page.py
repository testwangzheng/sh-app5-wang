from Page.home_page import Home_Page
from Page.login_page import Login_Page
from Page.setting_page import Setting_Page
from Page.user_page import User_Page
from Page.zhuce_page import Zhuce_Page

"""统一入口类"""
class Page:
    def __init__(self,driver):
        self.driver = driver

    def get_home_page(self):
        """返回 首页 类"""
        return Home_Page(self.driver)
    def get_zhuce_page(self):
        """返回 注册 类"""
        return Zhuce_Page(self.driver)
    def get_login_page(self):
        """返回 登录 类"""
        return Login_Page(self.driver)
    def get_user_page(self):
        """返回 个人中心 类"""
        return User_Page(self.driver)
    def get_setting_page(self):
        """返回 设置 类"""
        return Setting_Page(self.driver)

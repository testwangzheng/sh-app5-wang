import os,sys,pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())

from Base.page import Page
from Base.get_driver import get_driver
from Base.get_data import Get_Data

def get_login_data():
    """ 取 数据 """
    # 登录成功
    suc_list = []
    # 登录失败
    fal_list = []
    login_data = Get_Data().get_yaml_data("login_data.yml").get("login_data")
    for i in login_data.keys():
        if login_data.get(i).get("get_toast"):
            fal_list.append((i, login_data.get(i).get("phone"), login_data.get(i).get("passwd"),
                              login_data.get(i).get("get_toast"), login_data.get(i).get("expect_data")))
        else:
            suc_list.append((i, login_data.get(i).get("phone"), login_data.get(i).get("passwd"),
                            login_data.get(i).get("expect_data")))
        return {"suc":suc_list,"fal":fal_list}
class Test_01:
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc",
                                        "com.yunmall.ymctoc.ui.activity.MainActivity"))
    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("i, phone, passwd, toast, expect", get_login_data().get("suc"))
    def test_001(self, i, phone, passwd ,toast, expect):
        """测试 登录  成功"""
        # 首页，点击 -->我
        self.page_obj.get_home_page().click_my_btn()
        # 注册页， 点击 -->已有账号去登陆
        self.page_obj.get_zhuce_page().click_go_login()
        """登录 操作"""
        # 输入，手机号 密码 点击登录
        self.page_obj.get_login_page().login(phone, passwd)
        try:
            # 取 我的收藏
            mylike_text = self.page_obj.get_user_page().get_mylike_text()
            # 执行 退出  操作
            self.page_obj.get_user_page().click_set_btn()
            self.page_obj.get_setting_page().exit()
            # 断言
            assert expect in mylike_text
        except TimeoutException:
            # 关闭 登录页
            self.page_obj.get_login_page().click_close()
            assert False

    @pytest.mark.parametrize("i, phone, passwd, get_toast, expect_data", get_login_data().get("fal"))
    def test_002(self, i, phone, passwd, get_toast, expect_data):
        """失败测试用例"""
        # 点击我
        self.page_obj.get_home_page().click_my_btn()
        # 点击已有账号去登录
        self.page_obj.get_zhuce_page().click_go_login()
        # 执行登陆操作
        self.page_obj.get_zhuce_page().click_go_login()
        try:
            # 获取toast
            toast_message = self.page_obj.get_login_page().get_toast(get_toast)
            # 登录按钮是否存在
            if_login = self.page_obj.get_login_page().if_login_btn()
            # 关闭页面
            self.page_obj.get_login_page().close_login_page()
            # 断言
            assert toast_message == expect_data and if_login
        except TimeoutException:
            # 执行退出操作
            # 点击设置
            self.page_obj.get_user_page().click_set_btn()
            # 点击退出
            self.page_obj.get_setting_page().exit()
            # 断言
            assert False

from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver
    def search_element(self, loc, timeout=10, poll_frequency=1):
        """
        定位单个元素
        :param loc_type: 远元祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))
    def search_elements(self, loc, timeout=10, poll_frequency=1):
        """
        定位单个元素
        :param loc_type: 远元祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
    def click_element(self, loc, timeout=10, poll_frequency=1):
        """
        点击元素
        :param loc_type: 祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()
    def send_element(self, loc, text, timeout=10, poll_frequency=1):
        """
        输入元素
        :param loc: 祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param text: 发送文本
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        input_data = self.search_element(loc, timeout, poll_frequency)
        # 清空输入框
        input_data.clear()
        # 输入
        input_data.send_keys(text)

    def huadong(self,nu):
        """滑动屏幕"""
        fbl = self.driver.get_window_side()
        width = fbl.get("width")
        height = fbl.get("height")
        if nu == 1:
            self.driver.swit(width*0.5,height*0.8,width*0.5,height*0.3)
        if nu == 2:
            self.driver.swit(width*0.5,height*0.3,width*0.5,height*0.8)
        if nu == 3:
            self.driver.swit(width*0.8,height*0.5,width*0.3,height*0.5)
        if nu == 4:
            self.driver.swit(width*0.3,height*0.5,width*0.8,height*0.5)




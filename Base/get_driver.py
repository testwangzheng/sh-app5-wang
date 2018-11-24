from appium import webdriver

"""声明driver类"""
def get_driver(apk,act):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    #  支持 定位、获取 手机的 弹窗 内容
    desired_caps['automationName'] = 'Uiautomator2'
    # app的信息
    # desired_caps['appPackage'] = 'com.android.mms'
    # desired_caps['appActivity'] = '.ui.ConversationList'
    desired_caps['appPackage'] = apk
    desired_caps['appActivity'] = act

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
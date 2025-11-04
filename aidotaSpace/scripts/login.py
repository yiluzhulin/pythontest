import sys
import time
from base.yaml_unit import MyYaml

'''
平台登录
'''


class Login:
    def __init__(self, browser, env):
        self.browser = browser
        self.data = MyYaml()
        self.env = env
        # 文件标识，用于查找元素定位配置文件
        self.fun_flag = "login"

    def login(self):
        '''
        登录IAM平台
        :return:
        '''
        # 获取平台地址、用户名、密码
        url = self.data.get_element("var", self.env + ".url")
        user = self.data.get_element("var", self.env + ".user")
        pwd = self.data.get_element("var", self.env + ".pwd")

        self.browser.get(url)

        try:
            # 设置用户名、密码，并登录
            self.browser.input('xpath', self.fun_flag, "user", user)
            self.browser.input('xpath', self.fun_flag, "pwd", pwd)
            self.browser.button('xpath', self.fun_flag, "but")
            time.sleep(5)

            # 点击进入智能诊断平台
            self.browser.button('xpath', self.fun_flag, "aidota")
            time.sleep(5)

            # 切换到最新窗口的句柄
            self.browser.switch_to_window(-1)
            # 将页面比例缩放到80%
            self.browser.set_style_zoom("0.8")
            time.sleep(1)

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

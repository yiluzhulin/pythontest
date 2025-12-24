import time
from base.yaml_unit import MyYaml

'''
AI诊断任务界面操作
'''


class AiTasks:
    def __init__(self, browser, env):
        self.browser = browser
        self.data = MyYaml()
        self.env = env
        # 功能标识，用于查找元素定位配置文件
        self.fun_flag = "task"
        self.vin = self.data.get_element('var', self.env + ".vin")

    def entrance(self):
        '''
        进入AI诊断任务界面，并进行基本操作
        :return:
        '''
        # 展开AI诊断管理目录
        self.browser.button('xpath', self.fun_flag, "entrance")

        # 打开AI诊断任务页面
        self.browser.button('xpath', self.fun_flag, "tasks")
        time.sleep(2)

        # 新增任务
        # 打开新增任务窗口
        self.browser.button('xpath', self.fun_flag, "addTask.entrance")
        # 设置vin
        self.browser.input('xpath', self.fun_flag, "addTask.vin", self.vin)

        time.sleep(5)

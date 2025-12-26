import time
import sys
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
        self.test_flag = self.data.get_element('var', "flag")

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

        # # 新增任务
        # self.add_task()
        #
        # # 任务查询
        # self.task_search(["taskName","model","config","creater","status","vin"])
        #
        # # 配置列
        # self.task_column_config()

        # 查看任务详情
        self.task_detail()

        time.sleep(5)

    def add_task(self):
        '''
        新增AI诊断任务
        :return:
        '''
        try:
            # 打开新增任务窗口
            self.browser.button('xpath', self.fun_flag, "addTask.entrance")
            # 设置vin
            self.browser.input('xpath', self.fun_flag, "addTask.vin", self.vin)
            # 设置场景组
            self.browser.button('xpath', self.fun_flag, "addTask.sceneGroupName")
            self.browser.input('xpath', self.fun_flag, "addTask.sceneGroupName", self.test_flag)
            self.browser.button('xpath', self.fun_flag, "addTask.sceneGroupName_sel")
            # 设置场景
            self.browser.button('xpath', self.fun_flag, "addTask.sceneName")
            self.browser.input('xpath', self.fun_flag, "addTask.sceneName", self.test_flag)
            self.browser.button('xpath', self.fun_flag, "addTask.sceneName_sel")
            # 场景不配车辆弹框点击确定
            self.browser.button('xpath', self.fun_flag, "addTask.vinCheck_but")
            # 上传canlin文件
            self.browser.input('xpath', self.fun_flag, "addTask.canlin_upload",
                               "D:\wordspace\\aidotaSpace\\files\canlin信号demo1.xlsx")
            time.sleep(5)
            # 设置故障时间、范围
            self.browser.scroll('ele', 'xpath', self.fun_flag, "addTask.errorTime")
            errorTime = self.data.get_element('var', self.env + ".errorTime")
            startTime = self.data.get_element('var', self.env + ".startTime")
            endTime = self.data.get_element('var', self.env + ".endTime")
            self.browser.input('xpath', self.fun_flag, "addTask.errorTime", errorTime)
            self.browser.clear('xpath', self.fun_flag, "addTask.startTime")
            self.browser.input('xpath', self.fun_flag, "addTask.startTime", startTime)
            self.browser.clear('xpath', self.fun_flag, "addTask.endTime")
            self.browser.input('xpath', self.fun_flag, "addTask.endTime", endTime)
            # 点击确定
            self.browser.button('xpath', self.fun_flag, "addTask.submit_but")
            self.browser.button('xpath', self.fun_flag, "addTask.sceneCheck_but")
        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def task_search(self, conditions=[]):
        '''
        诊断任务查询
        :param conditions: 查询条件列表，默认没有查询条件
        :return:
        '''
        try:
            # 设置查询条件
            for cond in conditions:
                match cond:
                    case "taskName":
                        self.browser.input('xpath', self.fun_flag, "search.taskName", self.test_flag)
                    case "model":
                        model = self.data.get_element('var', self.env + ".model")
                        self.browser.input('xpath', self.fun_flag, "search.model", model)
                    case "config":
                        config = self.data.get_element('var', self.env + ".config")
                        self.browser.input('xpath', self.fun_flag, "search.config", config)
                    case "creater":
                        user = self.data.get_element('var', self.env + ".user")
                        self.browser.input('xpath', self.fun_flag, "search.creater", user)
                    case "status":
                        self.browser.button('xpath', self.fun_flag, "search.status")
                        self.browser.button('xpath', self.fun_flag, "search.status_jxz")
                        self.browser.button('xpath', self.fun_flag, "search.status_zdwc")
                    case "vin":
                        self.browser.input('xpath', self.fun_flag, "search.vin", self.vin)

            # 点击查询按钮
            self.browser.button('xpath', self.fun_flag, "search.search_but")

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def task_detail(self):
        '''
        查看任务详情
        :return:
        '''
        try:
            # 进入配置列界面
            self.browser.button('xpath', self.fun_flag, "detail.entrance")
            # 数据线性
            # 点击查询按钮
            self.browser.button('xpath', self.fun_flag, "detail.signalLineChart_search")
            time.sleep(1)
            # 点击全屏展示按钮
            self.browser.button('xpath', self.fun_flag, "detail.signalLineChart_max")
            time.sleep(1)
            self.browser.button('xpath', self.fun_flag, "detail.signalLineChart_ma_close")


        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def task_column_config(self):
        '''
        配置列
        :return:
        '''
        try:
            # 进入配置列界面
            self.browser.button('xpath', self.fun_flag, "columnConfig.entrance")
            self.browser.button('xpath', self.fun_flag, "columnConfig.column")
            self.browser.button('xpath', self.fun_flag, "columnConfig.submit_but")

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

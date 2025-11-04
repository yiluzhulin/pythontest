import time
import sys
from base.yaml_unit import MyYaml

'''
场景组&场景管理界面操作
'''


class SceneCanvas:
    def __init__(self, browser, env):
        self.browser = browser
        self.data = MyYaml()
        self.env = env
        # 功能标识，用于查找元素定位配置文件
        self.fun_flag = "scene"
        # 自动化测试数据标识
        self.test_flag = self.data.get_element('var', "flag")

    def entrance(self):
        '''
        进入场景组&场景管理界面
        :return:
        '''
        try:
            # 展开AI诊断管理目录
            self.browser.button('xpath', self.fun_flag, "entrance")
            time.sleep(1)

            # 打开场景组&场景管理页面
            self.browser.button('xpath', self.fun_flag, "sceneCanvas")
            time.sleep(3)

            # # 添加场景组
            # self.save_sceneGroup()

            self.save_scene()

            # # 场景查询
            # self.scene_search(["sceneGroupName"])


        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def scene_search(self, conditions=[]):
        '''
        场景查询
        :param conditions: 查询条件列表，默认没有查询条件
        :return:
        '''
        try:
            # 设置查询条件
            for cond in conditions:
                match cond:
                    case "sceneGroupName":
                        self.browser.input('xpath', self.fun_flag, "search.sceneGroupName", self.test_flag)
                    case "sceneName":
                        self.browser.input('xpath', self.fun_flag, "search.sceneName", self.test_flag)
                    case "groupCreateUser":
                        user = self.data.get_element('var', self.env + ".user")
                        self.browser.input('xpath', self.fun_flag, "search.groupCreateUser", user)
                    case "createUser":
                        user = self.data.get_element('var', self.env + ".user")
                        self.browser.input('xpath', self.fun_flag, "search.createUser", user)
                    case "status":
                        self.browser.button('xpath', self.fun_flag, "search.status")
                        time.sleep(1)
                        self.browser.button('xpath', self.fun_flag, "search.status_csz")
                        time.sleep(1)
                        self.browser.button('xpath', self.fun_flag, "search.status_bjz")
                        time.sleep(1)

            # 点击查询按钮
            self.browser.button('xpath', self.fun_flag, "search.search_but")
            time.sleep(3)

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def save_sceneGroup(self):
        '''
        添加场景组
        :return:
        '''
        try:
            # 点击创建场景组
            self.browser.button('xpath', self.fun_flag, "save_sceneGroup.entrance")
            time.sleep(1)

            # 设置场景组名称
            name = self.test_flag + time.strftime("%Y%m%d%H%M%S")
            self.browser.input('xpath', self.fun_flag, "save_sceneGroup.name", name)
            time.sleep(1)

            # 点击确定按钮
            self.browser.button('xpath', self.fun_flag, "save_sceneGroup.but")
            time.sleep(3)

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise


    def save_scene(self):
        '''
        添加场景
        :return:
        '''
        try:
            # 点击创建场景
            self.browser.button('xpath', self.fun_flag, "save_scene.entrance")
            time.sleep(3)

            #设置场景组
            self.browser.input('xpath', self.fun_flag, "save_scene.sceneGroupName_input", self.test_flag)
            time.sleep(1)
            self.browser.button('xpath', self.fun_flag, "save_scene.sceneGroupName")

            # # 设置车型
            # vehicleModel = self.data.get_element("var", self.env + ".vehicleModel")
            #
            # # 点击确定按钮
            # self.browser.button('xpath', self.fun_flag, "save_sceneGroup.but")
            time.sleep(3)

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

# # 调试使用
# if __name__=="__main__":
#     name = "auto" + time.strftime("%Y%m%d%H%M%S")
#     print(name)
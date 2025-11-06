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

            # 打开场景组&场景管理页面
            self.browser.button('xpath', self.fun_flag, "sceneCanvas")

            # # 添加场景组
            # self.save_sceneGroup()

            # self.save_scene()

            # 场景查询
            self.scene_search(["sceneGroupName"])

            # 编辑场景
            self.edit_scene()

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
                        self.browser.button('xpath', self.fun_flag, "search.status_csz")
                        self.browser.button('xpath', self.fun_flag, "search.status_bjz")

            # 点击查询按钮
            self.browser.button('xpath', self.fun_flag, "search.search_but")

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

            # 设置场景组名称
            name = self.test_flag + "cjz" + time.strftime("%Y%m%d%H%M%S")
            self.browser.input('xpath', self.fun_flag, "save_sceneGroup.name", name)

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

            # 设置基本信息
            # 设置场景组
            self.browser.input('xpath', self.fun_flag, "save_scene.sceneGroupName_input", self.test_flag)
            self.browser.button('xpath', self.fun_flag, "save_scene.sceneGroupName")

            # 设置场景
            sceneName = self.test_flag + "cj" + time.strftime("%Y%m%d%H%M%S")
            self.browser.input('xpath', self.fun_flag, "save_scene.sceneName", sceneName)

            # 设置车型
            vehicleModels = self.data.get_element("var", self.env + ".vehicleModels")
            for vehicleModel in vehicleModels:
                self.browser.input('xpath', self.fun_flag, "save_scene.vehicleModels_input", vehicleModel)
                self.browser.button('xpath', self.fun_flag, "save_scene.vehicleModels", vehicleModel)
                self.browser.button('xpath', self.fun_flag, "save_scene.main")

            # 设置IMOS版本
            self.browser.input('xpath', self.fun_flag, "save_scene.imOsVersions_input", "IMOS")
            self.browser.button('xpath', self.fun_flag, "save_scene.imOsVersions")

            # 设置下线日期
            self.browser.button('xpath', self.fun_flag, "save_scene.offlindDate")
            self.browser.button('xpath', self.fun_flag, "save_scene.startDate")
            time.sleep(1)
            self.browser.button('xpath', self.fun_flag, "save_scene.endDate")

            # 点击下一步按钮
            self.browser.button('xpath', self.fun_flag, "save_scene.next_but")
            time.sleep(3)

            # 设置逻辑判断
            self.edit_scene_canvas(["canlin"])

        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def edit_scene_canvas(self, nodes):
        '''
        配置场景逻辑
        :param nodes:需要添加的子任务类型
        :return:
        '''
        for node in nodes:
            match node:
                case "canlin":
                    # 信号子任务
                    self.edit_scene_canvas_canlin("ABSA")

    def edit_scene_canvas_canlin(self, signal):
        '''
        编辑场景的逻辑画布-添加信号子任务
        :return:
        '''
        # 信号子任务
        # 拖动信号子任务到画布
        self.browser.drag('xpath', self.fun_flag, "canvas.canlin.canlin_node", -200, 100)
        self.browser.double_click('xpath', self.fun_flag, "canvas.canlin.new_canlin_node")
        # 信号选择
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.signal_input", signal)
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.signal", signal)
        # 计算配置
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.cond_but")

        self.browser.button('xpath', self.fun_flag, "canvas.canlin.cond_but")
        # 设置运算表达式
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.cond_op", "x1")
        # 设置判断类型
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.cond_dss")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.cond_dss_eq")
        # 设置值
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.cond_val")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.cond_val_num_type")
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.cond_val_num_val", 1)
        # 点击确认
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.but")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.but")

    def edit_scene(self):
        '''
        编辑场景
        :return:
        '''
        self.browser.button('xpath', self.fun_flag, "edit_scene.edit")
        self.browser.button('xpath', self.fun_flag, "edit_scene.canvas")
        self.edit_scene_canvas(["canlin"])
        time.sleep(5)

# # 调试使用
# if __name__=="__main__":
#     name = "//li[span[text()='${var_to_change}']]"
#     name = name.replace("${var_to_change}","EP33-M0-L7")
#     print(name)

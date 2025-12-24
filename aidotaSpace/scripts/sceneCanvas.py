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
        进入场景组&场景管理界面，并执行基本操作
        :return:
        '''
        try:
            # 展开AI诊断管理目录
            self.browser.button('xpath', self.fun_flag, "entrance")

            # 打开场景组&场景管理页面
            self.browser.button('xpath', self.fun_flag, "sceneCanvas")

            # 添加场景组
            self.add_sceneGroup()

            # 添加场景
            self.add_scene()

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

    def add_sceneGroup(self):
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

    def add_scene(self):
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

            # 设置场景逻辑
            # 添加信号子任务
            self.add_scene_canvas_canlin("ABSA")

            # 添加判断子任务
            self.add_scene_canvas_decision()

            # 添加小结子任务
            self.add_scene_canvas_summary("小结1")
            self.add_scene_canvas_summary("小结2")

            # 连接线路
            self.edit_scene_canvas_line("canvas.canlin.out", "canvas.judge.in")
            self.edit_scene_canvas_line("canvas.judge.outY", "canvas.summary.in1")
            self.edit_scene_canvas_line("canvas.judge.outN", "canvas.summary.in2")

            # 格式化画布
            self.scene_canvas_format()

            # 逻辑校验
            # self.scene_logicValidate()

            # 创建完成
            self.scene_finish()
            time.sleep(1)


        except:
            print("元素读取出现异常：", sys.exc_info()[0])
            raise

    def edit_scene(self):
        '''
        编辑场景
        :return:
        '''
        self.browser.button('xpath', self.fun_flag, "edit_scene.edit")
        self.browser.button('xpath', self.fun_flag, "edit_scene.canvas")

        # 修改信号子任务
        self.edit_scene_canvas_canlin("ABSA", "ABSF")
        time.sleep(5)

        # 格式化画布
        self.scene_canvas_format()

        # 逻辑校验
        self.scene_logicValidate()

        # 创建完成
        self.scene_finish()

    def scene_logicValidate(self):
        '''
        点击逻辑校验
        :return:
        '''
        self.browser.button('xpath', self.fun_flag, "canvas.tools.logicValidate")
        time.sleep(2)

    def scene_finish(self):
        '''
        点击创建完成
        :return:
        '''
        self.browser.button('xpath', self.fun_flag, "canvas.tools.createFinish")
        self.browser.input('xpath', self.fun_flag, "canvas.tools.finishText", "验证通过")
        self.browser.button('xpath', self.fun_flag, "canvas.tools.finishButton")
        time.sleep(2)

    def scene_canvas_format(self):
        '''
        格式化场景
        :return:
        '''
        self.browser.button('xpath', self.fun_flag, "canvas.tools.format")

    def edit_scene_canvas_canlin(self, old_signal, new_signal):
        '''
        编辑场景的逻辑画布-修改信号子任务
        :param old_signal: 原信号名称
        :param new_signal: 新信号名称
        :return:
        '''
        # 双击打开已存在的信号子任务
        self.browser.double_click('xpath', self.fun_flag, "canvas.canlin.exist_canlin_node", old_signal)
        time.sleep(1)

        # 信号任务名称更新
        self.browser.clear('xpath', self.fun_flag, "canvas.canlin.title")
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.title", new_signal)

        # 信号选择
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.signal_input", new_signal)
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.signal", new_signal)

        # 锚点更新
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.summary")
        self.browser.clear('xpath', self.fun_flag, "canvas.canlin.summary")
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.summary", '@')
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.summary_signal", new_signal)
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.summary_signal_sel", new_signal)

        # 点击确认
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.but")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.but")

    def add_scene_canvas_canlin(self, signal):
        '''
        编辑场景的逻辑画布-添加信号子任务
        :param signal: 需要添加的信号名
        :return:
        '''
        # 拖动信号子任务到画布
        self.browser.drag_to_coord('xpath', self.fun_flag, "canvas.canlin.new_canlin_node", 0, 100)
        self.browser.double_click('xpath', self.fun_flag, "canvas.canlin.canlin_node")

        # 信号选择
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.signal_input", signal)
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.signal", signal)

        # 计算配置
        # 勾选条件计算
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

        # 锚点配置
        # 开启锚点
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.ancher")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher")
        # 设置源
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.ancher_resource_type")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_resource_type")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_resource_type_sel")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_resource_value")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_resource_value_sel")
        # 设置判断类型
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_dss")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_dss_eq")
        # 设置值
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_value_type")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.ancher_value_type_sel")
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.ancher_value_value", 1)
        # 设置锚点小结
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.summary", '@')
        self.browser.input('xpath', self.fun_flag, "canvas.canlin.summary_signal", signal)
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.summary_signal_sel", signal)

        # 点击确认
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.canlin.but")
        self.browser.button('xpath', self.fun_flag, "canvas.canlin.but")

        # 格式化画布
        self.scene_canvas_format()

    def add_scene_canvas_decision(self):
        '''
        编辑场景的逻辑画布-添加判断子任务
        :return:
        '''
        # 拖动判断子任务到画布
        self.browser.drag_to_coord('xpath', self.fun_flag, "canvas.judge.new_judge_node", 0, 100)
        self.browser.double_click('xpath', self.fun_flag, "canvas.judge.judge_node")
        # 设置判断类型为是非判断
        self.browser.button('xpath', self.fun_flag, "canvas.judge.resultType")
        self.browser.button('xpath', self.fun_flag, "canvas.judge.resultType_y_n")
        # 点击确认
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.judge.but")
        self.browser.button('xpath', self.fun_flag, "canvas.judge.but")

        # 格式化画布
        self.scene_canvas_format()

    def add_scene_canvas_summary(self, name):
        '''
        编辑场景的逻辑画布-添加小结子任务
        :param name: 小结名称
        :return:
        '''
        # 拖动小结子任务到画布
        self.browser.drag_to_coord('xpath', self.fun_flag, "canvas.summary.new_summary_node", 0, 100)
        self.browser.double_click('xpath', self.fun_flag, "canvas.summary.summary_node")
        # 设置小结任务名称
        self.browser.input('xpath', self.fun_flag, "canvas.summary.name", name)
        # 设置小结属性
        self.browser.button('xpath', self.fun_flag, "canvas.summary.attribute")
        self.browser.button('xpath', self.fun_flag, "canvas.summary.attribute_client")
        # 设置优先级
        self.browser.button('xpath', self.fun_flag, "canvas.summary.priority")
        self.browser.button('xpath', self.fun_flag, "canvas.summary.prion_first")
        # 设置根本原因
        self.browser.input('xpath', self.fun_flag, "canvas.summary.reason", name)
        # 设置处理方案
        self.browser.input('xpath', self.fun_flag, "canvas.summary.content", name)
        # 点击确定
        self.browser.scroll('ele', 'xpath', self.fun_flag, "canvas.summary.but")
        self.browser.button('xpath', self.fun_flag, "canvas.summary.but")

        # 格式化画布
        self.scene_canvas_format()

    def edit_scene_canvas_line(self, port_in, port_out):
        self.browser.drag_to_ele('xpath', self.fun_flag, port_in, port_out)
        time.sleep(1)

# # 调试使用
# if __name__=="__main__":
#     name = "//li[span[text()='${var_to_change}']]"
#     name = name.replace("${var_to_change}","EP33-M0-L7")
#     print(name)

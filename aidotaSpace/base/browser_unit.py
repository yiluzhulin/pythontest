import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.yaml_unit import MyYaml

'''
浏览器的基本操作
'''


class MyBrowser:

    def __init__(self):
        self.driver = webdriver.Chrome()
        # 隐式等待10s
        self.driver.implicitly_wait(10)

        self.data = MyYaml()

    def get(self, url):
        '''
        打开平台,并将窗口最大化
        :param url:
        :return:
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(1)

    def switch_to_window(self, n):
        '''
        切换到指定窗口的句柄
        :param n: 目标窗口句柄
        :return:
        '''
        handles = self.driver.window_handles
        new_window = handles[n]
        self.driver.switch_to.window(new_window)

    def set_style_zoom(self, n):
        '''
        调整窗口缩放比例
        :param n: 预期缩放比例
        :return:
        '''
        self.driver.execute_script("document.body.style.zoom=" + n)

    def get_mothod(self, mothod):
        '''
        提取原定定位的方式
        :param mothod: 元素定位方式标识
        :return:
        '''
        match mothod:
            case 'xpath':
                return By.XPATH
            case 'id':
                return By.ID
            case 'name':
                return By.NAME

    def input(self, mothod, file, sel_path, value):
        '''
        输入框赋值
        :param mothod:元素定位方式
        :param file:元素路径所在文件标识
        :param sel_path:元素路径在文件中存储的位置
        :param value:元素输入的目标值
        :return:
        '''
        time.sleep(1)
        mothod = self.get_mothod(mothod)

        sel = self.data.get_element(file, sel_path)
        input_box = self.driver.find_element(mothod, sel)
        input_box.send_keys(value)
        time.sleep(1)

    def button(self, mothod, file, sel_path, to_change=''):
        '''
        按钮点击
        :param mothod: 元素定位方式
        :param file: 元素路径所在文件标识
        :param sel_path: 元素路径在文件中存储的位置
        :param to_change: 元素路径中需要替换的变量目标值
        :return:
        '''
        mothod = self.get_mothod(mothod)
        sel = self.data.get_element(file, sel_path)

        # 元素替换
        if to_change != '':
            sel = sel.replace("${var_to_change}", to_change)

        input_box = self.driver.find_element(mothod, sel)
        input_box.click()
        time.sleep(1)

    def drag(self, mothod, file, sel_path, right, down):
        '''
        拖动子任务节点
        :param mothod: 元素定位方式
        :param file: 元素路径所在文件标识
        :param sel_path: 元素路径在文件中存储的位置
        :param right: 向右移动的位置
        :param down: 向下移动的位置
        :return:
        '''
        mothod = self.get_mothod(mothod)
        sel = self.data.get_element(file, sel_path)
        element_to_be_dragged = self.driver.find_element(mothod, sel)

        # 创建拖动模块
        action = ActionChains(self.driver)
        # 鼠标按下不松开，并执行动作
        action.click_and_hold(element_to_be_dragged).perform()
        # 将元素拖动到指定为止，向右+向下移动
        action.move_by_offset(right, down)
        # 释放鼠标， 完成拖动
        action.release().perform()

    def double_click(self, mothod, file, sel_path):
        '''
        元素执行双击操作
        :param mothod: 元素定位方式
        :param file: 元素路径所在文件标识
        :param sel_path: 元素路径在文件中存储的位置
        :return:
        '''
        mothod = self.get_mothod(mothod)
        sel = self.data.get_element(file, sel_path)
        element = self.driver.find_element(mothod, sel)

        # 执行双击操作
        action = ActionChains(self.driver)
        action.double_click(element).perform()

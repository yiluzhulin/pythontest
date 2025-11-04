import time
from cgitb import handler

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import new_window_is_opened

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

    def button(self, mothod, file, sel_path, ):
        '''
        按钮点击
        :param mothod: 元素定位方式
        :param file: 元素路径所在文件标识
        :param sel_path: 元素路径在文件中存储的位置
        :return:
        '''
        mothod = self.get_mothod(mothod)
        sel = self.data.get_element(file, sel_path)
        input_box = self.driver.find_element(mothod, sel)
        input_box.click()

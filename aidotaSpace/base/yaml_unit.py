import os.path
import yaml

'''
yaml文件的基本操作
'''


class MyYaml:
    def get_element(self, fun, path):
        '''
        基于不同功能，提取不同文件中的数据
        :param fun: 功能类型
        :param path: 参数在文件中的位置
        :return:
        '''
        file_path = "./common"
        # 基于功能模块，从不同文件中读取
        match fun:
            case "var":
                file_path = os.path.join(file_path, "vars.yaml")
            case "login":
                file_path = os.path.join(file_path, "login.yaml")
            case "scene":
                file_path = os.path.join(file_path, "sceneCanvas.yaml")

        # 读取文件内容
        with open(file_path, 'r', encoding="utf-8") as file:
            data = yaml.safe_load(file)
            eles = path.split('.')
            for ele in eles:
                data = data[ele]
            return data

# # 代码调试
# if __name__=="__main__":
#     str = "aaa.bbb"
#     ss = str.split('.')
#     print(ss)

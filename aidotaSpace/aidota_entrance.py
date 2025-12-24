from base.browser_unit import MyBrowser
from scripts.aiTasks import AiTasks
from scripts.login import Login
from scripts.sceneCanvas import SceneCanvas

if __name__ == "__main__":
    browser = MyBrowser()

    # 测试环境
    env = "sit"

    # 登录IAM平台
    login = Login(browser, env)
    login.login()

    # # 场景组&场景管理界面操作
    # sceneScanvas = SceneCanvas(browser, env)
    # sceneScanvas.entrance()

    # Ai诊断任务界面操作
    aiTasks = AiTasks(browser, env)
    aiTasks.entrance()

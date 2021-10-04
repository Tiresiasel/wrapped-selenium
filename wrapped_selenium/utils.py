import os
from os import path
import sys
from selenium import webdriver

current_path = path.dirname(__file__)


class WrappedSelenium:
    def __init__(self, headless=True, proxy=None, store_path=None):
        """
        init load driver data
        """
        # chrome_options 初始化选项
        self.chrome_options = webdriver.ChromeOptions()
        self.prepare_download_path(store_path)
        # 设置浏览器初始 位置x,y & 宽高x,y
        # self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument(f'--window-position={0},{0}')
        self.chrome_options.add_argument(f'--window-size={1920},{1080}')
        # 关闭自动测试状态显示 // 会导致浏览器报：请停用开发者模式
        # window.navigator.webdriver还是返回True,当返回undefined时应该才可行。
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 关闭开发者模式
        self.chrome_options.add_experimental_option("useAutomationExtension", False)
        # # 禁止图片加载, 下载路径
        # preferences = {
        #     # "profile.managed_default_content_settings.images": 2,
        #     # "download.default_directory":store_path,
        #     "profile.default_content_settings.popups": 0
        # }

        # if store_path is not None:
        #     preferences['download.default_directory'] = store_path

        # self.chrome_options.add_experimental_option("preferences", preferences)
        # 设置中文
        self.chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 更换头部
        self.chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
        # 隐藏浏览器
        if headless:
            self.chrome_options.add_argument('--headless')  # 隐藏浏览器

        if proxy is not None:
            self.chrome_options.add_argument('--proxy-server=%s' % proxy)

        # 部署项目在linux时，其驱动会要求这个参数
        # 创建浏览器对象
        script = '''
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        '''
        # Chromedriver指定路径
        if sys.platform == 'darwin':
            self.driver = webdriver.Chrome(executable_path=f"{current_path}/driver/chromedriver-darwin",
                                           options=self.chrome_options)
        elif sys.platform == "linux":
            # 部署项目在linux时，其驱动会要求这个参数
            self.chrome_options.add_argument('--disable-dev-shm-usage')
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-gpu')

            self.driver = webdriver.Chrome(executable_path=f"{current_path}/driver/chromedriver-linux",
                                           options=self.chrome_options)
        elif sys.platform == "win32":
            self.driver = webdriver.Chrome(executable_path=f"{current_path}\\driver\\chromedriver-win.exe",
                                           options=self.chrome_options)
        else:
            raise ValueError("Platform not support currently!")
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": script})

    @staticmethod
    def prepare_download_path(store_path):
        if store_path is not None:
            if not os.path.exists(store_path):
                os.makedirs(store_path)

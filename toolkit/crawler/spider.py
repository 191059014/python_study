import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
PROXYS = [
    {'http': '220.173.37.128:7890'},
    {'http': '120.26.160.120:7890'},
    {'http': '14.20.235.129:34100'},
]


def do_static_webpage_spider(url, encoding='utf-8'):
    """
    静态网页爬取
    :param url: 网页地址
    :param encoding: 编码
    :return: 网页源代码
    """
    last_exception = None
    # 重试三次
    for i in range(3):
        # 每次请求间隔2秒钟，防止被封
        time.sleep(2)
        for proxy in PROXYS:
            try:
                resp = requests.get(url, headers={'User-Agent': USER_AGENT}, proxies=proxy)
                status_code = resp.status_code
                if status_code != 200:
                    raise RuntimeError("code: " + str(status_code) + ', message: ' + resp.reason)
                return resp.content.decode(encoding)
            except Exception as e:
                last_exception = e
    if last_exception is not None:
        raise RuntimeError("静态网页[%s]爬取失败: %s" % (url, str(last_exception)))


def do_dynamic_webpage_spider(url, wait_js_load_sec=3):
    """
    动态网页爬取
    :param url: 网页地址
    :param wait_js_load_sec: 等待js加载的时间
    :return: 网页源代码
    """
    last_exception = None
    # 重试三次
    for i in range(3):
        try:
            # 设置Chrome不弹出界面，实现无界面爬取
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            # 指定chromedriver的路径（如果加入到环境变量中了，这里可以不设置）
            chrome_service = Service(executable_path="C:\WindowsD\work_soft\chromedriver_win32\chromedriver.exe")
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
            driver.get(url)
            time.sleep(wait_js_load_sec)
            return driver.page_source
        except Exception as e:
            last_exception = e
    if last_exception is not None:
        raise RuntimeError(last_exception)

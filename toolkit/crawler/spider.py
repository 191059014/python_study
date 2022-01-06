import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
PROXYS = [
    {'http': '220.173.37.128:7890'},
    {'http': '118.180.166.195:8060'},
    {'http': '120.26.160.120:7890'},
    {'http': '139.9.2.31:8081'},
    {'http': '14.20.235.129:34100'},
    {'http': '58.20.235.180:9091'},
    {'http': '118.180.166.195:8060'},
    {'http': '47.92.234.75:80'},
    {'http': '47.56.69.11:8000'},
    {'http': '183.247.211.151:30001'},
    {'http': '180.97.87.63:80'},
    {'http': '111.3.118.247:30001'},
    {'http': '221.125.138.189:8380'},
    {'http': '47.106.105.236:80'},
    {'http': '218.75.102.198:8000'},
    {'http': '152.136.62.181:9999'},
    {'http': '47.243.190.108:7890'},
    {'http': '115.235.18.113:9000'},
    {'http': '183.23.72.86:3128'},
    {'http': '117.114.149.66:55443'}
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
    for i in range(4):
        if (i > 0):
            print("retry %s times, waiting..." % i)
        # 每次请求间隔2秒钟，防止被封
        time.sleep(2)
        for i in range(10):
            # 随机获取代理
            index = random.randint(0, len(PROXYS))
            proxy = PROXYS[index]
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
        if (i > 0):
            print("retry %s times, waiting..." % i)
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

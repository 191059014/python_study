import time
from urllib import request
from urllib.request import Request

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class DynamicCrawler():
    """
    动态页面爬取，通过js渲染的网页
    """

    def __init__(self, url: str, loading_time_sec: int = 3) -> None:
        self.url = url
        self.loading_time_sec = loading_time_sec

    def do_crawling(self) -> str:
        """
        动态网页的爬取
        :return: 网页html
        """
        # 设置Chrome不弹出界面，实现无界面爬取
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 指定chromedriver的路径（如果加入到环境变量中了，这里可以不设置）
        chrome_service = Service(executable_path="C:\WindowsD\work_soft\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get(self.url)
        # 等待网页加载完成
        print("Waiting for %s seconds..." % self.loading_time_sec)
        time.sleep(self.loading_time_sec)
        print("Crawling finished, url=%s" % self.url)
        return driver.page_source


class StaticCrawler():
    """
    静态页面爬取
    """

    def __init__(self, url: str, encoding: str = 'utf-8') -> None:
        self.url = url
        self.encoding = encoding

    def do_crawling(self) -> str:
        """
        简单的爬取网页
        :return: 网页html
        """
        resp = request.urlopen(self.url)
        bytes = resp.read()
        html = bytes.decode(self.encoding)
        print("Crawling finished, url=%s" % self.url)
        return html

    def do_crawling_security(self) -> str:
        """
        安全爬取网页，设置用户代理
        :return: 网页html
        """
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        proxys = [
            {'http': '220.173.37.128:7890'},
            {'http': '120.26.160.120:7890'},
            {'http': '14.20.235.129:34100'},
        ]
        req = Request(self.url)
        req.add_header('User-Agent', user_agent)
        res = None
        for proxy in proxys:
            try:
                proxy_handler = request.ProxyHandler(proxy)
                opener = request.build_opener(proxy_handler)
                resp = opener.open(req)
                if resp:
                    bytes = resp.read()
                    res = bytes.decode(self.encoding)
                    print("Crawling finished, Proxy=%s, url=%s" % (proxy, self.url))
                    break
            except Exception as e:
                print("Crawling failed, Proxy=%s, url=%s, error=%s" % (proxy, self.url, e))
        return res


if __name__ == '__main__':
    # print(DynamicCrawler('https://www.toutiao.com/').do_crawling())
    print(StaticCrawler('https://www.toutiao.com/').do_crawling())

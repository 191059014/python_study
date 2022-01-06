"""
下载小说
"""
import re
import threading

from lxml import etree

import spider


def get_chapter_urls(url, chapter_xpath, encoding='utf-8'):
    """
    获取所有章节的uri
    :param url: 首页地址
    :param chapter_xpath: 章节超链接的xpath路径
    :param encoding: 编码
    :return: 超链接地址
    """
    page_source = spider.do_static_webpage_spider(url, encoding)
    document = etree.HTML(page_source)
    return document.xpath(chapter_xpath)


def parse_detail_page(detail_page_url, title_xpath, content_xpath, encoding):
    """
    解析某一章节
    :param detail_page_url: 章节页面地址
    :param title_xpath: 章节标题xpath路径
    :param content_xpath: 章节内容xpath路径
    :param encoding: 编码
    :return: 标题+内容
    """
    page_source = spider.do_static_webpage_spider(detail_page_url, encoding)
    document = etree.HTML(page_source)
    # 章节标题
    title = document.xpath(title_xpath)[0]
    # 章节内容
    contents = document.xpath(content_xpath)
    return title, contents


def save_to_file(save_file_path, all_chapter_contents: list, encoding):
    """
    保存到文件
    :param save_file_path: 文件路径
    :param all_chapter_contents: 所有章节内容
    """
    for chapter_content in all_chapter_contents:
        # 追加写入
        with open(save_file_path, mode='a', encoding=encoding) as f:
            f.write(chapter_content)


def do_spider(url, chapter_xpath, title_xpath, content_xpath, save_file_path, start: int, end: int, encoding='utf-8'):
    # 获取所有章节的uri
    chapter_urls = get_chapter_urls(url, chapter_xpath)
    # 获取域名
    host = re.search(r'((http|https)://.*?)/', url).group(0)
    # 获取章节完整地址
    chapter_full_urls = list(map(lambda uri: host + uri, chapter_urls[start:end]))
    # 处理所有章节
    all_chapter_contents = []
    for i in range(len(chapter_full_urls)):
        title, chapter_contents = parse_detail_page(chapter_full_urls[i], title_xpath, content_xpath, encoding)
        all_chapter_contents.append(title + "\r\n".join(chapter_contents))
        print("爬取完成 ---> %s" % title)
    # 保存到文件
    save_to_file(save_file_path % (str(start + 1) + "_" + str(end)), all_chapter_contents, encoding)
    print("====================第%s章-第%s章，爬取完成====================" % (start + 1, end))


if __name__ == '__main__':
    home_url = "https://www.mcmssc.com/0_69/"
    chapter_xpath = "//dt[contains(text(),'《最强狂兵》正文')]/following-sibling::dd/a/@href"
    title_xpath = "//div[@class='bookname']//h1[1]/text()"
    content_xpath = "//div[@id='content']/text()"
    save_file_path = "C:\\Users\\huangbiao\\Desktop\\最强狂兵_%s.txt"
    # 爬取章节范围
    chapter_num_scopes = [
        (3000, 4000),
        (4000, 5000)
    ]
    for start, end in chapter_num_scopes:
        args = (home_url, chapter_xpath, title_xpath, content_xpath, save_file_path, start, end, "utf-8")
        t = threading.Thread(target=do_spider, args=args)
        t.start()

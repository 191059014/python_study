import requests
from lxml import etree

img_save_path = 'C:\\Users\\huangbiao\\Desktop\\download_mm\\'
website_host = 'http://www.jj20.com'
home_html = requests.get('http://www.jj20.com/bz/nxxz').content.decode(encoding='gb2312')
document = etree.HTML(home_html)
a_elements = document.xpath('//ul[@class="picbz"]//a[1]')
for index, a_element in enumerate(a_elements, start=1):
    category_desc = a_element.xpath("img")[0].get('alt')
    href = a_element.get('href')
    detail_page_html = requests.get(website_host + href).content.decode(encoding='gb2312', errors='ignore')
    detail_document = etree.HTML(detail_page_html)
    img_elements = detail_document.xpath('//ul[@id="showImg"]//img')
    for image_index, img_element in enumerate(img_elements, start=1):
        img_src = img_element.get('src')
        img_bytes = requests.get("http:" + img_src).content
        with open(img_save_path + category_desc + str(image_index) + '.jpg', 'wb') as imgfile:
            imgfile.write(img_bytes)
    print('%s，共%s张，全部下载完毕' % (category_desc, len(img_elements)))

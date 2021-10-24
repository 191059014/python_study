import os.path
import re
import urllib.request as httputil

website_url = 'http://www.jj20.com/bz/nxxz/list_7_2.html'
website_encode = 'gb2312'
image_save_folder_path = 'C:\\Users\\huangbiao\\Desktop\\download_mm'

"""
打开url，返回html
"""


def _open_url(url):
    resp = httputil.urlopen(url)
    byte_data = resp.read()
    return byte_data


"""
从html中查找出图片地址
"""


def _find_image_address(byte_data):
    html = byte_data.decode(website_encode)
    # 查找img.*src="开头，以.jpg结尾的字符串列表
    image_address = re.findall("img.*src=\"(.*?).jpg", html)
    image_address = ['http:' + imageUrl + '.jpg' for imageUrl in image_address]
    return image_address


"""
如果文件夹不存在，则创建
如果文件夹已存在，则清空文件下的所有文件
"""


def _create_if_not_exist_folder(image_save_path):
    if not os.path.exists(image_save_path):
        os.mkdir(image_save_path)
    else:
        for image_path in os.listdir(image_save_path):
            image_full_path = os.path.join(image_save_path, image_path)
            if os.path.isfile(image_full_path):
                os.remove(image_full_path)
                print("删除图片: %s" % image_full_path)


"""
保存图片
"""


def _save_image(image_address):
    for image_url in image_address:
        # 从url中获取图片名称
        file_name = image_url.split('/')[-1]
        file_full_path = os.path.join(image_save_folder_path, file_name)
        with open(file_full_path, 'wb') as f:
            image = _open_url(image_url)
            f.write(image)
            print("保存图片: %s" % file_full_path)


"""
下载
"""


def download():
    # 打开网站网页
    byte_data = _open_url(website_url)
    # 根据html查找满足条件的图片地址
    image_address = _find_image_address(byte_data)
    # 创建文件夹
    _create_if_not_exist_folder(image_save_folder_path)
    # 保存图片
    _save_image(image_address)


if __name__ == '__main__':
    print('准备下载图片...')
    download()
    print('下载完毕^_^')

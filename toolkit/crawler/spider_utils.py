import json
from urllib import request
from urllib.request import Request

_DEFAULT_ENCODING = 'utf-8'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
proxys = [
    {'http': '220.173.37.128:7890'},
    {'http': '120.26.160.120:7890'},
    {'http': '14.20.235.129:34100'},
]


def get_bytes_security_from_remote(url) -> bytes:
    """
    从远程获取字节数据
    :return: 数据
    """
    req = Request(url)
    req.add_header('User-Agent', user_agent)
    for proxy in proxys:
        try:
            proxy_handler = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_handler)
            resp = opener.open(req)
            if resp:
                print("Invoke Remote Success, Proxy=%s" % proxy)
                return resp.read()
        except Exception as e:
            print("Invalid Proxy=%s" % proxy)
    raise Exception('Invoke Remote Failed')


def get_bytes_from_remote(url) -> bytes:
    """
    从远程获取字节数据
    :return: 数据
    """
    resp = request.urlopen(url)
    return resp.read()


def get_str_from_remote(url, encoding=_DEFAULT_ENCODING) -> str:
    """
    从远程获取字符串数据
    :return: 数据
    """
    return get_bytes_from_remote(url).decode(encoding)


def get_obj_from_remote(url, encoding=_DEFAULT_ENCODING):
    """
    从远程获取对象数据
    :return: 数据
    """
    return json.loads(get_str_from_remote(url, encoding))


def save_to_file(remote_url, file_path) -> None:
    """
    将远程内容保存到文件
    """
    byte_data = get_bytes_from_remote(remote_url)
    with open(file_path, 'wb') as f:
        f.write(byte_data)

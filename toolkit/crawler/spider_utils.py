import json
from urllib import request

_DEFAULT_ENCODING = 'utf-8'


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

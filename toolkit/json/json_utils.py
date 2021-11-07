import json
from datetime import datetime, date
from typing import Any


class CustomJsonEncoder(json.JSONEncoder):
    """
    自定义json编码
    """

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, o)


def write_file(obj, filename: str):
    """
    将json格式的对象写入json文件
    :param obj: 对象
    :param filename: 带路径的完整文件名
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)


def read_file(filename: str):
    """
    读取json文件并转换为对象
    :param filename: 带路径的完整文件名
    :return: json格式的对象
    """
    with open(filename, "rb") as f:
        return json.load(f)

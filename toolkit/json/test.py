import json
from datetime import datetime

from json_utils import write_file, read_file
from toolkit.json.json_utils import CustomJsonEncoder


class UserModel():

    def __init__(self, username, age, birthday: datetime) -> None:
        self.username = username
        self.age = age
        self.birthday = birthday


if __name__ == '__main__':
    json_model = UserModel('zhangsan', 19, datetime.now())
    print(json.dumps(json_model.__dict__, cls=CustomJsonEncoder))

    province_city_list = []
    province_city_list.append({"code": "001", "name": "湖北省", "citys": [{"code": "001001", "name": "武汉市"}]})
    province_city_list.append({"code": "002", "name": "深圳市", "citys": [{"code": "002001", "name": "深圳市"}]})
    write_file(province_city_list, '../../test/city.json')

    city_json_obj = read_file('../../test/city.json')
    print(city_json_obj)

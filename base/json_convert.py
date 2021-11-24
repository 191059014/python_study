import json
import random

# dumps 将对象序列化成json字符串
dict_1 = {}.fromkeys(range(5), random.randint(0, 9))
dict_1_json = json.dumps(dict_1)
print("%-50s   ===>   字典转换成json：%s" % (dict_1, dict_1_json))

# loads 将json字符串反序列化成对象
json_to_dict = json.loads(dict_1_json)
print("%-50s   ===>   json转换成字典：%s" % (dict_1, dict_1_json))

# dump  将对象序列化成json字符串，并写入文件中
province_city_list = []
province_city_list.append({"code": "001", "name": "湖北省", "citys": [{"code": "001001", "name": "武汉市"}]})
province_city_list.append({"code": "002", "name": "深圳市", "citys": [{"code": "002001", "name": "深圳市"}]})
with open("../temp/province_city.json", "w", encoding="utf-8") as json_file:
    json.dump(province_city_list, json_file, ensure_ascii=False, indent=4)
    print("将json格式对象写入文件完成")

# load  从json文件中读取数据，并反序列成对象
with open("../temp/province_city.json", "rb") as json_file:
    json_obj = json.load(json_file)
    print(json_obj)

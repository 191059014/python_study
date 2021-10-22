"""
这里放一些基础功能、常用函数
"""
print("所有内置函数：")
print(dir("_builtins_"))

print("查看帮助文档：")
print(help(list))

print("判断类型：")
print(type(1))
print(type(1.2))
print(type("zhangsan"))

print("判断是否是具体类型：")
print(isinstance("zhangsan", str))

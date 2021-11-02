"""
算数运算符
"""
print(1 + 2)  # 加法
print(3 - 1)  # 减法
print(2 * 3)  # 乘法
print(10 / 4)  # 除法，结果为2.5
print(10 % 4)  # 取模，结果为2
print(2 ** 3)  # 幂，结果为8
print(10 // 4)  # 取整除 - 向下取接近商的整数，结果为2
"""
逻辑运算符
"""
print(10 and 20)  # 布尔"与"，如果x为False，x and y 返回x的值，否则返回y的计算值，结果为20
print(10 or 20)  # 布尔"或"，如果x是True，它返回x的值，否则它返回y的计算值，结果为10
print(not 0)  # 0为假，非0，所以结果为True
print(not 1)  # 非0为真，所以结果为True
"""
成员运算符
"""
tuple_var = 1, 2, 3
print(1 in tuple_var)  # 结果为True
print(4 in tuple_var)  # 结果为False
print(1 not in tuple_var)  # 结果为False
print(4 not in tuple_var)  # 结果为True
"""
成员运算符（判断两个标识符是不是引用自一个对象）
"""
a = 10
b = 10
c = 15
print(a is b)  # 结果为True
print(a is c)  # 结果为False
print(a is not b)  # 结果为False
print(a is not c)  # 结果为True

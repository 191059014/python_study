'''
描述
计算一个浮点数的立方根，不使用库函数。
保留一位小数。
输入描述：
待求解参数，为double类型（一个实数）
输出描述：
输出参数的立方根。保留一位小数。
示例1
输入：
19.9
输出：
2.7
'''
f = float(input())
flag = True
if f < 0:
    flag = False
    f = abs(f)
res = 0.0
if 1 > f > 0:
    while True:
        res += 0.0001
        if round(res ** 3, 1) - f > 0.0001:
            break
else:
    while res < f:
        res += 0.0001
        if round(res ** 3, 1) == f:
            break
values = round(res, 1)
if not flag:
    values = 0 - values
print(values)

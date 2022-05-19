"""
描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
数据范围：保证输入的数字在 32 位浮点数范围内
输入描述：
输入一个正浮点数值
输出描述：
输出该数值的近似整数值

示例1
输入：
5.5
输出：
6
说明：
0.5>=0.5，所以5.5需要向上取整为6
"""

user_input = float(input())
zhengshu = user_input // 1
xiaoshu = user_input % 1
if xiaoshu >= 0.5:
    zhengshu += 1
print(int(zhengshu))

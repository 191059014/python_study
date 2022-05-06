"""
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
输入描述：
输入一个整数
输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
示例1
输入：
180
输出：
2 2 3 3 5
"""
import math

num = int(input())
try:
    for i in range(2, int(math.sqrt(num)) + 1): #只需要计算到平方根的位置即可
        while num % i == 0:
            print(i, end=' ')
            num = num // i
    if num > 2:
        print(num)
except Exception as e:
    pass

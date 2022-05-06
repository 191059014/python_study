"""
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
输入描述：
输入一个十六进制的数值字符串。
输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
示例1
输入：
0xAA
输出：
170
"""
try:
    user_input = input()
    print(int(user_input, 16))
except Exception as e:
    pass

"""
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。
输入描述：
输入一个int型整数
输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
示例1
输入：
9876673
输出：
37689
"""
user_input = input()
result = ""
for c in reversed(user_input):
    if c not in result:
        result += c
print(result)

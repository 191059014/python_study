"""
描述
给定 n 个字符串，请对 n 个字符串按照字典序排列。
输入描述：
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述：
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入：
9
cap
to
cat
card
two
too
up
boat
boot
复制
输出：
boat
boot
cap
card
cat
to
too
two
up
"""
total = int(input())
user_input_list = []
for i in range(total):
    user_input_list.append(input())
for item in sorted(user_input_list):
    print(item)

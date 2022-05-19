"""
描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）

输入描述：
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。

输出描述：
输出输入字符串中含有该字符的个数。（不区分大小写字母）

示例1
输入：
ABCabc
A
输出：
2
"""


def is_same_char(s1: str, s2: str):
    """
    判断两个字符是否是相同字符，不区分大小写
    """
    return s1 == s2 or s1.swapcase() == s2


str_input = input()
c_input = input()
times = 0
try:
    for s in str_input:
        if is_same_char(s, c_input):
            times += 1
    print(times)
except Exception as e:
    pass

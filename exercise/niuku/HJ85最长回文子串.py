"""
给定一个仅包含小写字母的字符串，求它的最长回文子串的长度。
所谓回文串，指左右对称的字符串。
所谓子串，指一个字符串删掉其部分前缀和后缀（也可以不删）的字符串
数据范围：字符串长度
进阶：时间复杂度：，空间复杂度：
输入描述：
    输入一个仅包含小写字母的字符串
输出描述：
    返回最长回文子串的长度
示例1
输入：
    cdabbacc
输出：
    4
说明：
abba为最长的回文子串
"""


def find_huiwen(leftIndex, rightIndex, text):
    global max_len
    is_equal = False
    while leftIndex >= 0 and rightIndex < len(text) and text[leftIndex] == text[rightIndex]:
        leftIndex -= 1
        rightIndex += 1
        is_equal = True
    if is_equal and max_len < rightIndex - leftIndex - 1:
        max_len = rightIndex - leftIndex - 1


text = input()
max_len = 0
for i in range(len(text)):
    find_huiwen(i, i + 1, text)
    find_huiwen(i, i + 2, text)
print(max_len)

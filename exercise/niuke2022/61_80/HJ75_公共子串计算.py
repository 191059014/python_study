'''
描述
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。
注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
输入描述：
输入两个只包含小写字母的字符串
输出描述：
输出一个整数，代表最大公共子串的长度
示例1
输入：
asdfas
werasdfaswer
输出：
6
'''
s1, s2 = input(), input()
res = ''
for i in range(len(s1)):
    for j in range(i + 1, len(s1) + 1):
        s3 = s1[i:j]
        if s3 in s2:
            if len(s3) > len(res):
                res = s3
print(len(res))

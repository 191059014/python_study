'''
描述
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
输入描述：
输入两个字符串
输出描述：
返回重复出现的字符
示例1
输入：
abcdefghijklmnop
abcsafjklmnopqrstuvw
输出：
jklmnop
'''
s1, s2 = input(), input()
max_sub = ''
min_s = s1
if len(s1) > len(s2):
    min_s = s2
for i in range(len(min_s)):
    for j in range(i, len(min_s)):
        sub = min_s[i:j + 1]
        if sub in s1 and sub in s2 and len(sub) > len(max_sub):
            max_sub = sub
print(max_sub)

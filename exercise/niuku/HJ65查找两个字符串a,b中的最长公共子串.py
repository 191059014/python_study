"""
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
本题含有多组输入数据！
数据范围：字符串长度，
进阶：时间复杂度：O(n的3次方)，空间复杂度：O(n)
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
"""
while True:
    try:
        text1 = input()
        text2 = input()
        min_len_str = text1
        if len(text1) > len(text2):
            min_len_str = text2
        max_len_sub = ''
        for start in range(len(text1)):
            for end in range(start + 1, len(text1) + 1):
                substr = text1[start:end]
                if substr not in text2:
                    continue
                if len(substr) > len(max_len_sub):
                    max_len_sub = substr
                elif len(substr) == len(max_len_sub):
                    index1 = min_len_str.index(substr)
                    index2 = min_len_str.index(max_len_sub)
                    if index1 < index2:
                        max_len_sub = substr
                else:
                    pass
        print(max_len_sub)
    except:
        break

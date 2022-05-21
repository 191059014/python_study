"""
描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
输入描述：
输入一行字符串，可以有空格
输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数
示例1
输入：
1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\][
输出：
26
3
10
12
"""
s = input()
char_count = 0
blank_count = 0
num_count = 0
other_count = 0
for c in s:
    if c.isalpha():
        char_count += 1
    elif c.isspace():
        blank_count += 1
    elif c.isnumeric():
        num_count += 1
    else:
        other_count += 1
print(char_count)
print(blank_count)
print(num_count)
print(other_count)

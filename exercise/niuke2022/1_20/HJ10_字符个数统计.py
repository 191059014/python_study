"""
描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。
多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。
输入描述：
输入一行没有空格的字符串。
输出描述：
输出 输入字符串 中范围在(0~127，包括0和127)字符的种数。
示例1
输入：
abc
输出：
3
"""
user_input = input()
no_repeat_str = ""
for str in user_input:
    if str not in no_repeat_str:
        no_repeat_str += str
print(len(no_repeat_str))

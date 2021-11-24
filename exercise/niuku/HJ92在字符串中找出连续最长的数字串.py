"""
输入一个字符串，返回其最长的数字子串，以及其长度。若有多个最长的数字子串，则将它们全部输出（按原字符串的相对位置）
本题含有多组样例输入。
数据范围：字符串长度  ， 保证每组输入都至少含有一个数字
输入描述：
    输入一个字符串。1<=len(字符串)<=200
输出描述：
    输出字符串中最长的数字字符串和它的长度，中间用逗号间隔。如果有相同长度的串，则要一块儿输出（中间不要输出空格）。
示例1
    输入：
        abcd12345ed125ss123058789
        a8a72a6a5yy98y65ee1r2
    输出：
        123058789,9
        729865,2
    说明：
    样例一最长的数字子串为123058789，长度为9
    样例二最长的数字子串有72,98,65，长度都为2
"""


def get_current_max_len(max_len_numeric_str):
    if max_len_numeric_str.find(",") > -1:
        arr = max_len_numeric_str.split(",")
        return len(arr[0])
    else:
        return len(max_len_numeric_str)


while True:
    try:
        text = input()
        max_len_numeric_str = ''
        for i in range(len(text)):
            end = i
            is_numeric = False
            while end < len(text) and text[end].isnumeric():
                end += 1
                is_numeric = True
            if is_numeric:
                max_len = get_current_max_len(max_len_numeric_str)
                if max_len < end - i:
                    max_len_numeric_str = text[i:end]
                elif max_len == end - i:
                    max_len_numeric_str += "," + text[i:end]
                else:
                    pass
        print("".join(max_len_numeric_str.split(",")) + "," + str(get_current_max_len(max_len_numeric_str)))
    except:
        break

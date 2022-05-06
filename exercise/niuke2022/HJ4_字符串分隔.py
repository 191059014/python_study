"""
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串

示例1
输入：
abc
输出：
abc00000
"""
user_input = input()
start_index = 0
end_index = 8
try:
    if len(user_input) <= 8:
        print(user_input + ''.zfill(8 - len(user_input)))
    else:
        while (len(user_input) > end_index):
            print(user_input[start_index:end_index])
            start_index = end_index
            end_index += 8
        if len(user_input) > start_index:
            print(user_input[start_index:] + ''.zfill(8 - len(user_input[start_index:])))
except Exception as e:
    pass

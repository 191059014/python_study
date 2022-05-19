"""
描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。
输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
输出描述：
删除字符串中出现次数最少的字符后的字符串。
示例1
输入：
aabcddd
输出：
aaddd
"""
user_input = input()
delete_chars = set(user_input[0])
min_times = user_input.count(user_input[0])
for c in user_input:
    count = user_input.count(c)
    if count == min_times:
        delete_chars.add(c)
    elif count < min_times:
        delete_chars.clear()
        delete_chars.add(c)
        min_times = count
for c in delete_chars:
    user_input = user_input.replace(c, '')
print(user_input)

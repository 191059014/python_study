"""
描述
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
输入描述：
 输入一个整数（int类型）
输出描述：
 这个数转换成2进制后，输出1的个数
示例1
输入：
5
输出：
2
"""
user_input = int(input())
s = bin(user_input)
total = 0
for s1 in s:
    if '1' == s1:
        total += 1
print(str(total))

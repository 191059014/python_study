"""
描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
输入描述：
输入
1 输入IP地址
2 输入10进制型的IP地址
输出描述：
输出
1 输出转换成10进制的IP地址
2 输出转换后的IP地址
示例1
输入：
10.0.3.193
167969729
输出：
167773121
10.3.3.193
"""
print(int(''.join([bin(int(ip_num))[2:].rjust(8, '0') for ip_num in input().split('.')]), 2))
bin_str = bin(int(input()))[2:]
ips = []
for i in range(len(bin_str), 0, -8):
    start_index = i - 8
    if start_index < 0:
        start_index = 0
    bin_s = bin_str[start_index:i].rjust(8, '0')
    ips.append(str(int(bin_s, 2)))
print('.'.join(reversed(ips)))

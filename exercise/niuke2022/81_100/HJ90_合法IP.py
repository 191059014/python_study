'''
描述
IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，
表示成一个无符号整数（因此正号不需要出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
现在需要你用程序来判断IP是否合法。
输入描述：
输入一个ip地址，保证不包含空格
输出描述：
返回判断的结果YES or NO
示例1
输入：
255.255.255.1000
输出：
NO
'''
ip_arr = input().split('.')
res = True
if len(ip_arr) != 4:
    res = False
else:
    for ip in ip_arr:
        if not ip.isnumeric():
            res = False
            break
        if not ip or (len(ip) != 1 and ip.startswith('0')):
            res = False
            break
        i = int(ip)
        if i < 0 or i > 255:
            res = False
            break
print('YES' if res else 'NO')

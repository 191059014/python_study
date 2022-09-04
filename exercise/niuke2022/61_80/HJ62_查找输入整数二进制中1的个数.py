'''
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！
输入描述：
输入一个整数
输出描述：
计算整数二进制中1的个数
示例1
输入：
5
输出：
2
说明：
5的二进制表示是101，有2个1
'''
while True:
    try:
        num = int(input())
        print(str(bin(num)).count("1"))
    except:
        break

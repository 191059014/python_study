"""
给你一串未加密的字符串str，通过对字符串的每一个字母进行改变来实现加密，加密方式是在每一个字母str[i]偏移特定数组元素a[i]的量，
数组a前三位已经赋值：a[0]=1,a[1]=2,a[2]=4。
当i>=3时，数组元素a[i]=a[i-1]+a[i-2]+a[i-3]，
例如：原文 abcde 加密后 bdgkr，其中偏移量分别是1,2,4,7,13。
输入描述:
第一行为一个整数n（1<=n<=1000），表示有n组测试数据，每组数据包含一行，原文str（只含有小写字母，0<长度<=50）。
输出描述:
每组测试数据输出一行，表示字符串的密文
示例1
输入
    1
    xy
输出
    ya
说明
第一个字符x偏移量是1，即为y，第二个字符y偏移量是2，即为a
"""


def get_pianyi(n):
    """
    获取便宜量
    """
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n == 3:
        return 4
    if n >= 3:
        return get_pianyi(n - 1) + get_pianyi(n - 2) + get_pianyi(n - 3)


def get_final_ch(ch, pianyi):
    """
    根据字符和偏移量，获取最终的字符
    """
    ch_table = [chr(i) for i in range(ord('a'), ord('a') + 26)]
    index = ch_table.index(ch)
    final_index = index + pianyi
    if final_index < 26:
        return ch_table[final_index]
    else:
        new_index = final_index % 26
        return ch_table[new_index]


while True:
    data_row = input()
    for i in range(int(data_row)):
        data = input()
        result = ''
        for n in range(len(data)):
            pianyi = get_pianyi(n)
            ch = get_final_ch(data[n], pianyi)
            result += ch
        print(result)

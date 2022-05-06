"""
斐波那契数列（Fibonacci sequence），又称为黄金分割数列，指的是这样的一个数列：
0,1,1,2,3,5,8,13,21,34
"""


def get_fibonacci(n):
    """
    获取第n个数的值
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)


if __name__ == '__main__':
    for i in range(1, 10):
        print(get_fibonacci(i), end=',')

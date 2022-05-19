"""
描述
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
输入描述：
输入正整数N（N不大于100）
输出描述：
输出一个N行的蛇形矩阵。
示例1
输入：
4
输出：
1 3 6 10
2 5 9
4 8
7
"""
n = int(input())


def find(num_no):  # num_no是第几个数的意思
    if num_no == 1:
        return 1
    else:
        return find(num_no - 1) + num_no


# 先计算第一行
first_row = [str(find(i)) for i in range(1, n + 1)]
print(' '.join(first_row))
# 接下来的每一行等于上一行去掉第一个数后，每个数-1
for i in range(n - 1):
    first_row = list(map(lambda s: str(int(s) - 1), first_row[1:]))
    print(' '.join(first_row))

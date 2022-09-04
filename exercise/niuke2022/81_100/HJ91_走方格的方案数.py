'''
描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，
要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
注：沿棋盘格之间的边缘线行走
输入描述：
输入两个正整数n和m，用空格隔开。(1≤n,m≤8)
输出描述：
输出一行结果
示例1
输入：
2 2
输出：
6
'''
n, m = map(int, input().split())
n = n + 1
m = m + 1


def dfs(i, j):
    if i == n or j == m:
        return 0
    if i == n - 1 and j == m - 1:
        return 1
    # 向右
    r1 = dfs(i + 1, j)
    # 向下
    r2 = dfs(i, j + 1)
    return r1 + r2


print(dfs(0, 0))

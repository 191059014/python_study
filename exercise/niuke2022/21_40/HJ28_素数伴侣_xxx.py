"""
描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，
从已有的 N （ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，
如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。
输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。
输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数
输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。
示例1
输入：
4
2 5 6 13
输出：
2
示例2
输入：
2
3 6
输出：
0
"""
'''
匈牙利算法(求二分图的最大匹配):要用到递归,思想:后来者居上
首先要明确：奇数+偶数 的结果才有可能是素数
'''


def is_susu(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


total = int(input())
arr = list(map(int, input().split()))
jishu_arr = list(filter(lambda x: x % 2 == 1, arr))
oushu_arr = list(filter(lambda x: x % 2 == 0, arr))
is_select_arr = [[False] * len(oushu_arr)] * len(jishu_arr)


def dfs(jishu_arr, oushu_arr, is_select_arr):
    max_res = 0
    for i in range(len(jishu_arr)):
        for j in range(len(oushu_arr)):
            single_res = 0
            if not is_select_arr[i][j] and is_susu(jishu_arr[i] + oushu_arr[j]):
                is_select_arr[i][j] = True
                single_res = dfs(jishu_arr, oushu_arr, is_select_arr) + 1
                is_select_arr[i][j] = False
            max_res = max(max_res, single_res)
    return max_res


print(dfs(jishu_arr, oushu_arr, is_select_arr))

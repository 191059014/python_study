'''
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
输入描述：
输入两个正整数A和B。
输出描述：
输出A和B的最小公倍数。
示例1
输入：
5 7
输出：
35
'''
m, n = list(map(int, input().split()))
if n < m:
    m, n = n, m
res = 0
for i in range(m, m * n + 1, m):
    if i % m == 0 and i % n == 0:
        res = i
        break
print(res)

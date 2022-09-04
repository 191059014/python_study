'''
描述
Redraiment是走梅花桩的高手。Redraiment可以选择任意一个起点，从前到后，但只能从低处往高处的桩子走。他希望走的步数最多，
你能替Redraiment研究他最多走的步数吗？
输入描述：
数据共2行，第1行先输入数组的个数，第2行再输入梅花桩的高度
输出描述：
输出一个结果
示例1
输入：
6
2 5 1 5 4 5
输出：
3
说明：
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5 ，下标分别是 1 5 6
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5， 下标分别是 3 5 6
从第5格开始走最多有2步,4 5， 下标分别是 5 6
所以这个结果是3。
'''
while True:
    try:
        n, nums = int(input()), list(map(int, input().split()))
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # i前面有几个递增序列，可以演变成i-1前面的最长递增子序列+1
                    dp[i] = max(dp[i], dp[j] + 1)
        print(max(dp))
    except:
        break
# 下面通过dfs也可以算出来，但是会超时
# total, arr = int(input()), list(map(int, input().split()))
# res = [1]
#
#
# def dfs(arr, startIndex, step, res):
#     # 截至条件
#     if startIndex == len(arr) - 1:
#         res.append(step)
#         return None
#         # 候选人
#     for i in range(startIndex + 1, len(arr)):
#         # 往下执行的条件
#         if arr[startIndex] < arr[i]:
#             dfs(arr, i, step + 1, res)
#     res.append(step)
#
#
# for i in range(len(arr)):
#     dfs(arr, i, 1, res)
# print(max(res))

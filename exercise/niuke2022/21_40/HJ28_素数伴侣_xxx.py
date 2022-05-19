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
'''


# 1.判断是否是素数(若在1到该数平方根之间都没有可除尽的数)
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 2.寻找'增广路径'(这个数可否匹配,该跟谁连)
def find(odd, visited, choose, evens):
    for j, even in enumerate(evens):  # 扫描每个待被匹配的even
        if is_prime(odd + even) and not visited[j]:
            visited[j] = True
            if choose[j] == 0 or find(choose[j], visited, choose, evens):
                # 如果第j位even还没被选 或者 选它的那个odd还有别的选择even可以选择,那就把这位even让给当前的odd
                choose[j] = odd
                return True  # 说明匹配
    return False


# 3.开始odd先生和even小姐们入场,并各自到自己队列,开始匹配
while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        count = 0
        # 奇数+奇数 = 偶数, 偶数 + 偶数 = 偶数,都不能成为素数.只能奇数+偶数的组合才有可能
        odds, evens = [], []  # 把数分为奇数和偶数
        # 每次拿一个数,添加到对应的list里
        for num in nums:
            if num % 2 == 1:
                odds.append(num)
            else:
                evens.append(num)

        # 对每个odd,去找自己的even
        choose = [0] * len(evens)  # 用来装匹配这位even的对应的odd先生
        for odd in odds:
            visited = [False] * len(evens)
            if find(odd, visited, choose, evens):
                count += 1
        print(count)
    except:
        break

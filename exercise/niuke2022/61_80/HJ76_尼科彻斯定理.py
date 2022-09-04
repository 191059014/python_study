'''
描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
输入一个正整数m（m≤100），将m的立方写成m个连续奇数之和的形式输出。
输入描述：
输入一个int整数
输出描述：
输出分解后的string
示例1
输入：
6
输出：
31+33+35+37+39+41
'''
num = int(input())
res = []
if num % 2 == 0:
    center = num ** 2
    left = center - 1
    right = center + 1
    while len(res) < num:
        res.append(left)
        res.append(right)
        left -= 2
        right += 2

else:
    center = num ** 2
    left = center
    right = center
    res.append(center)
    while len(res) < num:
        left -= 2
        right += 2
        res.append(left)
        res.append(right)
res = list(sorted(res))
print('+'.join(map(str, res)))

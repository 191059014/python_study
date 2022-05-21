"""
描述
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
输入描述：
输入起始高度，int型
输出描述：
分别输出第5次落地时，共经过多少米以及第5次反弹多高。
注意：你可以认为你输出保留六位或以上小数的结果可以通过此题。
示例1
输入：
1
输出：
2.875
0.03125
"""
init_height = int(input())
# 共经过多少米
m = init_height
# 第5次的高度
h = init_height
for _ in range(4):
    h = h / 2
    m += 2 * h
print(m)
print(round(h / 2, 6))

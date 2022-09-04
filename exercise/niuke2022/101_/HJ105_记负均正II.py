'''
描述
输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾。
输入描述：
输入任意个整数，每行输入一个。
输出描述：
输出负数个数以及所有非负数的平均值
示例1
输入：
-13
-4
-7
输出：
3
0.0
'''
nums = []
while True:
    try:
        nums.append(float(input()))
    except Exception as e:
        break
z = [n for n in nums if n >= 0]
f = [n for n in nums if n < 0]
print(len(f))
print(round(sum(z) / len(z), 1))

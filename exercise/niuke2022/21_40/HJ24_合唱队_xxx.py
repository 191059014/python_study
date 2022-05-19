"""
描述
N 位同学站成一排，音乐老师要请最少的同学出列，使得剩下的 K 位同学排成合唱队形。
设KK位同学从左到右依次编号为 1，2…，K ，他们的身高分别为T_1,T_2,…,T_KT
 ，则称这KK名同学排成了合唱队形。
通俗来说，能找到一个同学，他的两边的同学身高都依次严格降低的队形就是合唱队形。
例子：
123 124 125 123 121 是一个合唱队形
123 123 124 122不是合唱队形，因为前两名同学身高相等，不符合要求
123 122 121 122不是合唱队形，因为找不到一个同学，他的两侧同学身高递减。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
注意：不允许改变队列元素的先后顺序 且 不要求最高同学左右人数必须相等
输入描述：
用例两行数据，第一行是同学的总数 N ，第二行是 N 位同学的身高，以空格隔开
输出描述：
最少需要几位同学出列
示例1
输入：
8
186 186 150 200 160 130 197 200
输出：
4
说明：
由于不允许改变队列元素的先后顺序，所以最终剩下的队列应该为186 200 160 130或150 200 160 130
"""


def LTS(data_list: list):
    """
    依次计算出每个元素左边的递增序列
    """
    lenArr = [1] * len(data_list)
    for i in range(len(data_list)):
        for j in range(i):
            if data_list[i] > data_list[j]:
                # 例如如果a3>a2，那么a3的递增序列等于（a3，a2+1）的最大值
                lenArr[i] = max(lenArr[i], lenArr[j] + 1)
    return lenArr


total_num, height_list = int(input()), [int(i) for i in input().split()]
# 假设从第i个元素分割，分别计算左边和右边的最长子序列，用总数减去最长子序列，即为最少删除的数量
left_arr = LTS(height_list)
right_arr = LTS(height_list[::-1])[::-1]
print(total_num - max([left_arr[i] + right_arr[i] - 1 for i in range(total_num)]))

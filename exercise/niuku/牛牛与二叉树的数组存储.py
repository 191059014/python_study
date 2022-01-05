"""
题目地址：https://blog.csdn.net/Fiveneves/article/details/104367919?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522163801847216780265471866%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=163801847216780265471866&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-23-104367919.first_rank_v2_pc_rank_v29&utm_term=%E6%95%B0%E7%BB%84%E4%BA%8C%E5%8F%89%E6%A0%91+%E7%89%9B%E5%AE%A2&spm=1018.2226.3001.4187
二叉树的结构可以用数组来存储：
    1.数组0下标不使用
    2.节点i的左子节点在位置为(2i)
    3.节点i的右子节点在位置为(2i+1)
    4.节点i的父节点在位置为(i/2)
    5.根节点被保存到数组下标为1的位置
"""
# 节点长度
node_length = int(input())
# 节点位置编号
node_no_arr = list(map(int, ('-1 ' + input()).split()))  # 数组下标0不使用，但是要放一个值，才能适合上述规则
# 真实节点的个数
real_no_arr = list(filter(lambda x: x != -1, node_no_arr))
print("The size of the tree is %s" % len(real_no_arr))
print("Node %s is the root node of the tree" % real_no_arr[0])
for i in range(1, len(real_no_arr) + 1):
    index = node_no_arr.index(i)
    father = -1
    if index != 1:
        father = node_no_arr[index // 2]
    left_child = -1
    if index * 2 < len(node_no_arr):
        left_child = node_no_arr[index * 2]
    right_child = -1
    if index * 2 + 1 < len(node_no_arr):
        right_child = node_no_arr[index * 2 + 1]
    print("The father of node %s is %s, the left child is %s, and the right child is %s" % (
        i, father, left_child, right_child))

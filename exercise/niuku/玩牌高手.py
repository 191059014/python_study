"""
给定一个长度为n的整型数组，表示一个选手在n轮内可选择的牌面分数。选手基于规则选牌，请计算所有轮结束后其可以获得的最高总分数。
选择规则如下：
在每轮里选手可以选择获取该轮牌面，则其总分数加上该轮牌面分数，为其新的总分数。
选手也可不选择本轮牌面直接跳到下一轮，此时将当前总分数还原为3轮前的总分数，若当前轮次小于等于3（即在第1、2、3轮选择跳过轮次），则总分数置为0。
选手的初始总分数为0，且必须依次参加每一轮。
输入描述:
第一行为一个小写逗号分割的字符串，表示n轮的牌面分数，1<= n <=20。
分数值为整数，-100 <= 分数值 <= 100。
不考虑格式问题。
输出描述:
所有轮结束后选手获得的最高总分数。
示例1
输入
    1,-5,-6,4,3,6,-2
输出
    11
说明
总共有7轮牌面。
第一轮选择该轮牌面，总分数为1。
第二轮不选择该轮牌面，总分数还原为0。
第三轮不选择该轮牌面，总分数还原为0。
第四轮选择该轮牌面，总分数为4。
第五轮选择该轮牌面，总分数为7。
第六轮选择该轮牌面，总分数为13。
第七轮如果不选择该轮牌面，则总分数还原到3轮1前分数，即第四轮的总分数4，如果选择该轮牌面，总分数为11，所以选择该轮牌面。
因此，最终的最高总分为11。
"""


def get_total_score_before_3():
    """
    获取3轮前总分数
    """
    return last_3_total_scores[0]


def flush_last_3_total_scores(current_max_total_score):
    """
    刷新最后3轮总分数
    """
    last_3_total_scores[0] = last_3_total_scores[1]
    last_3_total_scores[1] = last_3_total_scores[2]
    last_3_total_scores[2] = current_max_total_score


last_3_total_scores = [0, 0, 0]
text = input()
score_list = text.split(",")
max_total_score = 0
for i in range(len(score_list)):
    score = int(score_list[i])
    total_score_before_3 = get_total_score_before_3()
    print('当前分数：%s，当前总分数：%s，三轮前总分数：%s' % (score, max_total_score, total_score_before_3))
    if score > 0:
        # 分数为正数，选择该轮
        max_total_score += score
    else:
        if abs(score) >= max_total_score:
            # 分数为负，并且绝对值大于当前总分数，如果还选择该轮，总分数直接小于0了，所以放弃该轮
            max_total_score = total_score_before_3
        else:
            if sum((score, max_total_score)) < total_score_before_3:
                # 分数为负，绝对值小于当前总分数，并且与当前总分数的和小于3轮前的总分数，还不如不选择该轮
                max_total_score = total_score_before_3
            else:
                # 分数为负，绝对值小于当前总分数，并且与当前总分数的和大于3轮前的总分数，则依然选择该轮
                max_total_score = sum((score, max_total_score))
    if i >= 3:
        # 刷新最后三轮的总分数
        flush_last_3_total_scores(max_total_score)

print(max_total_score)

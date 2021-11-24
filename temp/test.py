"""
Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，但是他们有时会在开始或结束时
加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,123321->51233214　。
因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？
输入： ABBA
输出： 4
输入： ABBBA
输出： 5
输入： 12HHHHA
输出： 4
"""

text = 'orhbjkglzfwnosubzickolwgxgggujypokwqkpbuopkwwzfyuuyyruomhpqgngurvngwrtusvixmslbdwrfjxwxlvemcqmorkvmrrzukmvqgqlxtodmpgmeoonzmdvxrzenhjpztlbletwcmjppjhcmthwmjuofblzghbgbvgjbknkxdwtrrmuwxriubguoqwusudvispbguhltdlwivfdtkwhrnnhsmltqkzqxobxxkzyurtrbpfprquboqxbwouzssjwlrzldeupdwjrtbbycssxucdkokcqrgihjjvwltnwushbukbwqimcshyeifbncmlkikznmmoqcceczbyvddxbrgoivkdrxhwoczvrhtxkqtumzqogrruxffobgmehtosquuxvnbczkxljgwzztfjpbstphopwnwpwjlhfisoyxgksgytcjjefhddnkcenibcqtofngrkegxutuilnwbhigkhkbnbxiuesbtmldpohbeqbiupvzzhocjwksqlghiimbnsvjcijkugqjryqzqydllbzyjivixskyefmffivjmnotpywubhhtoyzvfomxpycjrtximksttfvymrohfozmtdvbeqnbggsoumoppwvtnofpxnecdlrosmeerwqrsgfjvkjhegnvljgiqhitqikrkkgbyhfzotjxwiwgmiblyzgymruetnxfdgdeloilkyipfiklzueqkidkryhlioryjvkwespxhebhqghyjphtqcmtwpyumflzwsozmexkhpfnztuwyxmhthpsfcdvxpqvdbnnkcqzoueftrjpgbkecitxix'

max_len = 0
for_num = 0


def find(leftIndex, rightIndex, strlen):
    """
    中心扩展思维
    """
    global max_len
    global for_num
    while leftIndex >= 0 and rightIndex < strlen and text[leftIndex] == text[rightIndex]:
        for_num += 1
        leftIndex -= 1
        rightIndex += 1
    if max_len < rightIndex - leftIndex - 1:
        max_len = rightIndex - leftIndex - 1


for i in range(len(text) - 1):
    # abba类型
    find(i, i+1, len(text))
    # aba类型
    find(i, i + 2, len(text))

print(max_len)
print(for_num)
print(len(text))

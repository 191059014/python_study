s = 'orhbjkglzfwnosubzickolwgxgggujypokwqkpbuopkwwzfyuuyyruomhpqgngurvngwrtusvixmslbdwrfjxwxlvemcqmorkvmrrzukmvqgqlxtodmpgmeoonzmdvxrzenhjpztlbletwcmjppjhcmthwmjuofblzghbgbvgjbknkxdwtrrmuwxriubguoqwusudvispbguhltdlwivfdtkwhrnnhsmltqkzqxobxxkzyurtrbpfprquboqxbwouzssjwlrzldeupdwjrtbbycssxucdkokcqrgihjjvwltnwushbukbwqimcshyeifbncmlkikznmmoqcceczbyvddxbrgoivkdrxhwoczvrhtxkqtumzqogrruxffobgmehtosquuxvnbczkxljgwzztfjpbstphopwnwpwjlhfisoyxgksgytcjjefhddnkcenibcqtofngrkegxutuilnwbhigkhkbnbxiuesbtmldpohbeqbiupvzzhocjwksqlghiimbnsvjcijkugqjryqzqydllbzyjivixskyefmffivjmnotpywubhhtoyzvfomxpycjrtximksttfvymrohfozmtdvbeqnbggsoumoppwvtnofpxnecdlrosmeerwqrsgfjvkjhegnvljgiqhitqikrkkgbyhfzotjxwiwgmiblyzgymruetnxfdgdeloilkyipfiklzueqkidkryhlioryjvkwespxhebhqghyjphtqcmtwpyumflzwsozmexkhpfnztuwyxmhthpsfcdvxpqvdbnnkcqzoueftrjpgbkecitxix'


def findlen(s):
    n = len(s)
    if n < 2:
        return s
    maxlen = 1

    def finder(left, right):
        nonlocal maxlen
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # 退出循环的时候正面两边不满足条件，但是left和right需要用扩展前的
        if right - left - 1 > maxlen:
            maxlen = right - left - 1

    for i in range(n):
        finder(i, i)
        finder(i, i + 1)
    return maxlen


ret = findlen(s)
print(ret)
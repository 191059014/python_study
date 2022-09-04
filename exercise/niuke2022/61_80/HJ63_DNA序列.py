'''
描述
一个 DNA 序列由 A/C/G/T 四个字母的排列组合组成。 G 和 C 的比例（定义为 GC-Ratio ）是序列中 G 和 C 两个字母的总的出现次数除以
总的字母数目（也就是序列长度）。在基因工程中，这个比例非常重要。因为高的 GC-Ratio 可能是基因的起始点。
给定一个很长的 DNA 序列，以及限定的子串长度 N ，请帮助研究人员在给出的 DNA 序列中从左往右找出 GC-Ratio 最高且长度为 N 的第一个子串。
DNA序列为 ACGT 的子串有: ACG , CG , CGT 等等，但是没有 AGT ， CT 等等
输入描述：
输入一个string型基因序列，和int型子串的长度
输出描述：
找出GC比例最高的子串,如果有多个则输出第一个的子串
示例1
输入：
ACGT
2
输出：
CG
说明：
ACGT长度为2的子串有AC,CG,GT3个，其中AC和GT2个的GC-Ratio都为0.5，CG为1，故输出CG
'''
dna = input()
sub_len = int(input())
target_radio = 0
target_sub_dna = ''
for i in range(len(dna)):
    end_index = i + sub_len
    if end_index > len(dna):
        continue
    sub_dna = dna[i:end_index]
    cg_count = sub_dna.count('C') + sub_dna.count('G')
    radio = cg_count / sub_len
    if target_radio < radio:
        target_radio = radio
        target_sub_dna = sub_dna
print(target_sub_dna)

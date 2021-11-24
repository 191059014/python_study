"""
1、对输入的字符串进行加解密，并输出。
2、加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。
3、解密方法为加密的逆过程。
本题含有多组样例输入。
数据范围：输入的两个字符串长度满足  ，保证输入的字符串都是大小写字母或者数字
输入描述：
    输入一串要加密的密码
    输入一串加过密的密码
输出描述：
    输出加密后的字符
    输出解密后的字符
示例1
    输入：
        abcdefg
        BCDEFGH
    输出：
        BCDEFGH
        abcdefg
示例2
    输入：
        2OA92AptLq5G1lW8564qC4nKMjv8C
        B5WWIj56vu72GzRja7j5
        2gRSPzofpXZc8EHc5D3c2a5M04M47CAcVbjiCBjatOtM99W64
        2LQL3p4bf3k006a2YODG0r6fpeKohN4aY27ZImecaGArf2VzXM104Y3O7XiwuqmV
    输出：
        3pb03bQUmR6h2Mx9675Rd5OlnKW9d
        a4vvhI45UT61fYqIZ6I4
        3HstqAPGQyaD9fiD6e4D3B6n15n58dbDwCKJdcKBUpUn00x75
        1kpk2O3AE2J995Z1xncf9Q5EODjNGm3Zx16yhLDBZfzQE1uYwl093x2n6wHVTPLu
"""
encode_critical_point = {"9": "0", "z": "A", "Z": "a"}
decode_critical_point = {"0": "9", "A": "Z", "a": "z"}


def encode(str_input):
    new_str = ''
    for ch in str_input:
        new_ch = ch
        if ch in encode_critical_point:
            new_ch = encode_critical_point[ch]
        elif ch.isalpha():
            new_ch = chr(ord(ch) + 1)
            new_ch = new_ch.swapcase()
        elif ch.isnumeric():
            new_ch = str(int(ch) + 1)
        else:
            pass
        new_str += new_ch
    return new_str


def decode(str_input):
    new_str = ''
    for ch in str_input:
        new_ch = ch
        if ch.isalpha():
            # 解密的时候，先转换大小写
            ch = ch.swapcase()
            if ch in decode_critical_point:
                new_ch = decode_critical_point[ch]
            else:
                new_ch = chr(ord(ch) - 1)
        elif ch.isnumeric():
            if ch in decode_critical_point:
                new_ch = decode_critical_point[ch]
            else:
                new_ch = str(int(ch) - 1)
        else:
            pass
        new_str += new_ch
    return new_str


while True:
    try:
        str_input1 = input()
        str_input2 = input()
        print(encode(str_input1))
        print(decode(str_input2))
    except:
        break

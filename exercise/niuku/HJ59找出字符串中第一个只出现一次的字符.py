"""
找出字符串中第一个只出现一次的字符
数据范围：输入的字符串长度满足
输入描述：
    输入几个非空字符串
输出描述：
    输出第一个只出现一次的字符，如果不存在输出-1
输入：
    asdfasdfo
    aabb
输出：
    o
    -1
"""
while True:
    try:
        text = input()
        result = ''
        for ch in text:
            count = text.count(ch)
            if count == 1:
                result = ch
                break
        if result:
            print(result)
        else:
            print(-1)
    except:
        break

"""
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
输入描述：
一组字符串。
输出描述：
如果符合要求输出：OK，否则输出NG
示例1
输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出：
OK
NG
NG
OK
"""
result = []
while True:
    try:
        user_input = input()
        if len(user_input) < 8:
            result.append('NG')
            continue
        exist = False
        count_set = set()
        for i in range(len(user_input) - 3):
            if user_input[i].isnumeric():
                count_set.add('Number')
            elif user_input[i].isalpha() and user_input[i].isupper():
                count_set.add('Upper')
            elif user_input[i].isalpha() and user_input[i].islower():
                count_set.add('Lower')
            else:
                count_set.add('Other')
            text = user_input[i] + user_input[i + 1] + user_input[i + 2]
            index = user_input.find(text, i + 3)
            if index > 0:
                exist = True
                break
        if len(count_set) < 3:
            result.append('NG')
            continue
        if exist:
            result.append('NG')
        else:
            result.append('OK')
    except Exception as e:
        break
for item in result:
    print(item)

'''
描述
问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（注：能被*和?匹配的字符仅由英文字母和数字0到9组成，下同）
？：匹配1个字符
注意：匹配时不区分大小写。
输入：
通配符表达式；
一组字符串。
输出：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
输入描述：
先输入一个带有通配符的字符串，再输入一个需要匹配的字符串
输出描述：
返回不区分大小写的匹配结果，匹配成功输出true，匹配失败输出false
示例1
输入：
te?t*.*
txt12.xls
输出：
false
'''
import re

ms, fs = input(), input()
m = '[a-zA-Z0-9]'
ms = ms.replace('?', m + '{1}')
ms = ms.replace('***', m + '{0,}')
ms = ms.replace('**', m + '{0,}')
ms = ms.replace('*', m + '{0,}')
pat = re.compile(ms, re.I)
match = pat.fullmatch(fs)
print('true' if match is not None else 'false')

'''
描述
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
输入描述：
输入一行，每行空格分割，分别是年，月，日
输出描述：
输出是这一年的第几天
示例1
输入：
2012 12 31
输出：
366
'''

year, month, day = input().split()
day_map = {"1": 31, "3": 31, "5": 31, "7": 31, "8": 31, "10": 31, "12": 31, "4": 30, "6": 30, "9": 30, "11": 30}
if (int(year) % 100 != 0 and int(year) % 4 == 0) or (int(year) % 100 == 0 and int(year) % 400 == 0):
    day_map.setdefault("2", 29)
else:
    day_map.setdefault("2", 28)
res = int(day)
for i in range(1, int(month)):
    res += day_map.get(str(i))
print(res)

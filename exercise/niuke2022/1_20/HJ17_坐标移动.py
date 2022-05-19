"""
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，
并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
输入描述：
一行字符串
输出描述：
最终坐标，以逗号分隔
示例1
输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出：
10,-10
示例2
输入：
ABC;AKL;DA1;
复制
输出：
0,0
"""
import re

reg = '(A|D|W|S)([0-9]{1,2})'


def is_command_yes(command):
    return re.fullmatch(reg, command)


def parse_command(command):
    matcher = re.match(reg, command)
    return matcher.group(1), int(matcher.group(2))


valid_command_list = []
x = 0
y = 0
for command in input().split(';'):
    if is_command_yes(command):
        valid_command_list.append(command)
for command in valid_command_list:
    flag, num = parse_command(command)
    if flag == 'A':
        x -= num
    elif flag == 'D':
        x += num
    elif flag == 'W':
        y += num
    elif flag == 'S':
        y -= num
print('%s,%s' % (x, y))

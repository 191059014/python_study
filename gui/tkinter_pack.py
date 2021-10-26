from tkinter import *


def print_radio_value():
    print('单选按钮的值：%s' % radioVariable.get())


def print_check_value():
    checkValues = []
    for str in checkVariables:
        str_val = str.get()
        if str_val:
            checkValues.append(str_val)
    print('复选按钮的值：%s' % checkValues)


root = Tk()
# 第一个是指窗口的宽度，第二个窗口的高度，第三个窗口左上点离左屏幕边界距离，第四个窗口左上点离上面屏幕边界距离
root.geometry("600x800+500+100")

"""
单选按钮
"""
frame1 = Frame(root, bg='yellow')
radioVariable = IntVar()
rb1 = Radiobutton(frame1, text='男', variable=radioVariable, value=1, command=print_radio_value)
rb2 = Radiobutton(frame1, text='女', variable=radioVariable, value=0, command=print_radio_value)
rb1.pack(anchor=W)
rb2.pack(anchor=W)
frame1.pack(padx=10, pady=10, fill='x')
"""
复选框
"""
frame2 = Frame(root, bg='green')
checkVariables = []
btnTextList = ['西施', '貂蝉', '王昭君', '杨玉环']
for btnText in btnTextList:
    checkVariables.append(StringVar())
    cb = Checkbutton(frame2, text=btnText, variable=checkVariables[-1], onvalue=btnText, offvalue='',
                     command=print_check_value)
    cb.pack(anchor=W)
frame2.pack(padx=10, pady=10, fill='x')
"""
label标签
"""
frame3 = Frame(root, bg='yellow')
textLabel = Label(frame3,
                  text='Python 是一种解释型、面向对象、动态数据类型的高级程序设计语言。\nPython 由 Guido van Rossum 于 1989 年底发明，第一个公开发行版发行于 1991 年。',
                  justify=LEFT)
textLabel.pack(side=LEFT, anchor=W)
photo = PhotoImage(file='qq.png')
imageLabel = Label(frame3, image=photo)
imageLabel.pack(side=RIGHT)
frame3.pack(padx=10, pady=10, fill='x')
# 背景图片
frame4 = Frame(root, bg='green')
bgPhoto = PhotoImage(file='bg.png')
textLabel = Label(frame4,
                  text='学习Python很快乐^_^',
                  image=bgPhoto,
                  compound=CENTER,
                  font=("华文行楷", 20),
                  fg='white')
textLabel.pack()
frame4.pack(padx=10, pady=10, fill='x')
"""
label容器
"""
group = LabelFrame(root, text='最好的脚本语言是？')
langs = [('Python', 1), ('Perl', 2), ('Ruby', 3), ('Lua', 4)]
r_variable = IntVar()
for lang, num in langs:
    print(lang, num)
    rb = Radiobutton(group, text=lang, variable=r_variable, value=num, indicatoron=False)
    rb.pack(anchor=W)
group.pack(padx=10, pady=10, fill='x')

# 进入消息循环
mainloop()

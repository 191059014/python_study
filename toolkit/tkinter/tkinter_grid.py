import tkinter.messagebox
from tkinter import *

root = Tk()

Label(root, text='账号：').grid(row=0, column=0)
Label(root, text='密码：').grid(row=1, column=0)

user_name = StringVar()
password = StringVar()
e1 = Entry(root, textvariable=user_name)
e2 = Entry(root, textvariable=password, show='*')
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    tkinter.messagebox.showinfo(title='提示框', message='账号：%s，密码：%s' % (e1.get(), e2.get()))


Button(root, text='确定', width=10, command=show).grid(row=3, column=0, padx=10, pady=5, sticky=W)
Button(root, text='取消', width=10, command=root.quit).grid(row=3, column=1, padx=10, pady=5, sticky=E)

# 进入消息循环
mainloop()

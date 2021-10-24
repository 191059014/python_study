import tkinter as tk
import tkinter.messagebox as messagebox


def say_hi():
    print('hi')
    messagebox.showinfo(title='提示', message="how are you")


# 创建父窗口对象
root_window = tk.Tk()
# 创建Frame
frame_1 = tk.Frame(root_window)
frame_1.pack(padx=10, pady=10)
# 创建按钮
btn_1 = tk.Button(frame_1, bg='blue', fg='white', text='按钮1', command=say_hi)
btn_2 = tk.Button(frame_1, bg='blue', fg='white', text='按钮2', command=say_hi)
btn_3 = tk.Button(frame_1, bg='blue', fg='white', text='按钮3', command=say_hi)
# 调整位置
btn_1.pack(side='left')
btn_2.pack(side='left')
btn_3.pack(side='left')

# 进入消息循环
root_window.mainloop()

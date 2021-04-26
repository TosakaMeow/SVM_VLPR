import tkinter as tk
import Function
from tkinter import messagebox
import UI_main

def loginSystem():
    account = entryAcc.get()
    password = entryPwd.get()
    res = Function.loginSystem(account, password)
    if res == 1:
        messagebox.showerror(title='登录失败', message='出错了！请检查账号密码是否匹配，如果忘记密码联系管理员！')
    else:
        UI_main.mainF()
def regSystem():
    account = entryAcc.get()
    password = entryPwd.get()
    res = Function.regSystem(account, password)
    if res == 1:
        messagebox.showerror(title='注册失败', message='该账号已被注册，请直接使用密码进行登录！')
    else:
        messagebox.showinfo(title='注册成功', message='账号注册成功，现在可以使用此账号密码进行登录了！')

window = tk.Tk()
window.title('登录到系统')
window.geometry('480x240')

acc = tk.Label(window, text='账号:', font=('Arial', 16))
acc.place(x=50, y=40)
pwd = tk.Label(window, text='密码:', font=('Arial', 16))
pwd.place(x=50, y=100)

entryAcc = tk.Entry(window, show=None, font=('Arial', 16))
entryAcc.place(x=120, y=40)
entryPwd = tk.Entry(window, show='*', font=('Arial', 16))
entryPwd.place(x=120, y=100)

emergency = tk.Button(window, text="注册信息", width=10, height=1, font=('Arial', 12), command=regSystem)
emergency.place(x=120, y=140)

login = tk.Button(window, text="登录系统", width=10, height=1, font=('Arial', 12), command=loginSystem)
login.place(x=240, y=140)

window.mainloop()


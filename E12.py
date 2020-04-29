import tkinter as tk
def func():
    if ent1.get() == 'admin' and ent2.get() == '12345' :
        btn1.config(background = 'green')
    else :
        btn1.config(background = 'red')
win = tk.Tk()
lb1 = tk.Label(win,text = 'username')
ent1 = tk.Entry(win)
lb2 = tk.Label(win,text = 'password')
ent2 = tk.Entry(win)
btn1 = tk.Button(win,text = 'click here',command = func)

lb1.pack()
ent1.pack()
lb2.pack()
ent2.pack()
btn1.pack()

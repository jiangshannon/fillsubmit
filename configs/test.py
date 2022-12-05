# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2022/7/28
# @software:PyCharm
import random
import threading
import time
import tkinter as tk


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title("病毒")
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(
        text='病毒入侵',
        bg='Red',
        fon=('楷体', 17),
        width=15, height=2
    ).pack()
    window.mainloop()


threads = []
for i in range(9):
    t = threading.Thread(target=dow)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
dow()

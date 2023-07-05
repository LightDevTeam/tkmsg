import ctypes
import tkinter as tk
import sys
import time
from tkinter import ttk

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)

def msgbox(title,text,btn=None,tips=None):
    global window
    if btn==None:
        btn = 'OK'
    btn = f' {btn} '
    window = tk.Tk()
    window.title(title)
    window.config(bg='white')
    window.geometry('550x180')
    tk.Label(window,text=text,bg='white',font=(('Arial',12))).place(x='10',y='15')
    def close(event):
        window.destroy()
    def bg(event):
        lb.configure(bg='deepskyblue')
    def bbg(event):
        lb.configure(bg='orange')
    lb = tk.Label(window,text=btn,bg='orange',fg='white',cursor='hand2',font=(('Arial','12')))
    lb.place(x='480',y='130')
    lb.bind('<Button-1>',close)
    lb.bind('<Enter>',bg)
    lb.bind('<Leave>',bbg)
    if tips==None:
        tips = None
    else:
        tk.Label(window,text=tips,bg='white',fg='deepskyblue',font=(('Arial','8'))).place(x='0',y='160')
    window.mainloop()
def inputbox(title,text,btn=None,tips=None,width=None):
    global window
    if btn==None:
        btn = 'OK'
    btn = f' {btn} '
    window = tk.Tk()
    window.title(title)
    window.config(bg='white')
    window.geometry('550x180')
    tk.Label(window,text=text,bg='white',font=(('Arial',12))).place(x='10',y='15')
    def close(event):
        global response
        response = inputbox_frame.get()
        window.destroy()
    def bg(event):
        lb.configure(bg='deepskyblue')
    def bbg(event):
        lb.configure(bg='orange')
    lb = tk.Label(window,text=btn,bg='orange',fg='white',cursor='hand2',font=(('Arial','12')))
    lb.place(x='480',y='130')
    lb.bind('<Button-1>',close)
    lb.bind('<Enter>',bg)
    lb.bind('<Leave>',bbg)
    inputbox_frame = ttk.Entry(window,width='50')
    inputbox_frame.place(x='10',y='75')
    if tips==None:
        tips = None
    else:
        tk.Label(window,text=tips,bg='white',fg='deepskyblue',font=(('Arial','10'))).place(x='0',y='160')
    window.mainloop()
    return response

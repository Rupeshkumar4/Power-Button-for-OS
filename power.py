from logging import root
from sys import maxsize
from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -l")
def shutdown():
    os.system("shutdown /s /t 1")
root=Tk()
root.title("power option")
root.geometry("440x540")
#root.config(bg="grey")
root.maxsize(440,540)
root.minsize(220,320)
re_button=Button(root,text="Restart",bg="grey",fg="skyblue",
                      command=restart)
re_button.pack()
rb_button=Button(root,text="Restart Time",bg="grey",fg="skyblue",command=restart_time).pack()
sh_button=Button(root,text="Shutdown",bg="grey",fg="skyblue",command=shutdown).pack()
lg_button=Button(root,text="Log out",bg="grey",fg="skyblue",command=logout).pack()

root.mainloop()
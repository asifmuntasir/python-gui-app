import os
import time
import tkinter

def shutdown():
    os.system("shutdown /s /t 2")
    
def restart():
    os.system("shutdown /r /t 2")
    
def sleepmode():
    os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")

root = tkinter.Tk()
root.title("PC Shutdown")
root.geometry("250x200")

#Shutdown button
btn_s = tkinter.Button(root, text = "Shutdown", command=shutdown,bg="yellowgreen")
btn_s.place(x=90,y=45)

#Restart button
btn_r = tkinter.Button(root, text = "Restart", command=restart, bg="cyan")
btn_r.place(x=100,y=80)

#Sleep button
btn_s = tkinter.Button(root, text = "Sleep", command=sleepmode, bg="yellow")
btn_s.place(x=102.5,y=115)

root.mainloop()



from tkinter import * 
import time


root = Tk()

root.title("Time At Check")
root.geometry("400x200")
#root.iconbitmap("pyTimeimg.ico")


def clock():
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")

    lbl.config(text=hr + ":" + min + ":" + sec)
    lbl.after(1000,clock)


lbl=Label(root, text="", fg="black" , bg="#66ffcc", width= 50, height= 2 )
lbl.pack(pady=0)

clock()

root.mainloop()


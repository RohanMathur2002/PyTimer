from tkinter import * 
import time

def clock():
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")

    lbl.config(text=hr + ":" + min + ":" + sec)
    lbl.after(1000,clock) 

s1=0
s2=0
s3=0
m1=0
m2=0
m3=0
h1=0
h2=0
h3=0
#----------------------------------------------------------------
def play1():
    global s1,m1,h1 
    if s1==60:
        s1=0
        m1= m1+1
    else:
        s1=s1+1

    if m1== 60:
        m1=0
        h1=h1+1

def play2():
    global s2 , m2 , h2 
    if s2==60:
        s2=0
        m2= m2+1
    else:
        s2=s2+1

    if m2== 60:
        m2=0
        h2=h2+1

def play3():
    global s3 , m3 , h3
    if s3==60:
        s3=0
        minn= minn+1
    else:
        s3=s3+1

    if m3== 60:
        m3=0
        h3=h3+1
#-------------------------------------------------------------------

def c1():
    play1()
    lbl1.config(text=str(h1) + ":" + str(m1) + ":" + str(s1))
    lbl1.after(1000,c1)
def c2():
    play2()
    lbl2.config(text=str(h2) + ":" + str(m2) + ":" + str(s2))
    lbl2.after(1000,c2)
def c3():
    play3()
    lbl3.config(text=str(h3) + ":" + str(m3) + ":" + str(s3))
    lbl3.after(1000,c3)

#_____________________________________________________________________________________________
root = Tk()

root.title("Time At Check")
root.geometry("400x200")
# root.iconbitmap("C:\Users\Rohan Mathur\Downloads\pyTimeimg.ico")


#--------------------------------------------------------------
lbl=Label(root, text="", fg="black" , bg="#66ffcc" , width= 60)
lbl.grid(row=0, column=0, columnspan=9, pady=0)

lbl1=Label(root, text="", fg="black" , bg="#725B5B")
lbl1.grid(row=2, column=1, columnspan=3, pady=0)

lbl2=Label(root, text="", fg="black" , bg="#725B5B")
lbl2.grid(row=2, column=2, columnspan=3, pady=0)

lbl3=Label(root, text="", fg="black" , bg="#725B5B")
lbl3.grid(row=2, column=3, columnspan=3, pady=0)
#-------------------------------------------------------------------------

b1=Button(text="Start", command=c1)
b1.grid(row=4, column=1)

b2=Button(text="Start", command=c2)
b2.grid(row=4, column=3)

b3=Button(text="Start", command=c3)
b3.grid(row=4, column=5)
#---------------------------------------------------------------------------

clock()

root.mainloop()
#___________________________________________________________________________________________

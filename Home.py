from tkinter import *
from PIL import Image,ImageTk
from subprocess import call

root = Tk()
root.title("Home")
root.geometry("800x533+100+50")

def Att():
    call(["python","main.py"])

def Add():
    call(["python","AddStud.py"])

def Del():
    call(["python","DelStud.py"])

def View():
    call(["python","ViewStud.py"])

bg=ImageTk.PhotoImage(file="f2.jpg")
bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)


photo4 = PhotoImage(file="i1.png")
Button(root, image=photo4, command=Att).place(x=50,y=50,height=120,width=120)
Label(root,text="Take Attandance",font=("Verdana",10)).place(x=50,y=180)

photo2 = PhotoImage(file="add.png")
Button(root, image=photo2, command=Add).place(x=630,y=50,height=120,width=120)
Label(root,text="ADD Student",font=("Verdana",10)).place(x=650,y=180)


photo3 = PhotoImage(file="remove.png")
Button(root, image=photo3, command=Del).place(x=50,y=350,height=120,width=120)
Label(root,text="Remove Student",font=("Verdana",10)).place(x=50,y=480)

photo1 = PhotoImage(file="atta.png")
Button(root, image=photo1, command=View).place(x=630,y=350,height=120,width=120)
Label(root,text="View Student",font=("Verdana",10)).place(x=644,y=480)
root.mainloop()
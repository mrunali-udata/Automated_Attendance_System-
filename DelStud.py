from tkinter import *
from  PIL import ImageTk,Image
from  tkinter import filedialog
from tkinter import messagebox
import mysql.connector
from subprocess import call
import os

root = Tk()
root.title("Delete Student")
root.geometry("640x500")


mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()


# Image create
image=Image.open("back.jpg")
photo=ImageTk.PhotoImage(image)

# create canvas
my_canvas=Canvas(root,width=400, height=400)
my_canvas.pack(fill="both", expand=True)

# set image to canvas
my_canvas.create_image(0,0,image=photo,anchor="nw")

def save():
    global my_image
    global myresult
    if(rollno.get()==""):
        messagebox.showerror("showerror", "Enter Roll No of Student to Search")
    else:
        sql="SELECT * FROM Stud WHERE rollno= %s"
        val=(rollno.get(),)

        mycursor.execute(sql, val)
        myresult=mycursor.fetchone()
        if(myresult==None):
            messagebox.showerror("Show Error","Student Not Fount")
        else:
            print(myresult[0], myresult[1], myresult[2], myresult[3], )
            username.set(myresult[1])
            year.set(myresult[3])
            my_image = ImageTk.PhotoImage(Image.open(myresult[0]))
            my_lab = Label(image=my_image).place(x="420", y="100px")


def openimg():
    if (rollno.get() == ""):
        messagebox.showerror("showerror", "Select Student By Entering Roll No")

    else:
        sql = "SELECT * FROM Stud WHERE rollno= %s"
        val = (rollno.get(),)

        mycursor.execute(sql, val)
        myresult = mycursor.fetchone()
        if (myresult == None):
            messagebox.showerror("Show Error", "Student Not Fount")
        else:
            path = "Student" + chr(92) + textbox1.get() + ".jpg"
            os.remove(myresult[0])
            os.remove(path)
            sql = "DELETE FROM Stud WHERE rollno = %s"
            val = (rollno.get(),)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo("showinfo","1 record deleted")


#add Photo
button1=Button(root,text="Delete",bd=3,font=("Goudy old style",15),command=openimg)
button1_window=my_canvas.create_window(450,350,anchor="nw",window=button1)
button2=Button(root,text="Search",bd=3,font=("Goudy old style",15),command=save)
button2_window=my_canvas.create_window(150,350,anchor="nw",window=button2)

# add text(Label)
my_canvas.create_text(330,70,text="Delete Student",font=("Impact",25),fill="white")
my_canvas.create_text(100,150,text="Name",font=("Goudy 12 bold"),fill="white")
my_canvas.create_text(100,210,text="Roll No",font=("Goudy 12 bold"),fill="white")
my_canvas.create_text(100,270,text="Year",font=("Goudy 12 bold"),fill="white")


# add Entry
username=StringVar(root,name="user")
rollno=StringVar(root,name="pass")
year=StringVar(root,name="year")

textbox1=Entry(root,bd=3,textvariable=username,width=30)

textbox1_window=my_canvas.create_window(150,140,anchor="nw",window=textbox1)

textbox2=Entry(root,bd=3,textvariable=rollno,width=10)

textbox2_window=my_canvas.create_window(150,200,anchor="nw",window=textbox2)

textbox3=Entry(root,bd=3,textvariable=year,width=10)

textbox3_window=my_canvas.create_window(150,260,anchor="nw",window=textbox3)

root.mainloop()
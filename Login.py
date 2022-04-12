from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from subprocess import call
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()
root=Tk()
root.title("Login")
root.geometry("600x350")




#Function for Login
def login():
    if(username.get()!="" and password.get()!=""):
        #print(username.get())
        #print(password.get())
        sql = "SELECT * FROM login WHERE name = %s"
        adr = (username.get(),)

        mycursor.execute(sql, adr)

        myresult = mycursor.fetchone()

        print(myresult[1])
        if(myresult[1]==password.get()):
            messagebox.showinfo("Correct", "Login Successfully")
            call(["python","Home.py"]) #Name of Home Page
        else:
            messagebox.showerror("Wrong", "Login Unsuccessfully")
    else:
        messagebox.showerror("showerror", "Enter Both UserName And Password")

#Function for Sign In
def signin():
    if (username.get() != "" and password.get() != ""):
        # print(username.get())
        # print(password.get())
        sql = "SELECT * FROM login WHERE name = %s"
        adr = (username.get(),)

        mycursor.execute(sql, adr)

        myresult = mycursor.fetchone()

        if(myresult==None):
            sql = "INSERT INTO login (name, password) VALUES (%s, %s)"
            val = (username.get(), password.get())

            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            call(["python","dbex.py"]) #Name of Home Page except dbex
        else:
            messagebox.showerror("Error", "You Already have an account")
    else:
        messagebox.showerror("showerror", "Enter Both UserName And Password")


# Image create
image=Image.open("bgg2.jpg")
photo=ImageTk.PhotoImage(image)

# create canvas
my_canvas=Canvas(root,width=560, height=461)
my_canvas.pack(fill="both", expand=True)

# set image to canvas
my_canvas.create_image(0,0,image=photo,anchor="nw")


# add text(Label)
my_canvas.create_text(200,70,text="Face Recognization \nAttendance System",font=("Impact",25),fill="white")
my_canvas.create_text(100,150,text="UserName",font=("Goudy 12 bold"),fill="white")
my_canvas.create_text(100,210,text="Password",font=("Goudy 12 bold"),fill="white")

# add Buttons

button1=Button(root,text="Login",bg="royalblue4",fg="white",bd=5,font=("Goudy old style",15),command=login)
button1_window=my_canvas.create_window(70,280,anchor="nw",window=button1,width=100,height=40)

button2=Button(root,text="Sign in",bg="royalblue4",fg="white",bd=5,font=("Goudy old style",15),command=signin)
button2_window=my_canvas.create_window(210,280,anchor="nw",window=button2,width=100,height=40)

# add Entry
username=StringVar(root,name="user")
password=StringVar(root,name="pass")

textbox1=Entry(root,bd=3,textvariable=username)

textbox1_windoe=my_canvas.create_window(150,140,anchor="nw",window=textbox1)

textbox2=Entry(root,bd=3,textvariable=password)

textbox2_windoe=my_canvas.create_window(150,200,anchor="nw",window=textbox2)
root.mainloop()


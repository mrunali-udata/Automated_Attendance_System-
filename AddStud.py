from tkinter import *
from  PIL import ImageTk,Image
from  tkinter import filedialog
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


root = Tk()
root.title("Add Student")
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
    sql="INSERT INTO Stud (img,name,rollno,year) VALUES (%s, %s, %s, %s)"
    val=(path,textbox1.get(),textbox2.get(),n.get())
    mycursor.execute(sql, val)
    mydb.commit()
    print("Done")
    print(year.get())
    print(path)
    messagebox.showinfo("Info","1 Student Added")


def openimg():
    global my_image
    global my_image1
    global path
    root.filename = filedialog.askopenfilename(initialdir="/This PC", title="Select A Photo",filetypes=(("png files", "*.png"), ("all files", "*.*")))
    #my_lable = Label(root, text=root.filename).pack(side=RIGHT)

    my_image1=Image.open(root.filename)
    my_image2=Image.open(root.filename)
    """newsize=(4000,6000)
    my_image1=my_image1.resize(newsize)"""
    path="Student" + chr(92) + textbox1.get() + ".jpg"
    print(path)
    print(type(path))
    print(path)
    my_image1=my_image1.save(path)

    newsize1 = (140, 150)
    my_image2 = my_image2.resize(newsize1)
    path = "Student Photos" + chr(92) + textbox1.get() + ".jpg"
    print(path)
    print(type(path))
    print(path)
    my_image2 = my_image2.save(path)

    my_image = ImageTk.PhotoImage(Image.open(path))
    my_lab = Label(image=my_image).place(x="420",y="100px")

#add Photo
button1=Button(root,text="Add Photo",font=("Goudy old style",10),command=openimg)
button1_window=my_canvas.create_window(460,300,anchor="nw",window=button1)
button2=Button(root,text="Submit",bd=3,font=("Goudy old style",15),command=save)
button2_window=my_canvas.create_window(80,350,anchor="nw",window=button2)

# add text(Label)
my_canvas.create_text(330,70,text="Add Student",font=("Impact",25),fill="white")
my_canvas.create_text(100,150,text="Name",font=("Goudy 12 bold"),fill="white")
my_canvas.create_text(100,210,text="Roll No",font=("Goudy 12 bold"),fill="white")
my_canvas.create_text(100,270,text="Year",font=("Goudy 12 bold"),fill="white")


# add Entry
username=StringVar(root,name="user")
rollno=StringVar(root,name="pass")

textbox1=Entry(root,bd=3,textvariable=username,width=30)

textbox1_window=my_canvas.create_window(150,140,anchor="nw",window=textbox1)

textbox2=Entry(root,bd=3,textvariable=rollno,width=10)

textbox2_window=my_canvas.create_window(150,200,anchor="nw",window=textbox2)

#Add ComboBox
# Combobox creation
n = StringVar(root,name="year")
year = ttk.Combobox(root, width = 10, textvariable = n)
year['values'] = ('I Year','II Year','III Year')
year_window=my_canvas.create_window(150,260,anchor="nw",window=year)
# Shows I year as a default value

year.current(0)
root.mainloop()
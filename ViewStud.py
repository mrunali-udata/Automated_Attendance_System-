from tkinter import *
from  PIL import ImageTk,Image
from  tkinter import filedialog
from tkinter import ttk
import mysql.connector
import pyttsx3
import os
from tkinter import messagebox

root=Tk()
root.title("View Student")
root.geometry("600x480")
mydb=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
mycursor=mydb.cursor()

def show():
  # Text to Speech
  speaker = pyttsx3.init()
  speaker.say('Kindly wait, the file is opening')
  speaker.runAndWait()

  os.startfile('Attendance.csv')
  print("Done")

# Image create
image=Image.open("back.jpg")
photo=ImageTk.PhotoImage(image)

# create canvas
my_canvas=Canvas(root,width=560, height=461)
my_canvas.pack(fill="both", expand=True)

# set image to canvas
my_canvas.create_image(0,0,image=photo,anchor="nw")

# add Entry

T = Text(root, height = 23, width = 62)

textbox1_windoe=my_canvas.create_window(50,40,anchor="nw",window=T)
T.insert(INSERT,"\n\t Name \t\t Roll No \t\t Year ")
T.insert(INSERT,"\n ____________________________________________________________")

mycursor.execute("SELECT * FROM Stud")

myresult = mycursor.fetchall()

for x in myresult:
  T.insert(INSERT,"\n\n\t "+x[1]+" \t\t "+x[2]+"\t\t "+x[3])

button1=Button(root,text="Attendance",font=("Goudy old style",12),command=show).place(x=250,y=420,height=30,width=100)
root.mainloop()
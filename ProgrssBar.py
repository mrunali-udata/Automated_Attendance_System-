from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
import time
import pyttsx3
from subprocess import call

root = Tk()
root.geometry("900x392+100+50")
root.title("ProgressBar")
root.resizable(False,False)


bg=ImageTk.PhotoImage(file="f5.jpg")
bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)


#to Start Progress bar
def start():
    # Text to Speech
    speaker = pyttsx3.init()
    speaker.say('wait, the system is staring')
    speaker.runAndWait()

    bar.place(x=50,y=260)
    task= 10
    x=0
    speed=1
    while(x<task):
        time.sleep(0.30)
        bar['value']+=10
        x+=speed
        percent.set(str(int((x/task)*100))+"%")
        root.update_idletasks()
    call(["python","Login.py"])



#logo
photo= PhotoImage(file="logo.PNG")
l1=Label(image=photo)
l1.place(x=120,y=100)
percent = StringVar()

bar=Progressbar(root,orient=HORIZONTAL,length=300)
bar.pack_forget()

percentLable = Label(root,textvariable=percent).place(x=355,y=262)

button=Button(root,text="Start the System",command=start).place(x=160,y=300)

root.mainloop()


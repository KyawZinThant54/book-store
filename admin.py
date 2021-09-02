#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os




#create winodw
root=Tk()
root.title("Book store")
root.iconbitmap("image\logo.ico")

#To get fit on window
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))

#=============function==========================

def counter():
    root.withdraw()
    os.system("python counter_manager.py")
    root.deiconify()

def Employees():
    root.withdraw()
    os.system("python employe_manager.py")
    root.deiconify()
    
#==========================Background_photo================================
bg_photo=ImageTk.PhotoImage(Image.open("image\BG.jpg").resize((window_width,window_height)))
#==================place on the window=========================
Label(root,image=bg_photo).place(relx=0,rely=0)


#==============open Admin logo=====================
Admin=ImageTk.PhotoImage(Image.open("image\counter.png").resize((200,200)))
#=============admin button==================
Button1= Button(root,image=Admin,borderwidth=3,bg="#cadbc3",command=counter).place(relx=0.2, rely=0.3,width=180,height=190)
Label(root,text="Counter",font=('Arial', 10),bg="#ede5dd").place(relx=0.2,rely=0.496)

#==============open Employe logo========================
Employe= ImageTk.PhotoImage(Image.open("image\workers.png",).resize((200,200)))
#===================employe botton======================
Button2= Button(root,image=Employe, borderwidth=3,bg="#cadbc3",command=Employees).place(relx=0.64,rely=0.3,width=180,height=195)
Label(root,text="Employees",font=('Arial',10),bg="#ede5dd").place(relx=0.64,rely=0.5)

root.mainloop()
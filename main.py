#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox

#Database connection

with sqlite3.connect("database.db")as db:
    cur=db.cursor()

#create winodw
root=Tk()

root.title("Book store")
root.iconbitmap("image\logo.ico")

#To get fit on window
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))

#=================variable==============
user=StringVar()
pasd=StringVar()

#==============function===========
def admin():
    global option
    login_window.deiconify()
    option='Admin'

def employee():
    global option
    login_window.deiconify()
    option='Employe'

def login():
    username=user.get()
    password=int(pasd.get())
    entry1.delete(0,END)
    entry2.delete(0,END)
    

    find_user = 'SELECT * FROM {} WHERE id = ? and password = ?'.format(option)

    print(username, password)
    cur.execute(find_user, [username, password])
    results = cur.fetchone()
    print(results)
    
    if results:
        print('login')
        root.withdraw()
        login_window.withdraw()
        os.system('python {}.py'.format(option))

    else:
        messagebox.showerror("Error", "Incorrect usename or password") 


#==========================Background_photo================================
bg_photo=ImageTk.PhotoImage(Image.open("image\BG.jpg").resize((window_width,window_height)))
#==================place on the window=========================
Label(root,image=bg_photo).place(relx=0,rely=0)

#==============open Admin logo=====================
Admin=ImageTk.PhotoImage(Image.open("image\owner.png").resize((200,200)))

#=============admin button==================
Button1= Button(root,image=Admin,borderwidth=3,bg="#cadbc3",command=admin).place(relx=0.2, rely=0.3,width=160,height=190)
Label(root,text="Admin",font=('Arial', 10),bg="#ede5dd").place(relx=0.2,rely=0.496)

#==============open Employe logo========================
Employe= ImageTk.PhotoImage(Image.open("image\employ.jpg").resize((200,200)))
#===================employe botton======================
Button2= Button(root,image=Employe, borderwidth=3,bg="#cadbc3",command=employee).place(relx=0.64,rely=0.3,width=160,height=195)
Label(root,text="Employe",font=('Arial',10),bg="#ede5dd").place(relx=0.64,rely=0.5)

#======Login window==========
login_window=Toplevel(root)

login_window.title("Login")
login_window.geometry("{}x{}+{}+{}".format(window_width//6, window_height//3,
                        int(window_width/2.6), window_height//3))
login_window.iconbitmap('image\Login.ico')

#login logo
Login=ImageTk.PhotoImage(Image.open("image\logoo.ico").resize((35,35)))
Label(login_window,image=Login).place(relx=0.07, rely=0.27)
Label(login_window,text='Username', font="-family {Poppins} -size 15" ).place(relx=0.1, rely=0.1)

#login entry
entry1=Entry(login_window)
entry1.place(relx=0.25,rely=0.31,relwidth=0.7,relheight=0.08)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user)


#psw logo
password=ImageTk.PhotoImage(Image.open("image\password.png").resize((35,35)))
Label(login_window,image=password).place(relx=0.07, rely=0.5)
Label(login_window,text='Username', font="-family {Poppins} -size 15" ).place(relx=0.1, rely=0.1)

#login entry
entry2=Entry(login_window)
entry2.place(relx=0.25,rely=0.53,relwidth=0.7,relheight=0.08)
entry2.configure(font="-family {Poppins} -size 10")
entry2.configure(relief="flat")
entry2.configure(textvariable=pasd)


#login button
Button3=TkinterCustomButton(master=login_window,corner_radius=18,text="LOGIN",command=login)
Button3.place(relx=0.5,rely=0.8, anchor=CENTER)

#hide
login_window.withdraw()























root.mainloop()
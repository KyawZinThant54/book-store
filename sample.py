#importing libraries
from tkinter import*
from PIL import ImageTk,Image
from custom_button import TkinterCustomButton

#create window
root=Tk()
root.title("Grocery store")
root.iconbitmap("image\logo.ico")

#To get fit on screen
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))

#==========variable==============
user =StringVar()
passwd =StringVar()

#=================function====================
 
def admin():
    login_window.deiconify()

def employe():
    login_window.deiconify()


#==========================Background photo==========================
bg_photo= Image.open("image\BG.jpg")
bg_photo=bg_photo.resize((window_width,window_height),Image.ANTIALIAS)
bg_photo=ImageTk.PhotoImage(bg_photo)

#place on the window
Label(root,image=bg_photo).place(relx=0,rely=0)

#==============Admin Button==============================
admin_logo =ImageTk.PhotoImage(Image.open('image\owner.png').resize((200,200)))

# #create Admin Button
Button1=Button(root,image=admin_logo,borderwidth=3,bg="#cadbc3",relief=RIDGE,command=admin)
Button1.place(relx=0.1, rely=0.4,width=160,height=190)
Label(root,text="Admin",font=('Arial', 12),bg="#ede5dd").place(relx=0.1,rely=0.593)

#=============employe button==============
employe_logo=ImageTk.PhotoImage(Image.open("image\employe.png").resize((200,200)))

#create Employe Button
Button2=Button(root,image=employe_logo,borderwidth=3,bg="#cadbc3",relief=RIDGE,command=employe)
Button2.place(relx=0.64,rely=0.411,width=150,height=190)
Label(root,text="Employe",font=('Arial', 12),bg="#ede5dd").place(relx=0.64,rely=0.6)


#================ Login Screen===================
login_window = Toplevel(root)
from tkinter import*
from PIL import ImageTk,Image

login_window.title("Login")
login_window.geometry("{}x{}+{}+{}".format(window_width//6, window_height//3,
                        int(window_width/2.8), window_height//3))
login_window.iconbitmap('image\Login.ico')

#login logo
Login= ImageTk.PhotoImage(Image.open("image\logoo.ico").resize((20, 20)))
Label(login_window,image=Login).place(relx=0.1, rely=0.2)
Label(login_window,text='Username', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.1)

#login entry
entry1=Entry(login_window)
entry1.place(relx=0.25,rely=0.2,relwidth=0.7,relheight=0.08)
entry1.configure(font="-family {Poppins} -size 10")
entry1.configure(relief="flat")
entry1.configure(textvariable=user)

#password logo
password= ImageTk.PhotoImage(Image.open("image\password.png").resize((20, 20)))
Label(login_window,image=password).place(relx=0.1, rely=0.5)
Label(login_window,text='Username', font="-family {Poppins} -size 10" ).place(relx=0.1, rely=0.1)

#login entry
entry2=Entry(login_window)
entry2.place(relx=0.25,rely=0.5,relwidth=0.7,relheight=0.08)
entry2.configure(font="-family {Poppins} -size 10")
entry2.configure(relief="flat")
entry2.configure(textvariable=passwd)

# login_buttons
button1 =TkinterCustomButton(master=login_window, corner_radius=20,text="LOGIN")
button1 =TkinterCustomButton(master=login_window, corner_radius=20)
button1.place(relx=0.5, rely=0.8,  anchor=CENTER)

# hide
login_window.withdraw()



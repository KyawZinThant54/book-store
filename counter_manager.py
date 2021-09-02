#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox

#=============DB connection========================
with sqlite3.connect("database.db") as db:
    cur=db.cursor()

#create winodw
root=Tk()
root.title("Counter")
root.iconbitmap("image\logo.ico")



#To get fit on window
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))

#=================variabel=====================
new_ID=StringVar()
new_item=StringVar()
new_quantity=StringVar()
new_price=StringVar()

#=========================Function======================

def search():
    pass

def add_item():
    pass

def remove_item():
    pass

def edit_item():
    pass


#==============Manage Item===========================

Label(root,text="Books",font=('arial', 40, 'bold'),background="red",fg="white").place(relx=0.4,rely=0.07,anchor=W)
product = LabelFrame(root,text="Items",font=('arial', 20, 'bold'))
product.place(relx=0.05,rely=0.15, relwidth=0.45,relheight=0.7)


#=========================ID======================
Label(root,text="ID",font="-family {Poppins} -size 18").place(relx=0.08,rely=0.259)
entry1 =Entry(product)
entry1.place(relx=0.25, rely=0.1, relwidth=0.7, relheight=0.06)
entry1.configure(font="-family {Poppins} -size 15")
entry1.configure(relief="flat")
entry1.configure(textvariable=new_ID)

# Item
Label(product, text='Item',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.3)
entry2 = Entry(product)
entry2.place(relx=0.25, rely=0.3, relwidth=0.7, relheight=0.06)
entry2.configure(font="-family {Poppins} -size 15")
entry2.configure(relief="flat")
entry2.configure(textvariable=new_item)

# quantity
Label(product, text='In Stock',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.5)
entry3 = Entry(product)
entry3.place(relx=0.25, rely=0.5, relwidth=0.7, relheight=0.06)
entry3.configure(font="-family {Poppins} -size 15")
entry3.configure(relief="flat")
entry3.configure(textvariable=new_quantity)

# price
Label(product, text='Price',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.7)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.7, relwidth=0.7, relheight=0.06)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_price)


#====================button============================================
search_btn = TkinterCustomButton(master=product, corner_radius=20,text="Search", command=search)
search_btn.place(relx=0.01, rely=0.9)

add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add Item", command=add_item)
add_btn.place(relx=0.21, rely=0.9)

remove_btn = TkinterCustomButton(master=product, corner_radius=20,text="Remove Item", command=remove_item)
remove_btn.place(relx=0.41, rely=0.9)


edit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Edit Item", command=edit_item)
edit_btn.place(relx=0.61, rely=0.9)


exit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Exit", command=exit)
exit_btn.place(relx=0.81, rely=0.9)




root.mainloop()
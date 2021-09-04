#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox
from tkinter import ttk


#==========DB connection========================
with sqlite3.connect("database.db") as db:
    cur=db.cursor()



#create winodw
root=Tk()
root.title("Manage")
root.iconbitmap("image\logo.ico")

#To get fit on window
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))




#=================variabel=====================
new_ID=StringVar()
new_name=StringVar()
new_password=StringVar()
new_contact_info=StringVar()
new_adress=StringVar()

def search():
    pass

def Add():
    sql_command='''INSERT INTO  workers (ID,Name,password,Contact_info,
                   Adress)VALUES(?,?,?,?,?)'''
    cur.execute(sql_command,(new_ID.get(),new_name.get(),new_password.get(),new_contact_info.get(),new_adress.get()))
    db.commit()
    new_ID.set('')
    new_name.set('')
    new_password.set('')
    new_contact_info.set('')
    new_adress.set('')
    show()

def remove():
    sql_command=''' DELETE FROM workers WHERE id=?'''
    cur.execute(sql_command,[str(new_ID.get())])
    db.commit()
    new_ID.set('')
    new_name.set('')
    new_password.set('')
    new_contact_info.set('')
    new_adress.set('')
    show()

def edit():
    sql_command= ''' UPDATE workers SET Name=?, password=?,
                     contact_info=?,Adress=? WHERE ID=?'''
    cur.execute(sql_command,(new_name.get(),new_password.get(),new_contact_info.get(),new_adress.get(),new_ID.get()))
    db.commit()
    new_ID.set('')
    new_name.set('')
    new_password.set('')
    new_contact_info.set('')
    new_adress.set('')
    show()


def show():
    clear_item()
    sql_command="SELECT * FROM workers ORDER by ID ASC"
    cur.execute(sql_command)
    data=cur.fetchall()
    print(data)
    for num, record in enumerate(data):
        print(record)
        my_tree.insert(parent='', index='end',iid=num,values=(record[0], record[1], record[2], record[3],record[4]))

def clear_item():
    my_tree.delete(*my_tree.get_children())


















#===================Manage people=======================================


Label(root,text="Employee List",font=('arial', 30, 'bold'),background="red",fg="white").place(relx=0.4,rely=0.06,anchor=W)
product = LabelFrame(root,text="Employee",font=('arial', 20, 'bold'))
product.place(relx=0.05,rely=0.15, relwidth=0.45,relheight=0.74)


#ID
Label(root,text="ID",font="-family {Poppins} -size 18").place(relx=0.08,rely=0.24)
entry1 =Entry(product)
entry1.place(relx=0.25, rely=0.05, relwidth=0.7, relheight=0.05)
entry1.configure(font="-family {Poppins} -size 15")
entry1.configure(relief="flat")
entry1.configure(textvariable=new_ID)

#Name
Label(product, text='Name',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.19)
entry2 = Entry(product)
entry2.place(relx=0.25, rely=0.19, relwidth=0.7, relheight=0.05)
entry2.configure(font="-family {Poppins} -size 15")
entry2.configure(relief="flat")
entry2.configure(textvariable=new_name)

# Password
Label(product, text='Password',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.33)
entry3 = Entry(product)
entry3.place(relx=0.25, rely=0.33, relwidth=0.7, relheight=0.05)
entry3.configure(font="-family {Poppins} -size 15")
entry3.configure(relief="flat")
entry3.configure(textvariable=new_password)

# Contace_info
Label(product, text='Contact Info',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.48)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.48, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_contact_info)

#adress
Label(product, text='Adress',font="-family {Poppins} -size 15").place(relx=0.05, rely=0.63)
entry4 = Entry(product)
entry4.place(relx=0.25, rely=0.63, relwidth=0.7, relheight=0.05)
entry4.configure(font="-family {Poppins} -size 15")
entry4.configure(relief="flat")
entry4.configure(textvariable=new_adress)


# #====================button============================================
search_btn = TkinterCustomButton(master=product, corner_radius=20,text="Search", command=search)
search_btn.place(relx=0.01, rely=0.9)

add_btn = TkinterCustomButton(master=product, corner_radius=20,text="Add ", command=Add)
add_btn.place(relx=0.21, rely=0.9)

remove_btn = TkinterCustomButton(master=product, corner_radius=20,text="Remove", command=remove)
remove_btn.place(relx=0.41, rely=0.9)


edit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Edit", command=edit)
edit_btn.place(relx=0.61, rely=0.9)


exit_btn = TkinterCustomButton(master=product, corner_radius=20,text="Exit", command=exit)
exit_btn.place(relx=0.81, rely=0.9)

#==================Table===========================
item_aera=Frame(root)
item_aera.place(relx=0.52,rely=0.12,relwidth=0.5,relheight=0.78)

# scroll=Frame(root)
# scroll.pack(pady=20)





my_tree= ttk.Treeview(item_aera,height=10)
my_tree.place(relx=0, rely=0, relwidth=0.9,relheight=1)
style= ttk.Style()
style.configure("Treeview",font="-family {Poppins} -size 12", rowheight=30)
style.configure("Treeview.Heading", font="-family {Poppins} -size 15")


my_tree['columns'] = ('ID', 'Name', 'Password', 'Contact',"Adress")

my_tree.column('#0', width=0, minwidth=0, stretch=NO)
my_tree.column('ID', width=45)
my_tree.column('Name', width=50)
my_tree.column('Password', width=50)
my_tree.column('Contact', width=50)
my_tree.column('Adress', width=50)


# heading
my_tree.heading('#0', text='')
my_tree.heading('ID', text = 'ID')
my_tree.heading('Name', text = 'Name')
my_tree.heading('Password', text = 'Password')
my_tree.heading('Contact', text = 'Contact')
my_tree.heading('Adress', text = 'Adress')
















show()

root.mainloop()
#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox
from tkinter import ttk

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

#================backgroundImage===============
bg_photo=ImageTk.PhotoImage(Image.open("image\BG.jpg").resize((window_width,window_height)))
#==================place on the window=========================
Label(root,image=bg_photo).place(relx=0,rely=0)



def add_item():
    sql_command='''INSERT INTO  Books (ID,Item,Quantity,
                   price)VALUES(?,?,?,?)'''
    cur.execute(sql_command,(new_ID.get(),new_item.get(),new_quantity.get(),new_price.get()))
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()

def remove_item():
    sql_command=''' DELETE FROM Books WHERE id=?'''
    cur.execute(sql_command,[str(new_ID.get())])
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()


def edit_item():
    sql_command= ''' UPDATE Books SET item=?, quantity=?,
                     price=? WHERE ID=?'''
    cur.execute(sql_command,(new_item.get(),new_quantity.get(),new_price.get(),new_ID.get()))
    db.commit()
    new_ID.set('')
    new_item.set('')
    new_price.set('')
    new_quantity.set('')
    show_items()



def show_items():
    clear_item()
    sql_command="SELECT * FROM Books ORDER by quantity ASC"
    cur.execute(sql_command)
    data=cur.fetchall()
    print(data)
    for num, record in enumerate(data):
        print(record)
        my_tree.insert(parent='', index='end',iid=num,values=(record[0], record[1], record[2], record[3]))



def clear_item():
    my_tree.delete(*my_tree.get_children())
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


#==================Table===========================
item_aera=Frame(root)
item_aera.place(relx=0.52,rely=0.12,relwidth=0.5,relheight=0.78 )

my_tree= ttk.Treeview(item_aera,height=10)
my_tree.place(relx=0, rely=0, relwidth=0.9,relheight=1)
style= ttk.Style()
style.configure("Treeview",font="-family {Poppins} -size 12", rowheight=30)
style.configure("Treeview.Heading", font="-family {Poppins} -size 15")


my_tree['columns'] = ('Item-ID', 'Item', 'Quantity', 'Price')

my_tree.column('#0', width=0, minwidth=0, stretch=NO)
my_tree.column('Item-ID', width=100)
my_tree.column('Item', width=200)
my_tree.column('Quantity', width=50)
my_tree.column('Price', width=50)



# heading
my_tree.heading('#0', text='')
my_tree.heading('Item-ID', text = 'Item ID')
my_tree.heading('Item', text = 'Item')
my_tree.heading('Quantity', text = 'In Stock')
my_tree.heading('Price', text = 'Price')

show_items()
# loop forever
root.mainloop()
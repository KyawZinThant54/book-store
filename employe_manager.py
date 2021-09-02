#import libraries
from tkinter import*
from PIL import  ImageTk,Image
from custom_button import TkinterCustomButton
import sqlite3
import os
from tkinter import messagebox


#create winodw
root=Tk()
root.title("Manage")
root.iconbitmap("image\logo.ico")

#To get fit on window
window_width=root.winfo_screenwidth()
window_height=root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width,window_height))


root.mainloop()
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

root.mainloop()
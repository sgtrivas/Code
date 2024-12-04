from tkinter import *
#import tkinter as tk
from tkinter import ttk
root = Tk()

root.title('ADM')
pic = PhotoImage(file='./logo.png')
smaller_image = pic.subsample(3,3)
label1 = ttk.Label(
    root,
    #text="Android Device Manager v1", 
    image=smaller_image,
    font=('Arial',20),
    compound='bottom',
    borderwidth=1  ,
    #relief='raised'

    # image=pic
)
label1.grid(row=0)
#  BUTTON FUNCTIONS
def ref_but():
    label2= Label(root, text="Hello").grid(row=3, column=0)

def mir_but():
    label3= Label(root, text="Hello").grid(row=3, column=1)

def adb_but():
    label4= Label(root, text="Hello").grid(row=3, column=2)

def scr_but():
    label5= Label(root, text="Hello").grid(row=3, column=3)

def term_but():
    label6= Label(root, text="Hello").grid(row=3, column=4)

#  BUTTONS
refresh_button = Button(root, text="refresh", command=ref_but)
mirror_button = Button(root, text="mirror", command=mir_but)
adb_button = Button(root, text="adb", command=adb_but)
screenShot_button = Button(root, text="screenshot",command=scr_but)
terminal_button = Button(root, text="terminal", command=term_but)

refresh_button.grid(row=2, column=0)
mirror_button.grid(row=2, column=1)
adb_button.grid(row=2, column=2)
screenShot_button.grid(row=2, column=3)
terminal_button.grid(row=2, column=4)

root.geometry('1024x640')
root.resizable(True,True)
root.mainloop()
from tkinter import *
#import tkinter as tk
from tkinter import ttk
root = Tk()
# Class used to build the Table. 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):

                
                self.e = Entry(root, width=20,
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i+1, column=j)
                self.e.insert(END, lst[i][j])
############################################################################
# TABLE INFO VARIABLES
# //THIS FUNCTION WILL COLLECT BASIC DEVICE INFO FOR THE TABLE

#def getInfo():
#    global status, number, imei, other
   
# TEST TABLE INFO
status = 'go'
number = 15163032444
imei = 'asdlkj;ajsgdf'
other = 'stuff'
lst = [('STATUS','NUMBER','IMEI','Other'),
       (status,number,imei,other),
       (status,number,imei,other),
       (status,number,imei,other),
       (status,number,imei,other)
      ]
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

############################################################################
# Window setup 
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
root.geometry('1024x640')
root.resizable(True,True)



# buttons for actions

#Connect


#Browse


#Logs


#Input


#Mirror


#Screenshot


#Install


#Terminal


#ADB Commands


 
# take the data


#t = Table(root)
Table(root)
root.mainloop()


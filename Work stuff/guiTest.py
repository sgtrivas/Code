#  hello world app for Tkinter
import tkinter as tk
root = tk.Tk()
root.title('Banana Interest Survey')
root.geometry('600x480+300+300')
#root.resizable(True,True)
root.resizable(False,False)
label = tk.Label(root, text="Please take survey",
                 font='Arial 16 bold',
                 bg='grey',
                 fg='#FF0')
label.pack()
#Button()
root.mainloop()


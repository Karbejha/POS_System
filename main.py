from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Data Entry')
root.geometry('450x350')

# Title
title = Label(root, text='Data Entry',font='Arial 20 bold')
title.grid(row=0,column=0, pady=5,columnspan=2)

# First name and Last name
FirstName = Label(root, text='First Name')
FirstName.grid(row=1,column=0)



root.mainloop()
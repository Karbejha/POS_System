from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Data Entry')
root.geometry('540x370')

# Title
title = Label(root, text='Data Entry',font='Arial 15 bold')
title.grid(row=0,column=0, pady=10,columnspan=4,sticky='we')

# First name and Last name
FirstName = Label(root, text='First Name')
FirstName.grid(row=1,column=0,padx=10)

FirstName_ = Entry(root, width=20)
FirstName_.grid(row=1,column=1)

LastName = Label(root,text='Last Name')
LastName.grid(row=1 , column=2, padx=10 )

LastName_ = Entry(root , width=20)
LastName_.grid(row=1,column=3,padx=5)

# Birthday
BirthDay = Label(root, text="Bith Date")
BirthDay.grid(row=2,column=0 , ipady=20)

BirthDay_= Entry(root, width=20)
BirthDay_.grid(row=2 , column=1 , columnspan=3 , sticky='we')

# Gender

gender = Label(root , text='Gender')
gender.grid(row=3 , column=0,pady=5 , columnspan=1)

gender_ = ttk.Combobox(root, width=20,values=['Male','Female','Other'])
gender_.grid(row=3 , column=1 , columnspan=4 , sticky='we')


# Country

country = Label (root ,text='Country')
country.grid(row=4,column=0,pady=15)

country_= ttk.Combobox(root, width=20,values=['Turkey','Pakistan','Malaysia','Egypt','Algeria','Morocco','India','Vietnam','Thailand'])
country_.grid(row=4,column=1,pady=5,columnspan=3,sticky='we')

# Explain the problem

problem = Label(root,width=20,text='Explain\n problem')
problem.grid(row=5,column=0)

problem_= Text(width=20,height=5)
problem_.grid(row=5,column=1,columnspan=3,sticky='we',pady=5)

# Buttom

def Clear():
    FirstName_.delete(0,'end')
    LastName_.delete(0, "end")
    BirthDay_.delete(0,'end')
    gender_.delete(0,'end')
    country_.delete(0,'end')
    problem_.delete('1.0','end')

ClearButton = Button(root,text='Clear',width=7,height=2,command=Clear)
ClearButton.grid(row=6,column=2)


def Save():
    Firstname=FirstName_.get()
    Lastname=LastName_.get()
    Birthday=BirthDay_.get()
    Gender=gender_.get()
    Country=country_.get()
    Problem=problem_.get('1.0','end-1c')
    text=FirstName_+','+LastName_+','+BirthDay_+','+gender_+','+country_+','+problem_+'\n'
    with open(r'C:\Users\moham\Desktop\Python Test','a')as file:
        file.write(text)
    Clear()



SaveButton = Button(root,text='Save',width=7,height=2,command=Save)
SaveButton.grid(row=6,column=1)

root.mainloop()
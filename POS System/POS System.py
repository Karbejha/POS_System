from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

class POS:
    def __init__(self,root):
        self.root=root
        self.root.title("Point of Sale")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="cadetblue")

        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        Amount = StringVar()
        choice = StringVar()


        MainFrame = Frame(self.root,bg='cadetblue')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame= Frame(MainFrame,bg='cadetblue',bd=5,width=1348 , height=160,padx=4,pady=4,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame,bg='cadetblue',bd=5,width=800,height=300,padx=4,pady=4,relief=RIDGE)
        DataFrame.pack(side=LEFT)

        DataFrameLeftCover = LabelFrame(DataFrame,bg='cadetblue',bd=5,width=800,height=300,padx=4,pady=4,font=('arial',12,'bold'),text="Point of sale",relief=RIDGE)
        DataFrameLeftCover.pack(side=LEFT)

        ChangeButtonFrame = Frame (DataFrameLeftCover,bd=5,width=300 ,height=460,pady=4,relief=RIDGE)
        ChangeButtonFrame.pack(side=LEFT,padx=4)

        ReciptFrame = Frame(DataFrameLeftCover,bd=5 , width=200 , height=400, pady=5,padx=1, relief=RIDGE)
        ReciptFrame.pack(side=RIGHT,padx=4)

        FoodItemFrame=LabelFrame(DataFrame,bd=5,width=450,height=300,padx=5,pady=2,relief=RIDGE,bg='cadetblue',font=('arial',12,'bold'),text="Items")
        FoodItemFrame.pack(side=RIGHT)

        CallFrame = Frame(ButtonFrame,bd=5,width=432,height=140,relief=RIDGE)
        CallFrame.grid(row = 0 , column=0,padx=5)

        ChangeFrame = Frame(ButtonFrame,bd=5,width=500,height=140 , pady=2,relief=RIDGE)
        ChangeFrame.grid(row=0,column=1,padx=5)

        RemoveFrame=Frame(ButtonFrame,bd=5,width=400,height=140,pady=4,relief=RIDGE)
        RemoveFrame.grid(row=0,column=2,padx=5)

if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()
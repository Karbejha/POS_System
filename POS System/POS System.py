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


        #self.Coffe1 = PhotoImage(file="Coffe1.gif")
        self.Coffe2 = PhotoImage(file="Coffe2.gif")
        #self.Coffe3 = PhotoImage(file="Coffe3.gif")
        #self.Coffe4 = PhotoImage(file="Coffe4.gif")
        #self.Coffe5 = PhotoImage(file="Coffe5.gif")
        #self.Coffe6 = PhotoImage(file="Coffe6.gif")

        #self.Drink1 = PhotoImage(file="Drink1.gif")
        #self.Drink2 = PhotoImage(file="Drink2.gif")
        #self.Drink3 = PhotoImage(file="Drink3.gif")
        #self.Drink4 = PhotoImage(file="Drink4.gif")
        #self.Drink5 = PhotoImage(file="Drink5.gif")
        #self.Drink6 = PhotoImage(file="Drink6.gif")

        #self.Cake1 = PhotoImage(file="Cake1.gif")
        #self.Cake2 = PhotoImage(file="Cake2.gif")
        #self.Cake3 = PhotoImage(file="Cake3.gif")
        #self.Cake4 = PhotoImage(file="Cake4.gif")
        #self.Cake5 = PhotoImage(file="Cake5.gif")
        #self.Cake6 = PhotoImage(file="Cake6.gif")

        #self.IceCake1 = PhotoImage(file="IceCake1.jpeg")
        #self.IceCake2 = PhotoImage(file="IceCake2.jpeg")
        #self.IceCake3 = PhotoImage(file="IceCake3.jpeg")
        #self.IceCake4 = PhotoImage(file="IceCake4.jpeg")
        #self.IceCake5 = PhotoImage(file="IceCake5.jpeg")
        #self.IceCake6 = PhotoImage(file="IceCake6.jpeg")

        #self.FastFood1 = PhotoImage(file="FastFood1.jpeg")
        #self.FastFood2 = PhotoImage(file="FastFood2.jpeg")
        #self.FastFood3 = PhotoImage(file="FastFood3.jpeg")
        #self.FastFood4 = PhotoImage(file="FastFood4.jpeg")
        #self.FastFood5 = PhotoImage(file="FastFood5.jpeg")
        #self.FastFood6 = PhotoImage(file="FastFood6.jpeg")


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

        CallFrame = Frame(ButtonFrame,bd=5,width=405,height=140,relief=RIDGE)
        CallFrame.grid(row = 0 , column=0,padx=5)

        ChangeFrame = Frame(ButtonFrame,bd=5,width=500,height=140 , pady=2,relief=RIDGE)
        ChangeFrame.grid(row=0,column=1,padx=5)

        RemoveFrame=Frame(ButtonFrame,bd=5,width=400,height=140,pady=4,relief=RIDGE)
        RemoveFrame.grid(row=0,column=2,padx=5)

        #============================  Entry And Widget ================================

        self.lblsubTotal = Label(CallFrame,font=('arial',14,'bold'),text="Sub Total",bd=5)
        self.lblsubTotal.grid(row=0,column=0,sticky=W,padx=5)
        self.txtsubTotal = Entry(CallFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2,width=24)
        self.txtsubTotal.grid(row=0, column=1, sticky=W, padx=5)

        self.lblTax = Label(CallFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CallFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2, width=24)
        self.txtTax.grid(row=1, column=1, sticky=W, padx=5)

        self.lblTotal = Label(CallFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(CallFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2, width=24)
        self.txtTotal.grid(row=2, column=1, sticky=W, padx=5)

#============================  Entry And Widget 2 ================================

        self.lblMop = Label(ChangeFrame,font=('arial',14,'bold'),text="Methof of Payment",bd=5)
        self.lblMop.grid(row=0,column=0,sticky=W,padx=5)
        self.cboMop = ttk.Combobox(ChangeFrame, font=('arial', 14, 'bold'), width=36 , state='readonly', textvariable=choice,justify=RIGHT)
        self.cboMop['values']=('','Cash','Visa Card','Master Card')
        self.cboMop.current(0)
        self.cboMop.grid(row=0, column=1)

        self.lblCost = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Cash", bd=5)
        self.lblCost.grid(row=1, column=0, sticky=W, padx=5)
        self.txtCost = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2, width=38)
        self.txtCost.grid(row=1, column=1, sticky=W, padx=5)

        self.lblChange = Label(ChangeFrame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2, column=0, sticky=W, padx=5)
        self.txtChange = Entry(ChangeFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2, width=38)
        self.txtChange.grid(row=2, column=1, sticky=W, padx=5)

#============================  Entry And Widget 2 ================================

        self.btnPay = Button(RemoveFrame , padx=2,font=('arial',15,'bold'),text="Pay",bd=2,width=9,height=1)
        self.btnPay.grid(row=0,column=0,pady=2,padx=4)

        self.btnExit = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Exit", bd=2, width=9, height=1)
        self.btnExit.grid(row=0, column=1, pady=2, padx=4)

        self.btnReset = Button(RemoveFrame, padx=2, font=('arial', 15, 'bold'), text="Reset", bd=2, width=9, height=1)
        self.btnReset.grid(row=1, column=0, pady=2, padx=4)

        self.btnRemoveItem = Button(RemoveFrame, padx=2, font=('arial', 14, 'bold'), text="Remove Item", bd=2, width=9, height=1)
        self.btnRemoveItem.grid(row=1, column=1, pady=2, padx=4)

#============================  Entry And Widget 3 ================================

        self.btnCoffe1 = Button(ChangeButtonFrame , padx=2,image=self.Coffe2,bd=2,width=104,height=104)
        self.btnCoffe1.grid(row=0,column=0,pady=2,padx=4)






if __name__=='__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()
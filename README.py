# calculator-in-gui
from tkinter import *

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnclearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal=Tk()
cal.title("CALCULATOR")
operator=""

text_Input=StringVar()
txtDisplay = Entry(cal ,font="arial 20 bold",textvariable=text_Input,bd=30,insertwidth=4,bg="powder blue",
                 justify='right').grid(columnspan=4)

Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='7',bg="powder blue"
       ,command=lambda:btnclick(7)).grid(row=1,column=0)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='8',bg="powder blue"
       ,command=lambda:btnclick(8)).grid(row=1,column=1)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='9',bg="powder blue"
       ,command=lambda:btnclick(9)).grid(row=1,column=2)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='+',bg="powder blue"
        ,command=lambda:btnclick('+')).grid(row=1,column=3)
#==========================================================================================
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='4',bg="powder blue"
       ,command=lambda:btnclick(4)).grid(row=2,column=0)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='5',bg="powder blue"
       ,command=lambda:btnclick(5)).grid(row=2,column=1)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='6',bg="powder blue"
       ,command=lambda:btnclick(6)).grid(row=2,column=2)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='-',bg="powder blue"
       ,command=lambda:btnclick('-')).grid(row=2,column=3)
#==========================================================================================
Button(cal,padx=16,bd=8,pady=16,fg="black",font='arial 20 bold',text='1',bg="powder blue"
       ,command=lambda:btnclick(1)).grid(row=3,column=0)
Button(cal,padx=16,bd=8,pady=16,fg="black",font='arial 20 bold',text='2',bg="powder blue"
       ,command=lambda:btnclick(2)).grid(row=3,column=1)
Button(cal,padx=16,bd=8,pady=16,fg="black",font='arial 20 bold',text='3',bg="powder blue"
       ,command=lambda:btnclick(3)).grid(row=3,column=2)
Button(cal,padx=16,bd=8,pady=16,fg="black",font='arial 20 bold',text='*',bg="powder blue"
       ,command=lambda:btnclick('*')).grid(row=3,column=3)
#==========================================================================================
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='0',bg="powder blue"
       ,command=lambda:btnclick(0)).grid(row=4,column=0)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='c',bg="powder blue"
       ,command=btnclearDisplay).grid(row=4,column=1)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='=',bg="powder blue"
       ,command=btnEqualInput,).grid(row=4,column=2)
Button(cal,padx=16,pady=16,bd=8,fg="black",font='arial 20 bold',text='/',bg="powder blue"
       ,command=lambda:btnclick('/')).grid(row=4,column=3)






cal.mainloop()

from tkinter import *

#начало программы
calc =Tk()
calc.geometry("270x150")
calc.title("илья канкулятор")
calc.configure(background="blue")


equation =StringVar()

screen = Entry(calc,textvariable=equation)
screen.grid(columnspan=4,ipadx=70, ipady=10)

b1 =Button(calc, text='1',fg='blue', bg='brown',height=1,width=7)
b1.grid(row=2, column=0)

b2 =Button(calc, text='2',fg="blue", bg="brown",height=1,width=7)
b2.grid(row=2, column=1)

b3 =Button( calc,text='3',fg="blue", bg="brown",height=1,width=7)
b3.grid(row=2, column=2)

bc = Button(calc, text='c',fg="blue",bg="brown",width=7)
bc.grid(row=2, column=3)

b4 =Button(calc, text='4',fg="blue",bg="brown",width=7)
b4.grid(row=3 ,column=0)

b5 =Button(calc, text='5',fg="blue",bg="brown",width=7)
b5.grid(row=3, column=1)

b6 =Button(calc, text='6',fg="blue",bg="brown",width=7)
b6.grid(row=3, column=2)

bplus =Button(calc, text='+',fg="blue",bg="brown",width=7)
bplus.grid(row=3, column=3)

b7 =Button(calc, text='7',fg="blue",bg="brown",width=7)
b7.grid(row=4, column=0)

b8 =Button(calc,text='8',fg="blue",bg="brown",width=7)
b8.grid(row=4, column=1)

b9 =Button(calc, text='9',fg="blue",bg="brown",width=7)
b9.grid(row=4, column=2)

bmultiply=Button(calc, text='*',fg="blue",bg="brown",width=7)
bmultiply.grid(row=4, column=3)

b0 =Button(calc, text='0',fg="blue",bg="brown",width=7)
b0.grid(row=5, column=0)

btochka =Button(calc, text='.',fg="blue",bg="brown",width=7)
btochka.grid(row=5, column=1)

bdelenie =Button(calc, text='/',fg="blue",bg="brown",width=7)
bdelenie.grid(row=5, column=2)

bminus =Button(calc, text='-',fg="blue",bg="brown"width=7)
bminus.grid(row=5, column=3)

bequals =Button(calc, text'=',fg="blue",bg"bgrown"width=7)
bequals.grid(row=6, column=0)

expression =""
def press(num):
global expression
expression = expression +str(num)
equation.set(expression)

def equalpress():
try:
global equalpress
total = str (eval (expression))
equation.set(total)

expression = ""
except:
equation.set(" error ")
expression = " "


#конец программы
calc.mainloop()
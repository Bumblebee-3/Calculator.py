from tkinter import *

expression=''

gui=Tk()
gui.title('Simple Calculator')
gui.geometry('230x120')
gui.configure(background='blue')

def press(num):
    global expression
    expression = expression + num
    equation.set(expression)

def clear():
    global expression
    expression=''
    equation.set(expression)

def equal():
    global expression
    try:
        total= eval(expression)
        equation.set(total)
        expression=''
    except:
        equation.set('Undefined')
        expression=''

equation=StringVar()
entery_field=Entry(gui, text=equation)
entery_field.grid(columnspan=40,ipadx=56)
equation.set('enter your expression')

B1=Button(gui,text='1',bg='red', fg='black', height=1, width=7, command=lambda:press('1'))
B1.grid(row=1,column=0)#1

B2=Button(gui,text='2',bg='red', fg='black', height=1, width=7, command=lambda:press('2'))
B2.grid(row=1,column=1)#2

B3=Button(gui,text='3',bg='red', fg='black', height=1, width=7, command=lambda:press('3'))
B3.grid(row=1,column=2)#3

B4=Button(gui,text='4',bg='red', fg='black', height=1, width=7, command=lambda:press('4'))
B4.grid(row=2,column=0)#4

B5=Button(gui,text='5',bg='red', fg='black', height=1, width=7, command=lambda:press('5'))
B5.grid(row=2,column=1)#5

B6=Button(gui,text='6',bg='red', fg='black', height=1, width=7, command=lambda:press('6'))
B6.grid(row=2,column=2)#6

B7=Button(gui,text='7',bg='red', fg='black', height=1, width=7, command=lambda:press('7'))
B7.grid(row=3,column=0)#7

B8=Button(gui,text='8',bg='red', fg='black', height=1, width=7, command=lambda:press('8'))
B8.grid(row=3,column=1)#8

B9=Button(gui,text='9',bg='red', fg='black', height=1, width=7, command=lambda:press('9'))
B9.grid(row=3,column=2)#9

BA=Button(gui,text='+',bg='green', fg='black', height=1, width=7, command=lambda:press('+'))
BA.grid(row=1,column=4)# +

Bs=Button(gui,text='-',bg='green', fg='black', height=1, width=7, command=lambda:press('-'))
Bs.grid(row=2,column=4)#-

Bm=Button(gui,text='×',bg='green', fg='black', height=1, width=7, command=lambda:press('*'))
Bm.grid(row=3,column=4)# x

Bd=Button(gui,text='÷',bg='green', fg='black', height=1, width=7, command=lambda:press('/'))
Bd.grid(row=4,column=4)# ÷

B0=Button(gui,text='0',bg='red', fg='black', height=1, width=7, command=lambda:press('0'))
B0.grid(row=4,column=1)# 0

Be2=Button(gui,text='=',bg='white', fg='black', height=1, width=7, command=lambda:equal())
Be2.grid(row=4,column=2)# =

ce=Button(gui,text='CE',bg='white', fg='black', height=1, width=7, command=lambda:clear())
ce.grid(row=4,column=0)# clear all


gui.mainloop()


#Coded By Bumblebee

﻿from tkinter import *

def valik():
    num=var.get()
    lbox.insert(END,num)

def valik_2():
    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-": lbox.insert(END,val1)
    if val2!="-": lbox.insert(END,val2)
    if val3!="-": lbox.insert(END,val3)

aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")
var=IntVar() #SrtingVar() 
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik) 
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik) 
lbox=Listbox(aken,height=3)
var1=StringVar()
var2=StringVar()
var3=StringVar()
c1=Checkbutton(aken,text="Esimene",variable=var1,onvalue="Esimene",offvalue="-")
c2=Checkbutton(aken,text="Teine",variable=var2,onvalue="Teine",offvalue="--")
c3=Checkbutton(aken,text="Kolmas",variable=var3,onvalue="Kolmas",offvalue="---")

lbox.grid(row=0,column=0)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

c1.grid(row=1,column=1)
c2.grid(row=2,column=1)
c3.grid(row=3,column=1)
aken.mainloop()
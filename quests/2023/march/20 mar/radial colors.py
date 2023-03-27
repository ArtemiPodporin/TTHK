from random import choice
from tkinter import *

colors = ["black", "cyan", "magenta", "red", "blue", "gray", "yellow", "green", "lightblue", "pink", "gold"]
raam=Tk
raam.title("Radius")
tahvel = Canvas(raam, width=600, height=600, background="white")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel.create_oval(x0,y0,x1,y1, fill=choice(colors))
    #sleep(1)
tahvel.grid()

raam.mainloop()
 
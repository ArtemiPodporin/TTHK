import tkinter as tk
from math import *

def show_bahamas():
    canvas.create_rectangle(0, 0, 300, 200, fill="blue")
    canvas.create_polygon([150, 0, 0, 100, 150, 200], fill="yellow")
    canvas.create_polygon([150, 0, 300, 100, 150, 200], fill="yellow")

def show_estonia():
    canvas.create_rectangle(0 ,0 ,300 ,66.6 ,fill ="blue")
    canvas.create_rectangle(0 ,66.6 ,300 ,133.2 ,fill ="black")
    canvas.create_rectangle(0 ,133.2 ,300 ,200 ,fill ="white")

def show_japan():
    canvas.create_oval(100-60/2**0.5+50-10/2**0.5,
                       (100-60/2**0.5+50-10/2**0.5)*3/4,
                       (100+60/2**0.5+50+10/2**0.5),
                       (100+60/2**0.5+50+10/2**0.5)*3/4,
                       fill='red')

root = tk.Tk()
root.title("Flags")

canvas = tk.Canvas(root,width=300,height=200,bg='white')
canvas.pack()

bahamas_button = tk.Button(root,text="Flag of Bahamas",command=show_bahamas)
bahamas_button.pack(side=tk.LEFT)

estonia_button = tk.Button(root,text="Flag of Estonia",command=show_estonia)
estonia_button.pack(side=tk.LEFT)

japan_button = tk.Button(root,text="Flag of Japan",command=show_japan)
japan_button.pack(side=tk.LEFT)

root.mainloop()
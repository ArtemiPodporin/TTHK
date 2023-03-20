import tkinter as tk

def show_bahamas():
    canvas.create_rectangle(0, 0, 300, 200, fill="#7fffd4")
    canvas.create_rectangle(0, 66, 300, 133, fill="yellow")
    canvas.create_polygon([0, 0], [100, 100], [0, 200], fill="black")

def show_estonia():
    canvas.create_rectangle(0, 0, 300, 200/3.0*1.0 , fill="blue")
    canvas.create_rectangle(0 ,200/3.0*1.0 ,300 ,200/3.0*2.0 ,fill="black")
    canvas.create_rectangle(0 ,200/3.0*2.0 ,300 ,200/3.0*3.1 ,fill="white")

root = tk.Tk()
root.title("Lippud")

canvas = tk.Canvas(root,width=300,height=200,bg="cyan")
canvas.pack()

bahamas_button = tk.Button(root,text="Flag of the Bahamas",command=show_bahamas)
bahamas_button.pack()

estonia_button = tk.Button(root,text="Flag of the Estonian state",command=show_estonia)
estonia_button.pack()

root.mainloop()
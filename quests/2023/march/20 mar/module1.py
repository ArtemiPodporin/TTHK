import tkinter as tk

root = tk.Tk()

# create a canvas
C = tk.Canvas(root, width=250, height=200)
C.pack()

# define the coordinates of the rectangle
x0, y0 = 50, 50
x1, y1 = 200, 150

# create a visible rectangle on the canvas
C.create_rectangle(x0, y0, x1, y1, outline='red')

# create the ellipse that fits into the rectangle
id = C.create_oval(x0, y0, x1-1, y1-1, fill='blue')

root.mainloop()

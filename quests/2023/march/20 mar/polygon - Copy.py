import tkinter as tk

# create a new Tkinter window
root = tk.Tk()

# create a new canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# define the vertices of the polygon
vertices = [100, 100, 200, 50, 300, 150, 250, 250, 150, 200]

# create the polygon object on the canvas
polygon_id = canvas.create_polygon(*vertices, outline='black', fill='white', width=2)

# start the Tkinter event loop
root.mainloop()

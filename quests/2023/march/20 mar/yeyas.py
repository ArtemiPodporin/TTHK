import tkinter as tk

def joonista_muster(canvas, x, y, suurus, sügavus):
    if sügavus == 0:
        return
    canvas.create_rectangle(x-suurus/2, y-suurus/2, x+suurus/2, y+suurus/2)
    canvas.create_oval(x-suurus/4, y-suurus/4, x+suurus/4, y+suurus/4)
    joonista_muster(canvas, x+suurus/2, y+suurus/2, suurus/2, sügavus-1)
    joonista_muster(canvas, x-suurus/2, y+suurus/2, suurus/2, sügavus-1)
    joonista_muster(canvas, x+suurus/2, y-suurus/2, suurus/2, sügavus-1)
    joonista_muster(canvas, x-suurus/2, y-suurus/2, suurus/2, sügavus-1)

def joonista():
    canvas.delete("all")
    suurus = int(size_entry.get())
    sügavus = int(depth_entry.get())
    joonista_muster(canvas, 200, 200, suurus, sügavus)

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

size_label = tk.Label(root, text="Suurus:")
size_label.pack()

size_entry = tk.Entry(root)
size_entry.pack()

depth_label = tk.Label(root, text="Sugavus:")
depth_label.pack()

depth_entry = tk.Entry(root)
depth_entry.pack()

draw_button = tk.Button(root, text="Joonista", command=joonista)
draw_button.pack()

root.mainloop()
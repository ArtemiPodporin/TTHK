import tkinter as tk

# looge uus Tkinteri aken
root = tk.Tk()

# luua uus lõuend
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# määratleda hulknurga tipud
vertices = [100, 100, 200, 50, 300, 150, 250, 250, 150, 200]

# luua lõuendile hulknurkobjekt
polygon_id = canvas.create_polygon(*vertices, outline='black', fill='white', width=2)

# start the Tkinter event loop
root.mainloop()

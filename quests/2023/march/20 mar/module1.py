import tkinter as tk

root = tk.Tk()

# luua lõuend
C = tk.Canvas(root, width=250, height=200)
C.pack()

# määrake ristküliku koordinaadid
x0, y0 = 50, 50
x1, y1 = 200, 150

# luua lõuendile nähtav ristkülik
C.create_rectangle(x0, y0, x1, y1, outline='red')

# luua ellips, mis sobib ristkülikuga
id = C.create_oval(x0, y0, x1-1, y1-1, fill='blue')

root.mainloop()

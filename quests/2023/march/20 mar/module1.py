import tkinter as tk

root = tk.Tk()

# luua l�uend
C = tk.Canvas(root, width=250, height=200)
C.pack()

# m��rake ristk�liku koordinaadid
x0, y0 = 50, 50
x1, y1 = 200, 150

# luua l�uendile n�htav ristk�lik
C.create_rectangle(x0, y0, x1, y1, outline='red')

# luua ellips, mis sobib ristk�likuga
id = C.create_oval(x0, y0, x1-1, y1-1, fill='blue')

root.mainloop()

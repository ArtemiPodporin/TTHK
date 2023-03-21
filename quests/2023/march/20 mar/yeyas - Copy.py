import tkinter as tk

def draw_chess_board(canvas, length, depth):
    if depth == 0:
        return
    for i in range(8):
        x1 = i * length
        y1 = 0
        x2 = (i+1) * length
        y2 = length
        if i % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill='black')
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill='white')
        for j in range(2):
            cx = x1 + (j+1) * length / 2
            cy = (2*j+1) * length / 4
            canvas.create_oval(cx-length/4, cy-length/4, cx+length/4, cy+length/4, fill='red')
    canvas.update()
    draw_chess_board(canvas, length/2, depth-1)

def draw_pattern():
    length = int(length_entry.get())
    depth = int(depth_entry.get())
    canvas.delete('all')
    draw_chess_board(canvas, length, depth)

root = tk.Tk()
root.title('Rekursiivne malelaua muster')

length_label = tk.Label(root, text='Ruudu pikkus:')
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

depth_label = tk.Label(root, text='Sügavus:')
depth_label.grid(row=1, column=0, padx=5, pady=5)
depth_entry = tk.Entry(root)
depth_entry.grid(row=1, column=1, padx=5, pady=5)

draw_button = tk.Button(root, text='Joonista muster', command=draw_pattern)
draw_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
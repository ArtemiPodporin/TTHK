import tkinter as tk


def draw_square(length, depth, x, y):
    if depth == 0:
        return

    canvas.create_rectangle(x, y, x+length, y+length)

    new_length = length / 3
    new_depth = depth - 1

    draw_square(new_length, new_depth, x, y)
    draw_square(new_length, new_depth, x+new_length, y)
    draw_square(new_length, new_depth, x+2*new_length, y)

    draw_square(new_length, new_depth, x, y+new_length)
    draw_square(new_length, new_depth, x+2*new_length, y+new_length)

    draw_square(new_length, new_depth, x, y+2*new_length)
    draw_square(new_length, new_depth, x+new_length, y+2*new_length)
    draw_square(new_length, new_depth, x+2*new_length, y+2*new_length)


def draw():
    canvas.delete(tk.ALL)

    length = int(length_var.get())
    depth = int(depth_var.get())

    draw_square(length, depth, 10, 10)


root = tk.Tk()
root.title("Recursive Square")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

length_var = tk.StringVar(value="300")
depth_var = tk.StringVar(value="4")

length_label = tk.Label(root, text="pikkus:")
length_entry = tk.Entry(root, textvariable=length_var)

depth_label = tk.Label(root, text="sugavus:")
depth_1_button = tk.Radiobutton(root, text="1", variable=depth_var, value="1")
depth_2_button = tk.Radiobutton(root, text="2", variable=depth_var, value="2")
depth_3_button = tk.Radiobutton(root, text="3", variable=depth_var, value="3")
depth_4_button = tk.Radiobutton(root, text="4", variable=depth_var, value="4")
depth_5_button = tk.Radiobutton(root, text="5", variable=depth_var, value="5")

draw_button = tk.Button(root, text="joonista", command=draw)

length_label.pack()
length_entry.pack()

depth_label.pack()
depth_1_button.pack()
depth_2_button.pack()
depth_3_button.pack()
depth_4_button.pack()
depth_5_button.pack()

draw_button.pack()

root.mainloop()

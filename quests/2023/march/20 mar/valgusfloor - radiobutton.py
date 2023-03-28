import tkinter as tk

class Valgusfoor:
    def __init__(self, master):
        self.master = master
        self.master.title("Valgusfoor")

        # Создайте радиокнопки для каждого источника света
        self.radio_var = tk.StringVar()
        self.radio_var.set('red')
        self.red_rb = tk.Radiobutton(master, text="Punane", value="red", variable=self.radio_var, command=self.change_color)
        self.yellow_rb = tk.Radiobutton(master, text="Kollane", value="yellow", variable=self.radio_var, command=self.change_color)
        self.green_rb = tk.Radiobutton(master, text="Roheline", value="green", variable=self.radio_var, command=self.change_color)

        # Добавьте радиокнопки в окно
        self.red_rb.pack(side="left")
        self.yellow_rb.pack(side="left")
        self.green_rb.pack(side="left")

        # Создайте холст для света
        self.canvas = tk.Canvas(master, width=100, height=250, bg="white")
        self.canvas.pack()

        # Сначала нарисуйте свет
        self.change_color()

    def change_color(self):
        color = self.radio_var.get()
        self.canvas.delete("all")
        if color == "punane":
            self.canvas.create_oval(25, 25, 75, 75, fill="red")
            self.canvas.create_oval(25, 100, 75, 150, fill="gray")
            self.canvas.create_oval(25, 175, 75, 225, fill="gray")
        elif color == "kollane":
            self.canvas.create_oval(25, 25, 75, 75, fill="gray")
            self.canvas.create_oval(25, 100, 75, 150, fill="yellow")
            self.canvas.create_oval(25, 175, 75, 225, fill="gray")
        elif color == "roheline":
            self.canvas.create_oval(25, 25, 75, 75, fill="gray")
            self.canvas.create_oval(25, 100, 75, 150, fill="gray")
            self.canvas.create_oval(25, 175, 75, 225, fill="green")

root = tk.Tk()
traffic_light = Valgusfoor(root)
root.mainloop()

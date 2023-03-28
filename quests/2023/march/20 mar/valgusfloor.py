import tkinter as tk

class Valgusfoor:
    def __init__(self, master):
        self.master = master
        self.master.title("Valgusfoor")

        # luua valgusfoori jaoks lõuend
        self.canvas = tk.Canvas(master, width=100, height=300)
        self.canvas.pack()

        # looge tulede jaoks kolm ringi
        self.red_light = self.canvas.create_oval(25, 25, 75, 75, fill="gray")
        self.yellow_light = self.canvas.create_oval(25, 100, 75, 150, fill="gray")
        self.green_light = self.canvas.create_oval(25, 175, 75, 225, fill="gray")

        # luua nupud, mille abil kasutaja saab valgust vahetada
        self.red_button = tk.Button(master, text="Punane", command=self.switch_red)
        self.red_button.pack(side="left", padx=10)

        self.yellow_button = tk.Button(master, text="Kollane", command=self.switch_yellow)
        self.yellow_button.pack(side="left", padx=10)

        self.green_button = tk.Button(master, text="Roheline", command=self.switch_green)
        self.green_button.pack(side="left", padx=10)

    def switch_red(self):
        # lülitage kõik tuled välja, seejärel lülitage punane tuli sisse
        self.canvas.itemconfig(self.red_light, fill="red")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="gray")

    def switch_yellow(self):
        # lülitage kõik tuled välja, seejärel lülitage kollane tuli sisse
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="yellow")
        self.canvas.itemconfig(self.green_light, fill="gray")

    def switch_green(self):
        # lülitage kõik tuled välja, seejärel lülitage sisse roheline tuli
        self.canvas.itemconfig(self.red_light, fill="gray")
        self.canvas.itemconfig(self.yellow_light, fill="gray")
        self.canvas.itemconfig(self.green_light, fill="green")

root = tk.Tk()

tl = Valgusfoor(root)

root.mainloop()
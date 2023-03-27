import tkinter as tk

class FlagApp:
    def __init__(self, master):
        self.master = master
        self.master.title("lippud")
        self.create_widgets()

    def create_widgets(self):
        self.selected_flag = tk.StringVar()

        self.bahamas_rb = tk.Radiobutton(self.master, text="Bahamas", value="bahamas", variable=self.selected_flag, command=self.draw_flag)
        self.bahamas_rb.pack()

        self.estonia_rb = tk.Radiobutton(self.master, text="Estonia", value="estonia", variable=self.selected_flag, command=self.draw_flag)
        self.estonia_rb.pack()

        self.japan_rb = tk.Radiobutton(self.master, text="Japan", value="japan", variable=self.selected_flag, command=self.draw_flag)
        self.japan_rb.pack()

        self.canvas = tk.Canvas(self.master, width=300, height=200)
        self.canvas.pack()

    def draw_flag(self):
        self.canvas.delete("all")

        flag = self.selected_flag.get()

        if flag == "bahamas":
            self.canvas.create_rectangle(0, 0, 300, 200, fill="#0B4F8C")
            self.canvas.create_polygon(150, 100, 225, 50, 225, 150, fill="#FFC72C")
            self.canvas.create_polygon(150, 100, 75, 50, 75, 150, fill="#FFC72C")
        elif flag == "estonia":
            self.canvas.create_rectangle(0, 0, 300, 200, fill="#0072C6")
            self.canvas.create_rectangle(0, 0, 100, 200, fill="#FFFFFF")
            self.canvas.create_rectangle(200, 0, 300, 200, fill="#FFFFFF")
            self.canvas.create_rectangle(95, 0, 105, 200, fill="#000000")
            self.canvas.create_rectangle(195, 0, 205, 200, fill="#000000")
        elif flag == "japan":
            self.canvas.create_oval(50, 50, 250, 150, fill="#FFFFFF")
            self.canvas.create_oval(100, 50, 200, 150, fill="#C8102E")
        else:
            print("vale")

root = tk.Tk()
app = FlagApp(root)
root.mainloop()

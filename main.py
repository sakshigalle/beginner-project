import tkinter as tk
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter App Example")
        self.init_ui()

    def init_ui(self):
        self.label = tk.Label(self, text="Enter your name:")
        self.label.pack()

        self.textbox = tk.Entry(self)
        self.textbox.pack()

        self.button = tk.Button(self, text="Say Hello", command=self.say_hello)
        self.button.pack()

        self.result = tk.Label(self, text="")
        self.result.pack()

    def say_hello(self):
        name = self.textbox.get()
        self.result.config(text=f"Hello, {name}!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
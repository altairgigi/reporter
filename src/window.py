import customtkinter as ctk
from src.components.frame import Frame

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reporter")
        self.geometry("600x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark")

        self.frame = Frame(master=self)
        self.frame.grid(row=0, column=0, sticky="nsew")
import customtkinter as ctk
class Heading(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.month = ctk.CTkEntry(self, placeholder_text="Month")
        self.month.pack(side="left", pady=20, padx=20, fill="x")

        self.year = ctk.CTkEntry(self, placeholder_text="Year")
        self.year.pack(pady=20, padx=20, fill="x")

    def get_data():
        pass
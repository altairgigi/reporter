import customtkinter as ctk

class Heading(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.month = ctk.CTkEntry(self, placeholder_text="Month")
        self.month.pack(side="left", fill="x")

        self.year = ctk.CTkEntry(self, placeholder_text="Year")
        self.year.pack(side="right", fill="x")

    def get_data(self):
        return {
            "month": self.month.get(),
            "year": self.year.get()
        }
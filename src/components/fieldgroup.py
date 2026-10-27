import customtkinter as ctk
class FieldGroup(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.pack(anchor="w")

        self.valid_votes = ctk.CTkEntry(self, placeholder_text="Valid votes")
        self.valid_votes.pack(side="left", pady=10, padx=10, fill="x")

        self.total_votes = ctk.CTkEntry(self, placeholder_text="Total votes")
        self.total_votes.pack(pady=10, padx=10, fill="x")

    def get_data():
        pass
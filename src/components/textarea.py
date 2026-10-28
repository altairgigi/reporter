import customtkinter as ctk

class TextArea(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)

        self.text_label = ctk.CTkLabel(self, text=text)
        self.text_label.pack(anchor="w")
        
        self.text_box = ctk.CTkTextbox(self, width=500, height=100)
        self.text_box.pack()

    def get_data(self):
        return {"text": self.text_box.get("1.0", "end")}
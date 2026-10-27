import customtkinter as ctk
class TextArea(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)

        self.text_label = ctk.CTkLabel(self, text=text)
        self.text_label.pack(anchor="w")
        
        self.text_textbox = ctk.CTkTextbox(self, width=500, height=100)
        self.text_textbox.pack()

    def get_data():
        pass
import customtkinter as ctk

class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.month = ctk.CTkEntry(self, placeholder_text="month")
        self.month.pack(pady=20, padx=20, fill="x")

        self.year = ctk.CTkEntry(self, placeholder_text="year")
        self.year.pack(pady=20, padx=20, fill="x")

        self.updatelabel = ctk.CTkLabel(self, text="Regional Updates")
        self.updatelabel.pack(pady=20)
        self.updatetextbox = ctk.CTkTextbox(self, width=500, height=100)
        self.updatetextbox.pack(pady=20)

        self.moderationlabel = ctk.CTkLabel(self, text="Moderation Updates")
        self.moderationlabel.pack(pady=20)
        self.moderationtextbox = ctk.CTkTextbox(self, width=500, height=100)
        self.moderationtextbox.pack(pady=20)

        self.cabinetlabel = ctk.CTkLabel(self, text="Moderation Updates")
        self.cabinetlabel.pack(pady=20)
        self.cabinettextbox = ctk.CTkTextbox(self, width=500, height=100)
        self.cabinettextbox.pack(pady=20)

        self.commissionlabel = ctk.CTkLabel(self, text="Moderation Updates")
        self.commissionlabel.pack(pady=20)
        self.commissiontextbox = ctk.CTkTextbox(self, width=500, height=100)
        self.commissiontextbox.pack(pady=20)
        
        self.savebutton = ctk.CTkButton(self, text="Save", command=self.button_callbck)
        self.savebutton.pack(padx=20, pady=20)

        self.copybutton = ctk.CTkButton(self, text="Copy to clipboard", command=self.button_callbck)
        self.copybutton.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reporter")
        self.geometry("600x800")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        ctk.set_appearance_mode("dark")

        self.frame = ScrollableFrame(master=self)
        self.frame.grid(row=0, column=0, sticky="nsew")

app = Interface()
app.mainloop()
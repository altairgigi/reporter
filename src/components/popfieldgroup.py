import customtkinter as ctk

class PopFieldGroup(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.pack(anchor="w")

        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(pady=10)

        self.entry1A = ctk.CTkEntry(self.entry_frame, placeholder_text="Past Population")
        self.entry1A.grid(row=0, column=0)
        self.entry1B = ctk.CTkEntry(self.entry_frame, placeholder_text="Current Population")
        self.entry1B.grid(row=0, column=1)
        self.entry2A = ctk.CTkEntry(self.entry_frame, placeholder_text="Past WA Population")
        self.entry2A.grid(row=1, column=0)
        self.entry2B = ctk.CTkEntry(self.entry_frame, placeholder_text="Current WA Population")
        self.entry2B.grid(row=1, column=1)
        self.entry3A = ctk.CTkEntry(self.entry_frame, placeholder_text="Past Delegate Endorsement")
        self.entry3A.grid(row=2, column=0)
        self.entry3B = ctk.CTkEntry(self.entry_frame, placeholder_text="Current Delegate Endorsement")
        self.entry3B.grid(row=2, column=1)
        self.entry4A = ctk.CTkEntry(self.entry_frame, placeholder_text="Past Yeld Rate")
        self.entry4A.grid(row=3, column=0)
        self.entry4B = ctk.CTkEntry(self.entry_frame, placeholder_text="Current Yeld Rate")
        self.entry4B.grid(row=3, column=1)

        self.population_entries = [
            [self.entry1A, self.entry1B],
            [self.entry2A, self.entry2B],
            [self.entry3A, self.entry3B],
            [self.entry4A, self.entry4B],
        ]

    def get_data(self):
        population_data = [
            {"entry": entry_a.get(), "data": entry_b.get()}
            for entry_a, entry_b in self.population_entries
        ]

        return {"population": population_data}
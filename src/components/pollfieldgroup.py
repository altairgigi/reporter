import customtkinter as ctk

class PollFieldGroup(ctk.CTkFrame):
    def __init__(self, master, text):
        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=text)
        self.label.pack(anchor="w")

        self.votes_frame = ctk.CTkFrame(self)
        self.votes_frame.pack()

        self.valid_votes = ctk.CTkEntry(self.votes_frame, placeholder_text="Valid votes")
        self.valid_votes.grid(row=0, column=0)

        self.total_votes = ctk.CTkEntry(self.votes_frame, placeholder_text="Total votes")
        self.total_votes.grid(row=0, column=1)

        self.entry_frame = ctk.CTkFrame(self)
        self.entry_frame.pack(pady=10)

        self.entry1A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry1A.grid(row=0, column=0)
        self.entry1B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry1B.grid(row=0, column=1)
        self.entry2A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry2A.grid(row=1, column=0)
        self.entry2B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry2B.grid(row=1, column=1)
        self.entry3A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry3A.grid(row=2, column=0)
        self.entry3B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry3B.grid(row=2, column=1)
        self.entry4A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry4A.grid(row=3, column=0)
        self.entry4B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry4B.grid(row=3, column=1)
        self.entry5A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry5A.grid(row=4, column=0)
        self.entry5B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry5B.grid(row=4, column=1)
        self.entry6A = ctk.CTkEntry(self.entry_frame, placeholder_text="Officer")
        self.entry6A.grid(row=5, column=0)
        self.entry6B = ctk.CTkEntry(self.entry_frame, placeholder_text="Vote")
        self.entry6B.grid(row=5, column=1)

        self.officer_entries = [
            [self.entry1A, self.entry1B],
            [self.entry2A, self.entry2B],
            [self.entry3A, self.entry3B],
            [self.entry4A, self.entry4B],
            [self.entry5A, self.entry5B],
            [self.entry6A, self.entry6B]
        ]

        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.pack()

        self.image_url = ctk.CTkEntry(self.image_frame, placeholder_text="Image url")
        self.image_url.pack()

    def get_data(self):
        vote_data = [
            self.valid_votes.get(),
            self.total_votes.get()
        ]

        officers_data = [
            {"officer": entry_a.get(), "vote": entry_b.get()}
            for entry_a, entry_b in self.officer_entries
        ]

        image_url = self.image_url.get()

        return {
            "vote": vote_data,
            "officers": officers_data,
            "image": image_url
        }
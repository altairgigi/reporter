import customtkinter as ctk
from src.components.heading import Heading
from src.components.textarea import TextArea
from src.components.table import Table
from src.components.fieldgroup import FieldGroup
import src.config as config

class Frame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.heading = Heading(self)
        self.heading.pack(pady=10)

        self.regiona_updates = TextArea(self, "Regional Updates")
        self.regiona_updates.pack(pady=10)

        self.moderation_updates = TextArea(self, "Moderation Updates")
        self.moderation_updates.pack(pady=10)

        self.cabinet_updates = TextArea(self, "Cabinet Updates")
        self.cabinet_updates.pack(pady=10)

        self.commission_updates = TextArea(self, "Commission Updates")
        self.commission_updates.pack(pady=10)

        self.wa_table = Table(self, True, config.A_TABLE_COLUMNS)
        self.wa_table.pack(pady=10)

        self.sc_table = Table(self, True, config.A_TABLE_COLUMNS)
        self.sc_table.pack(pady=10)

        self.authorship_table = Table(self, False, config.B_TABLE_COLUMNS)
        self.authorship_table.pack(pady=10)
        
        self.poll_results = FieldGroup(self, "Poll Results")
        self.poll_results.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.button_save = ctk.CTkButton(self.button_frame, text="Save", command=self.handle_save)
        self.button_save.pack(side="left", padx=20, pady=20)

        self.button_copy = ctk.CTkButton(self.button_frame, text="Copy to clipboard", command=self.handle_copy)
        self.button_copy.pack(padx=20, pady=20)

    def handle_save(self):
        print("save clicked")

    def handle_copy(self):
        print("copy clicked")
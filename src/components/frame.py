import customtkinter as ctk
from src.components.table import Table
import src.config as config

class Frame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.title_frame =ctk.CTkFrame(self)
        self.title_frame.pack()
        self.month = ctk.CTkEntry(self.title_frame, placeholder_text="Month")
        self.month.pack(side="left", pady=20, padx=20, fill="x")
        self.year = ctk.CTkEntry(self.title_frame, placeholder_text="Year")
        self.year.pack(pady=20, padx=20, fill="x")

        self.update_frame =ctk.CTkFrame(self)
        self.update_frame.pack(pady=10)
        self.update_label = ctk.CTkLabel(self.update_frame, text="Regional Updates")
        self.update_label.pack(anchor="w")
        self.update_textbox = ctk.CTkTextbox(self.update_frame, width=500, height=100)
        self.update_textbox.pack()

        self.moderation_frame =ctk.CTkFrame(self)
        self.moderation_frame.pack(pady=10)
        self.moderation_label = ctk.CTkLabel(self.moderation_frame, text="Moderation Updates")
        self.moderation_label.pack(anchor="w")
        self.moderation_textbox = ctk.CTkTextbox(self.moderation_frame, width=500, height=100)
        self.moderation_textbox.pack()

        self.cabinet_frame =ctk.CTkFrame(self)
        self.cabinet_frame.pack(pady=10)
        self.cabinet_label = ctk.CTkLabel(self.cabinet_frame, text="Moderation Updates")
        self.cabinet_label.pack(anchor="w")
        self.cabinet_textbox = ctk.CTkTextbox(self.cabinet_frame, width=500, height=100)
        self.cabinet_textbox.pack()

        self.commission_frame =ctk.CTkFrame(self)
        self.commission_frame.pack(pady=10)
        self.commission_label = ctk.CTkLabel(self.commission_frame, text="Moderation Updates")
        self.commission_label.pack(anchor="w")
        self.commission_textbox = ctk.CTkTextbox(self.commission_frame, width=500, height=100)
        self.commission_textbox.pack()

        self.wa_table_frame =ctk.CTkFrame(self)
        self.wa_table_frame.pack(pady=10)
        self.wa_table = Table(self.wa_table_frame, config.A_TABLE_COLUMNS)
        self.wa_table.pack()

        self.sc_table_frame =ctk.CTkFrame(self)
        self.sc_table_frame.pack(pady=10)
        self.sc_table = Table(self.sc_table_frame, config.A_TABLE_COLUMNS)
        self.sc_table.pack()

        self.authorship_table_frame =ctk.CTkFrame(self)
        self.authorship_table_frame.pack(pady=10)
        self.authorship_table = Table(self.authorship_table_frame, config.B_TABLE_COLUMNS)
        self.authorship_table.pack()

        self.button_frame =ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)
        self.save_button = ctk.CTkButton(self.button_frame, text="Save", command=self.handle_save)
        self.save_button.pack(side="left", padx=20, pady=20)
        self.copy_button = ctk.CTkButton(self.button_frame, text="Copy to clipboard", command=self.handle_copy)
        self.copy_button.pack(padx=20, pady=20)

    def handle_save(self):
        print("save clicked")

    def handle_copy(self):
        print("copy clicked")
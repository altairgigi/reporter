import customtkinter as ctk
from src.components.heading import Heading
from src.components.textarea import TextArea
from src.components.table import Table
from src.components.popfieldgroup import PopFieldGroup
from src.components.pollfieldgroup import PollFieldGroup
from src.generator import Generator
import src.config as config

class Frame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.heading = Heading(self)
        self.heading.pack(pady=10)

        self.population_data = PopFieldGroup(self, "Population Data")
        self.population_data.pack(pady=10)

        self.regional_updates = TextArea(self, "Regional Updates")
        self.regional_updates.pack(pady=10)

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
        
        self.poll_results = PollFieldGroup(self, "Poll Results")
        self.poll_results.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        self.button_save = ctk.CTkButton(self.button_frame, fg_color="green", hover_color="darkgreen", text="Save", command=self.handle_save)
        self.button_save.pack(side="left", padx=20, pady=20)

        self.button_copy = ctk.CTkButton(self.button_frame, fg_color="yellow", hover_color="gold", text_color="black", text="Copy to clipboard", command=self.handle_copy)
        self.button_copy.pack(padx=20, pady=20)

    def generate(self):
        data = {
            "heading": self.heading.get_data(),
            "population": self.population_data.get_data(),
            "regional": self.regional_updates.get_data(),
            "moderation": self.moderation_updates.get_data(),
            "cabinet": self.cabinet_updates.get_data(),
            "commission": self.commission_updates.get_data(),
            "wa": self.wa_table.get_data(),
            "sc": self.sc_table.get_data(),
            "authorships": self.authorship_table.get_data(),
            "poll": self.poll_results.get_data()
        }

        return Generator.format(data)
    
    def handle_save(self):
        bbcode = self.generate()
        print("Save successful")

    def handle_copy(self):
        bbcode = self.generate()
        print("Copy successful")
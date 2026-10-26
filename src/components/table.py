import customtkinter as ctk
import src.config as config

class Table(ctk.CTkFrame):
    def __init__(self, master, columns):
        super().__init__(master)
        self.columns = columns

        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.grid()

        self.headers = config.WA_TABLE_HEADERS

        if self.columns <= len(self.headers):
            for col in range(columns):
                label = ctk.CTkLabel(self.table_frame, text=self.headers[col])
                label.grid(row=0, column=col)

            for col in range(columns):
                field = ctk.CTkEntry(self.table_frame)
                field.grid(row=1, column=col)
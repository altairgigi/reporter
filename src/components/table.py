import customtkinter as ctk
import src.config as config

class Table(ctk.CTkFrame):
    def __init__(self, master, is_bool, columns):
        super().__init__(master)
        self.is_bool = is_bool
        self.columns = columns
        self.table = []

        self.controls_frame = ctk.CTkFrame(self)
        self.controls_frame.pack(side="right", anchor="n")

        self.active = ctk.CTkCheckBox(self.controls_frame, text="Active")
        self.active.pack()
        self.active.select()

        self.button_add = ctk.CTkButton(self.controls_frame, height=10, width=10, text="Add row", command=self.add_row)
        self.button_add.pack()

        self.button_remove = ctk.CTkButton(self.controls_frame, height=10, width=20, text="Remove Row", command=self.remove_row)
        self.button_remove.pack()

        self.rows_frame = ctk.CTkFrame(self)
        self.rows_frame.pack()

        self.headers = config.WA_TABLE_HEADERS

        if self.columns <= len(self.headers):
            for col in range(columns):
                label = ctk.CTkLabel(self.rows_frame, text=self.headers[col])
                label.grid(row=0, column=col)

            self.add_row()

    def add_row(self):
        index = len(self.table) + 1
        row = []

        for col in range(self.columns):
            if col == self.columns - 1 and self.is_bool:
                option = ctk.CTkOptionMenu(self.rows_frame, values=["FOR", "AGAINST"])
                option.grid(row=index, column=col)
                row.append(option)
            else:
                entry = ctk.CTkEntry(self.rows_frame)
                entry.grid(row=index, column=col)
                row.append(entry)

        self.table.append(row)

    def remove_row(self):
        index = len(self.table) - 1

        if index >= 0:
            for col in range(self.columns):
                self.table[index][col].destroy()

        self.table.pop(index)

    def get_data(self):
        pass
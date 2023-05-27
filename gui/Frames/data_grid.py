import tkinter as tk
from gui.gui_const import *



class DataGrid(tk.Frame):
    def __init__(self, master, bg, items_number = 4) -> None:
        super().__init__(master, bg=bg)

        self.grid_columnconfigure((1, 2), weight=2)
        self.grid_columnconfigure(0, weight=2)

        for i in range(items_number):
            self.lbl_color_code = tk.Label(self,
                                           text=f'Code {i + 1}',
                                           fg=FG_WHITE,
                                            background=BG_GREY_COLOR,
                                           font=('Verdana', 12))
            self.lbl_color_code.grid(row=i, column=0,
                                     padx=10, pady=10, sticky='ew')
            
            self.lbl_crypto_name = tk.Label(self,
                                           text=f'Crypto {i + 1}',
                                           fg=FG_WHITE,
                                            background=BG_GREY_COLOR,
                                           font=('Verdana', 12))
            self.lbl_crypto_name.grid(row=i, column=1,
                                     padx=10, pady=10, sticky='ew')
            
            self.lbl_crypto_trend = tk.Label(self,
                                           text=f'Trend {i + 1}',
                                           fg=FG_WHITE,
                                            background=BG_GREY_COLOR,
                                           font=('Verdana', 12))
            self.lbl_crypto_trend.grid(row=i, column=2,
                                     padx=10, pady=10, sticky='ew')
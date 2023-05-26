import tkinter as tk
from gui.gui_const import BG_COLOR


class AccountBalance(tk.Frame):
    def __init__(self, master, bg) -> None:
        super().__init__(master, bg=bg)

        self.grid_columnconfigure(0, weight=1)

        self.lbl_balance_title = tk.Label(self,
                                          text='Balance',
                                          background=BG_COLOR,
                                          font=('Verdana', 18))
        self.lbl_balance_title.grid(row=0, column=0,
                                    padx=10, pady=10, sticky='ew')

        self.lbl_balance_amount = tk.Label(self,
                                          text='$ 20.916,92 $',
                                          background=BG_COLOR,
                                          font=('Verdana', 24))
        self.lbl_balance_amount.grid(row=1, column=0,
                                    padx=10, pady=10, sticky='ew')
        
        self.lbl_balance_trend = tk.Label(self,
                                          text='+ 25,93 %',
                                          background=BG_COLOR,
                                          font=('Verdana', 16))
        self.lbl_balance_trend.grid(row=2, column=0,
                                    padx=10, pady=10, sticky='ew')    
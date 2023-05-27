import tkinter as tk

from gui.gui_const import *
from gui.Frames.account_balance import AccountBalance
from gui.Frames.dashboard import Dashboard

class MainWindow(tk.Tk):
    def __init__ (self) -> None:
        super().__init__()

        self.title('Crypto market APP')
        self.geometry('500x600')

        self.frm_account_balance = AccountBalance(self,
                                                  bg=BG_AM_COLOR)
        self.frm_account_balance.pack(padx=0, pady=(0, 10), fill='x')
        
        self.frm_dashboard = Dashboard(self,
                                     bg=BG_GREY_COLOR)
        self.frm_dashboard.pack(padx=10, pady=(0, 10), fill='x')
        
        
        
        
        
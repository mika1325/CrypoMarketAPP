import tkinter as tk

from gui.gui_const import BG_COLOR
from gui.Frames.account_balance import AccountBalance


class MainWindow(tk.Tk):
    def __init__ (self) -> None:
        super().__init__()

        self.title('Crypto market APP')
        self.geometry('500x600')

        self.frm_account_balance = AccountBalance(self,
                                                  bg=BG_COLOR)
        self.frm_account_balance.pack(padx=0, pady=(0, 25), fill='x')
        
        self.frm_dashboar = tk.Frame(self,
                                     bg=BG_COLOR)
        
        
        
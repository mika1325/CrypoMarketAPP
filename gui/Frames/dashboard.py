import tkinter as tk
from gui.gui_const import *
from gui.Frames.data_grid import DataGrid



class Dashboard(tk.Frame):
    def __init__(self, master, bg) -> None:
        super().__init__(master, bg=bg)

        self.grid_columnconfigure(0, weight=1)

        self.lbl_pie_chart = tk.Label(self,
                                      text='Pie Chart',
                                      fg=FG_WHITE,
                                      background=BG_GREY_COLOR,
                                      font=('Verdana', 18))
        self.lbl_pie_chart.grid(row=0, column=0,
                                padx=10, pady=10, sticky='nesw')
    
        self.frm_data_grid = DataGrid(self, bg=BG_GREY_COLOR)
        self.frm_data_grid.grid(row=0, column=1,
                                padx=10, pady=10, sticky='nesw')
       
        
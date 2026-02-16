import json, tkinter
from tkinter import Label, Button, messagebox, Text, font

class MainForm(tkinter.Tk):

    def __init__(self):
        super().__init__()

        self.title("Check PerCom")
        self.geometry("500x550")
        self.resizable(False,False)
        self.font = font.Font(size=20)
        self.option_add("*Font",self.font)

        # --- --- TextBox --- ---
        self.textbox = Text(self,width=32,height=15)
        self.textbox.place(x=10,y=10)
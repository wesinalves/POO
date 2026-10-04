"""
Classe personalizada para nota fiscal
"""
from tkinter import *

class Nota(Text):
    def __init__(self, parent=None):
        super().__init__(
            parent,
            height=17, 
            width=47, 
            padx=5, 
            pady=5, 
            font=("Arial", 30, "normal"),
            bd=0,
            highlightthickness=0,
        )
        self.insert("1.0", "Casas Brasília - Ponto de Venda")
        self.pack(expand=YES, fill=BOTH)


if __name__ == "__main__":
    Nota("Nota Fiscal Eletrônica - Casas Brasília").mainloop()
"""
Classe campo consiste dos componentes label e entry agrupados
"""
from tkinter import *
import configs as cf

class Campo(Frame):
    def __init__(self, chave, parent=None):
        super().__init__(parent)
        self.pack()
        self.chave = chave
        self.mostrar_campo()

    def mostrar_campo(self):
        self.rotulo = Label(self, 
            text=self.chave, 
            fg=cf.ORANGE, 
            font=("Arial", 30, "bold")
        )
        self.rotulo.pack(side=TOP, anchor="w", padx=5)
        self.entrada = Entry(
            self,
            font=("Arial", 30, "bold"),
            bd=0,
            highlightthickness=0
        )
        self.entrada.pack(side=BOTTOM, padx=5)

if __name__ == "__main__":
    Campo("Produto").mainloop()
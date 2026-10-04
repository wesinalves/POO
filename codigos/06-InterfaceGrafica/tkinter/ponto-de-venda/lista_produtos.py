from tkinter import *
from tkinter import ttk
import configs as cf

produtos = ["Bermuda", "Short", "Saia", "Camisa", "Calça"]

class ListaProdutos(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(fill=X)
        self.mostrar_campo()

    def mostrar_campo(self):
        
        self.rotulo = Label(self, 
            text="Produtos", 
            fg=cf.ORANGE, 
            font=("Arial", 30, "bold")
        )
        self.rotulo.pack(side=TOP, anchor="w", padx=5)

        self.combo = ttk.Combobox(
            self,
            values=produtos,
            font=("Arial", 29, "normal"),
        )
        self.combo.pack(side=BOTTOM, expand=YES)


if __name__ == "__main__":
    ListaProdutos().mainloop()
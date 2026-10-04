from tkinter import *
from configs import *

class Info(Frame):
    def __init__(self, chave, parent=None):
        super().__init__(parent)
        self.pack(padx=50, pady=50)
        self.chave = chave
        self.mostrar_info()

    def mostrar_info(self):
        self.rotulo = Label(
            self,
            text=self.chave,
            fg=ORANGE,
            font=("Arial", 30, "bold")
        )
        self.rotulo.pack(side=LEFT, padx=5, pady=5)
        self.valor = Label(
            self,
            text="-",
            fg=ORANGE,
            font=("Arial", 30, "normal")
        )
        self.valor.pack(side=LEFT, padx=5, pady=5)

if __name__ == "__main__":
    Info("Total").mainloop()
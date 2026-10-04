"""
Classe personalizada para botão
"""
from tkinter import *
import configs as cf

class Botao(Button):
    def __init__(self, texto, cor, fundo, parent=None, **config):
        super().__init__(
                parent,
                text = texto,
                fg = cor,
                bg = fundo, # não funciona no macOs
                width = 14,
                font=("Arial", 30, "bold"),
                bd=0,
                highlightthickness=0,
                **config,
            )
        self.pack(side=LEFT, padx=5, pady=5) 

if __name__ == "__main__":
    bt = Botao("Meu botão", cf.ORANGE, cf.NAVY)
    print(bt.cget("bg"))
    mainloop()


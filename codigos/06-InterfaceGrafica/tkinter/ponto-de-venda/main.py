from tkinter import *

from botao import Botao
from campo import Campo
from lista_produtos import ListaProdutos
from nota import Nota
from info import Info
from eventos import EventosPontoVenda
from configs import *


class PontoVenda:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1500x900")
        self.window.title("Casas Brasília - Varejo e Atacado")
        self.window.config(padx=20, pady=20, bg=NAVY)

        self.topo = Frame(self.window)
        self.topo.pack(side=TOP)

        self.fundo = Frame(self.window)
        self.fundo.pack(side=BOTTOM, anchor="e")

        self.lateral = Frame(self.window)
        self.lateral.pack(side=LEFT, fill=Y)

        self.centro = Frame(self.window)
        self.centro.pack(side=RIGHT, fill=BOTH, expand=YES)

        self.valor_total = 0
        self.eventos = EventosPontoVenda(self)
        self.criar_interface()

    def criar_interface(self):
        Label(self.topo, 
            text="Ponto de Vendas - Caixa Aberto",
            bg=NAVY, 
            fg=ORANGE, 
            font=("Arial", 30, "bold")
        ).pack()

        ##### Centro da janela
        self.nota = Nota(self.centro)

        ##### Lateral da janela
        self.produto = ListaProdutos(self.lateral)
        self.codigo = Campo("Código Barra", self.lateral)
        self.valor = Campo("Valor", self.lateral)
        self.quant = Campo("Quantidade", self.lateral)
        self.quant.entrada.bind("<Return>", self.eventos.cadastrar_item)
        self.total = Info("Total: ", self.lateral)

        #### Fundo da janela
        bt1 = Botao("Cadastrar Item", ORANGE, ORANGE, self.fundo)
        #bt1.bind("<Return>", self.enter_event)
        bt1.config(command=self.eventos.cadastrar_item)

        bt2 = Botao("Pagar", ORANGE, ORANGE, self.fundo)        


if __name__ == "__main__":
    PontoVenda().window.mainloop()
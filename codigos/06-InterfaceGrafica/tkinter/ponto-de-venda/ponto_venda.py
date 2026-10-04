from tkinter import *
from tkinter import ttk

###################
NAVY = "#253C6D"
WEDDING = "#30497D"
RETRO = "#455B8A"
ORANGE = "#F2842F"

estilo = {
    "bd": 0,
    "highlightthickness": 0,
}

#########################
subtotal = 0
def cadastrar_event():
    global subtotal

    cod = codigo_entry.get()
    desc = descricao_list.get()
    qt = int(quant_entry.get())
    val = float(valor_entry.get())

    text = f"\n[{cod}] {desc}: {qt} {val:.2f} -> {(qt * val):.2f}"
    nota_fiscal.insert("end", text)

    subtotal += qt * val

    subtotal_valor.config(text=str(f"{subtotal:.2f}"))


##########################
window = Tk()
window.geometry("1500x900")
window.title("Casas Brasília - Ponto de venda")
window.config(padx=20, pady=20, bg=NAVY)

label_caixa = Label(text="Caixa Ocupado", bg=ORANGE, foreground=NAVY, font=("Arial", 30, "bold"))
label_caixa.grid(row=0, column=0, padx=5, pady=5)

nota_fiscal = Text(height=17, width=47, **estilo, padx=5, pady=5, font=("Arial", 30, "normal"))
nota_fiscal.insert("1.0", "Casas Brasília")
nota_fiscal.grid(row=1, column=1, rowspan=10, padx=5, pady=5, columnspan=2)

codigo_label = Label(text="Código Barra", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "bold"))
codigo_label.grid(row=1, column=0, sticky="sw", padx=5)

codigo_entry = Entry(font=("Arial", 20, "normal"), **estilo)
codigo_entry.grid(row=2,column=0, sticky="nw", padx=5, pady=5, ipadx=12, ipady=12)

subtotal_label = Label(text="Subtotal:", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "normal"))
subtotal_label.grid(row=0, column=1, sticky="e", padx=5, pady=5)

subtotal_valor = Label(text="00,00", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "bold"))
subtotal_valor.grid(row=0, column=2, sticky="w", padx=5, pady=5)

descricao_label = Label(text="Descrição", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "bold"))
descricao_label.grid(row=3, column=0, sticky="sw", padx=5)

produtos = ["Bermuda", "Short", "Saia", "Camisa", "Calça"]
descricao_list = ttk.Combobox(window, values=produtos, font=("Arial", 19, "normal"))
descricao_list.grid(row=4, column=0, sticky="nw", padx=5, pady=5, ipadx=12, ipady=12)
descricao_list.current(0)

valor_label = Label(text="Valor", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "bold"))
valor_label.grid(row=5, column=0, sticky="sw", padx=5)

valor_entry = Entry(font=("Arial", 20, "normal"), **estilo)
valor_entry.grid(row=6, column=0, sticky="nw", padx=5, pady=5, ipadx=12, ipady=12)

quant_label = Label(text="Quantidade", bg=NAVY, foreground=ORANGE, font=("Arial", 30, "bold"))
quant_label.grid(row=7, column=0, sticky="sw", padx=5)

quant_entry = Entry(font=("Arial", 20, "normal"), **estilo)
quant_entry.grid(row=8, column=0, sticky="nw", padx=5, pady=5, ipadx=12, ipady=12)


insert = Button(text="Cadastrar Item", 
                width=14, 
                foreground=WEDDING,
                bg=ORANGE, 
                **estilo, 
                relief="flat", 
                overrelief="flat",
                font=("Arial", 30, "bold"), 
                command=cadastrar_event)
insert.grid(row=9, column=0, sticky="nw")

pay = Button(text="Pagar", 
                width=14, 
                fg=ORANGE,
                bg=ORANGE, 
                **estilo, 
                relief="flat", 
                overrelief="flat",
                font=("Arial", 30, "bold"), 
                command=cadastrar_event)
pay.grid(row=10, column=0, sticky="nw")


######################################

window.mainloop()
class EventosPontoVenda:
    def __init__(self, app):
        self.app = app

    def cadastrar_item(self, event=None):
        app = self.app

        cod = app.codigo.entrada.get()
        desc = app.produto.combo.get()
        qt = int(app.quant.entrada.get())
        val = float(app.valor.entrada.get())
    
        text = f"\n[{cod}] {desc}: {qt} {val:.2f} -> {(qt * val):.2f}"
        app.nota.insert("end", text)
        app.valor_total += qt * val
        app.total.valor.config(text=str(f"{app.valor_total:.2f}"))    
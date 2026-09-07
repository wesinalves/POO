class Estudante:
    def __init__(self, nome, matricula, email):
        self._nome = nome,
        self._matricula = matricula
        self.__email = email
        self._falta = 0
        self._mencao = None

    @property
    def email(self):
        return self.__email

    def marcar_falta(self):
        self._falta += 1
        return self._falta

    def atribuir_mencao(self, valor) -> str:
        if valor < 0 or valor > 10:
            return "Valor da nota não é permitido"
        if valor > 9:
            self._mencao = "EX"
        elif valor > 7:
            self._mencao = "BOM"
        elif valor > 5:
            self._mencao = "REG"
        elif valor > 3:
            self._mencao = "REC"
        else:
            self._mencao = "REP"

        return self._mencao

    def registar_participacao(self, valor):
        if valor < 1 or valor > 5:
            print("Insira um valor de 1 a 5")
            return
        self._participacao = valor


class EstudanteEnsinoMedio(Estudante):
    def __init__(self, nome, matricula, email, serie):
        super().__init__(nome, matricula, email)
        self._serie = serie

if __name__ == "__main__":
    e1 = EstudanteEnsinoMedio("Pedro", "001", "pedro@gmail.com", "ano1")
    print(e1.marcar_falta())
    print("-"*10)
    print(e1.email)
    print(e1._nome)
    print(e1._matricula)
    print("-"*10)
    print(e1.atribuir_mencao(-2))
    e1.registar_participacao(0)
    
    
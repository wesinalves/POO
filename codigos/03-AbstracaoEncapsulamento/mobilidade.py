"""
Sistema de micromobilidade urbana
Autor: Wesin Ribeiro

O sistema deve modelar a interação entre os usuários e as bicicletas disponíveis na cidade por meio da troca de mensagens entre os objetos.
Você deverá criar duas classes em Python: Bicicleta e Usuario. Ambas devem seguir as convenções de encapsulamento e visibilidade de atributos.

Implemente as classes Bicicleta e Usuário conforme a descrição da atividade em

/atividades/03-AbstracaoEncapsulamento/Sistema de micromobilidade.pdf

"""

class Bicicleta:
    def __init__(self, codigo, modelo, carga_bateria, disponivel):
        self._codigo = codigo
        self._modelo = modelo
        self.carga_bateria = carga_bateria
        self._disponivel = disponivel

    @property
    def carga_bateria(self):
        return self._carga_bateria

    @carga_bateria.setter
    def carga_bateria(self, valor: float):
        if 0 <= valor <= 100:
            self._carga_bateria = valor
        else:
            print("Valor não permitido")

    def usar(self, minutos: float):
        consumo = minutos * 0.5
        self.carga_bateria = self.carga_bateria - consumo
        if self.carga_bateria <= 0:
            self._disponivel = False
            self.carga_bateria = 0

    def recarregar(self):
        self.carga_bateria = 100
        self._disponivel = True

    def autonomia_estimada(self):
        autonomia = self.carga_bateria * 0.8 # em KM
        return autonomia

    def __str__(self):
        return f"{self._codigo}, {self.carga_bateria}"


class Usuario:
    def __init__(self, nome, saldo, bike_alugada, viagens_realizadas):
        self._nome = nome
        self._saldo = saldo
        self._bike_alugada = bike_alugada
        self._viagens_realizadas = viagens_realizadas

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            return "Informe um valor positivo!"
        self._saldo = valor

    def adicionar_saldo(self, valor: float):
        self.saldo = valor

    def alugar_bike(self, bike: Bicicleta) -> str:
        if self._bike_alugada is not None:
            return "Usuário já possui bike alugada"
        if self.saldo < 5.0:
            return "Saldo insuficiente"
        if bike.carga_bateria < 10.0:
            return "Bateria insuficiente"

        self._bike_alugada = bike
        bike._disponivel = False
        return "Bike alugada com sucesso!"

    def devolver_bike(self, tempo_uso): # tempo em minutos 
        custo = tempo_uso * 0.40
        self.saldo = self.saldo - custo
        self._bike_alugada._disponivel = True
        self._bike_alugada.usar(tempo_uso)
        self._bike_alugada = None
        self._viagens_realizadas += 1

    def __str__(self):
        return f"{self._nome}, {self.saldo}"


if __name__ == "__main__":
    # Criando as instâncias
    bike_eletrica = Bicicleta(codigo="BK-100", modelo="Urbana", carga_bateria=90.0, disponivel=True)
    cliente = Usuario(nome="Pedro", saldo=20.00, bike_alugada=None, viagens_realizadas=0)

    # Demonstração de uso e mensagens entre objetos
    print(bike_eletrica)
    cliente.alugar_bike(bike_eletrica)
    cliente.devolver_bike(tempo_uso=30)

    print(cliente)
    print(bike_eletrica)
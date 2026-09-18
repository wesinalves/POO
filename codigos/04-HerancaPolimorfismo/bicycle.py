class Veiculo:
    """Veiculo"""
    nome = "Veiculo"
    def __init__(self, marca):
        self._marca = marca


class DuasRodas(Veiculo):
    def __init__(self, marca, motor):
        super().__init__(marca)
        self._motor = motor

class Bicicleta(DuasRodas):
    def __init__(self, marca, cor):
        super().__init__(marca, motor=False)
        self._cor = cor


bike = Bicicleta("caloi", "vermelha")
print(dir(bike.__class__))
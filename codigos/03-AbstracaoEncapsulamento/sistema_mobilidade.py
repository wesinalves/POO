# -*- coding: utf-8 -*-
"""
Módulo contendo as classes Bicicleta e Usuario para o sistema de Bike-Sharing.
Implementado conforme os princípios de POO e encapsulamento em Python.
"""

class Bicicleta:
    def __init__(self, codigo: str, modelo: str, carga_bateria: float = 100.0, disponivel: bool = True):
        self._codigo = codigo
        self._modelo = modelo
        self.carga_bateria = float(carga_bateria)
        self._disponivel = disponivel

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def carga_bateria(self) -> float:
        return self._carga_bateria

    @carga_bateria.setter
    def carga_bateria(self, valor: float):
        # Validação rígida de limites de bateria (0 a 100)
        if 0.0 <= valor <= 100.0:
            self._carga_bateria = float(valor)
            print("setando carga da bateria")
        else:
            raise ValueError("A carga da bateria deve estar estritamente entre 0.0 e 100.0.")

    @property
    def disponivel(self) -> bool:
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor: bool):
        self._disponivel = bool(valor)

    def usar(self, minutos: float):
        """Reduz a bateria proporcionalmente ao tempo de uso (0.5% por minuto)"""
        consumo = minutos * 0.5
        self.carga_bateria = max(0.0, self._carga_bateria - consumo)  # Usa o setter para validar
        if self._carga_bateria == 0.0:
            self._disponivel = False

    def recarregar(self):
        """Eleva a bateria para 100% e redefine como disponível"""
        self.carga_bateria = 100.0
        self._disponivel = True

    def autonomia_estimada(self) -> float:
        """Estima a autonomia com base no consumo médio (1% = 0.8 km)"""
        return self._carga_bateria * 0.8

    def __str__(self) -> str:
        status = "Disponível" if self._disponivel else "Indisponível"
        return f"Bicicleta {self._codigo} ({self._modelo}) - Bateria: {self._carga_bateria}% - Status: {status}"


class Usuario:
    def __init__(self, nome: str, saldo: float = 0.0):
        self._nome = nome
        self._saldo = max(0.0, float(saldo))  # Usa lógica condicional para evitar saldo negativo inicial
        self._bike_alugada = None
        self._viagens_realizadas = 0

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        # Impede que alterações definam saldo negativo usando lógica condicional
        if valor < 0.0:
            self._saldo = 0.0
        else:
            self._saldo = float(valor)

    @property
    def bike_alugada(self) -> Bicicleta:
        return self._bike_alugada

    @property
    def viagens_realizadas(self) -> int:
        return self._viagens_realizadas

    def adicionar_saldo(self, valor: float):
        """Incrementa o saldo se for um valor positivo"""
        if valor < 0.0:
            raise ValueError("O valor de depósito não pode ser negativo.")
        self.saldo += valor  # Usa o setter

    def alugar_bike(self, bike: Bicicleta) -> str:
        """Aluga uma bike atendendo a todas as restrições de negócio"""
        if self._bike_alugada is not None:
            return "Erro: Usuário já possui uma bicicleta alugada."
        if self._saldo < 5.0:
            return "Erro: Saldo mínimo de R$ 5,00 necessário para aluguel."
        if not bike.disponivel:
            return "Erro: Bicicleta não está disponível."
        if bike.carga_bateria <= 10.0:
            return "Erro: Carga de bateria insuficiente (mínimo de 10%)."

        # Conclui aluguel
        self._bike_alugada = bike
        bike.disponivel = False
        return "Aluguel realizado com sucesso!"

    def devolver_bike(self, tempo_uso: float) -> str:
        """Devolve a bike, calcula tarifas e atualiza estados"""
        if self._bike_alugada is None:
            return "Erro: Nenhuma bicicleta alugada para devolver."

        custo = tempo_uso * 0.40
        self.saldo -= custo  # Setter garante que o saldo não fique negativo (fica 0.0 se estourar)
        
        bike = self._bike_alugada
        bike.usar(tempo_uso)  # Atualiza estado da bateria e disponibilidade
        
        # Desassocia se a bike ainda tiver alguma bateria ou se o uso foi concluído
        self._bike_alugada = None
        self._viagens_realizadas += 1
        
        # Se a bateria zerou, ela fica indisponível. Caso contrário, volta a ficar disponível.
        if bike.carga_bateria > 0.0:
            bike.disponivel = True
            
        return f"Devolução realizada! Custo da corrida: R$ {custo:.2f}. Saldo restante: R$ {self.saldo:.2f}."

    def __str__(self) -> str:
        bike_status = self._bike_alugada.codigo if self._bike_alugada else "Nenhuma"
        return f"Usuário: {self._nome} | Saldo: R$ {self._saldo:.2f} | Bike Alugada: {bike_status} | Viagens: {self._viagens_realizadas}"

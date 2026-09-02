"""
Sistema de micromobilidade urbana
Autor: Wesin Ribeiro

O sistema deve modelar a interação entre os usuários e as bicicletas disponíveis na cidade por meio da troca de mensagens entre os objetos.
Você deverá criar duas classes em Python: Bicicleta e Usuario. Ambas devem seguir as convenções de encapsulamento e visibilidade de atributos.

Implemente as classes Bicicleta e Usuário conforme a descrição da atividade em

/atividades/03-AbstracaoEncapsulamento/Sistema de micromobilidade.pdf

"""

class Bicicleta:
    pass

class Usuario:
    pass

if __name__ == "__main__":
    # Criando as instâncias
    bike_eletrica = Bicicleta(codigo="BK-100", modelo="Urbana", carga_bateria=90.0, disponivel=True)
    cliente = Usuario(nome="Pedro", saldo=20.00, bike_alugada=None, viagens_realizadas=0)

    # Demonstração de uso e mensagens entre objetos
    print(bike_eletrica)
    cliente.alugar_bike(bike_eletrica)
    cliente.devolver_bike(minutos_uso=30)

    print(cliente)
    print(bike_eletrica)
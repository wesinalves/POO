"""
Programa para calcular valor decimal a partir do valor binário
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 08/08/2026
"""
numero = int(input('Entre com o numero binário: '))
decimal = 0

n = 0
while numero != 0:
    digito = numero % 2
    decimal = decimal + (digito * 2**n)
    numero = numero // 10
    n = n + 1

print(decimal)
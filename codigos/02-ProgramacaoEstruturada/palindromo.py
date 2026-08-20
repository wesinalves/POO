"""
Programa para detectar números palíndromos
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 08/08/2026
"""
numero = int(input('Entre com o numero: '))
decimal = 0
digito = []

n = 0
while n < 5:
    digito.append(numero % 10)  
    numero = numero // 10
    n = n + 1


if digito[0] == digito[4] and digito[1] == digito[3]:
    print("Palindromo detectado!")
else:
    print('Palindromo NAO detectado!')
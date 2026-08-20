"""
Programa para calcular diametro e área da circunferência
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 08/08/2026
"""
PI = 3.14159

raio = int(input('Forneça o valor do raio: '))

diametro = 2*PI*raio
area = PI*raio*raio

print(diametro)
print(area)
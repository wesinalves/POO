"""
Programa para calcular fatorial de um número
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 08/08/2026
"""
#a
N = int(input('entre com o valor de N: '))

fatorial = 1
for n in range(N+1,1,-1):
    fatorial = fatorial * (n - 1)

print(fatorial)

#b
e = 1
termos = 0
for i in range(10,0, -1):
    fatorial = 1
    for n in range(i+1,1,-1):
        fatorial = fatorial * (n - 1)
    termos = termos + (1 / fatorial)

e += termos
print('valor de e:', e)

#c
ex = 1
termos = 0
x = int(input('entre com o valor de x: '))
for i in range(10, 0, -1):
    fatorial = 1
    for n in range(i+1,1,-1):
        fatorial = fatorial * (n - 1)
    termos = termos + (x**i / fatorial)

ex += termos
print('Valor de ex:', ex)
    


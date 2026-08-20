"""
Programa para calcular numeros primos
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 13/08/20226
"""
from math import sqrt

# a) escreva função
def numero_primo_n(num: int)->bool:
    # divisivel por 1 e por ele mesmo
    primo = True
    limite = (num//2) + 1
    for i in range(2,limite):
        if num % i == 0:
            primo = False
            break
    return primo

# c) verificar limite superior n/2 e sqrt(n).
def numero_primo_r(num: int)->bool:
    # divisivel por 1 e por ele mesmo
    primo = True
    limite = int(sqrt(num)) + 1
    for i in range(2,limite):
        if num % i == 0:
            primo = False
            break
    return primo
            

if __name__ == '__main__':  
    # b) imprime numeros primos entre 2 e 1000
    count = 0
    for i in range(2,1001):
        if numero_primo_r(i):
            print(i, end=" ")
            count += 1

    print()
    print(count)
    
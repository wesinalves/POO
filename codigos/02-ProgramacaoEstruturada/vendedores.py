"""
Programa para calcular total de vendas
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 10/08/20226
"""

# use listas de listas
# vendedores 1 - 3
# produtos 1 - 4
# recibo: 1,2,7 (vendedor, produto, quantidade)

# ler informações e resuma total de vendas por vendedor e por produto

# Matriz de vendas (coluna - vendedor)

# totais cruzados à direita das linhas

# na parte inferior das colunas totalizadas

matriz = [
    [1,3,5],
    [2,4,8],
    [4,6,7],
    [9,5,5]
]
col1 = 0
col2 = 0
col3 = 0

print('   V1| V2| V3| VT')
for i in range(4):
    print(f'P{i}', end=" ")
    sumrow = 0
    for j in range(3):
        print(matriz[i][j], end=" | ")
        sumrow += matriz[i][j]
        if j == 0:
            col1 += matriz[i][j]
        elif j == 1:
            col2 += matriz[i][j]
        elif j == 2:
            col3 += matriz[i][j]
    print(sumrow)

print(f'PT {col1}| {col2}| {col3}|')
"""
Programa para converter KM -> ML
Autor: Wesin Ribeiro
Disciplina: Programação orientada a objetos
Data: 08/08/2026
---------------------------------------------------------------------------
In this exercise you should convert kilometres to miles.
We will add several new tests to your program:
1. Verify that the user has entered a positive distance (i.e. they cannot enter a negative number).
2. Verify that the input is a number; if it is not a number then do nothing; otherwise convert the distance to miles.
To check to see if a string contains only digits use the method isnumeric()
for example '42'.isnumeric(); which returns True if the string only con-
tains numbers. 
Note this method only works for positive integers; but this is sufcient for this example.
"""
while True:
    kilometers = input('Entre com a distancia em KM: ')

    if kilometers[0] == '-':
        print('Entre com um valor positivo!')
        break

    if kilometers.isnumeric() == False:
        print('Entre com um valor numérico!')
        break

    if kilometers == 'sair':
        break

    # converte km to miles
    miles = float(kilometers) / 1.609

    print(f"{float(kilometers):.2f}KM -> {miles:.2f} ML")

    


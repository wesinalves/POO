lista = [1]*1000

for i in range(2,1000):
    resto = i + 1
    for j in range(resto, 1000):
        if j % i == 0:
            lista[j] = 0

count = 0
for i in range(2,999):
    if lista[i] == 1:
        print(i, end=" ")
        count += 1

print("\n", count)
for i in range(10,0,-1):
    print("* "*i)


print("*")

contador = -1
for i in range(10,0,-1):
    if i == 10:
        print("* "*i)
    else:
        print(" "*contador, "* "*i)
    contador += 2
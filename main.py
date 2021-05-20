numeros_positivos = int(0)
cont = int(0)

while (cont < 6):
    numero = float(input())
    if (numero > 0):
        numeros_positivos = numeros_positivos + 1
    cont = cont + 1

print("{} valores positivos".format(numeros_positivos))
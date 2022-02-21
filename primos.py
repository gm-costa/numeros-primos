# Crivo de Eratóstenes
import os
from time import time

os.system("clear") or None  # limpa console

num_maximo = int(input("Mostrar os números primos de 1 até: "))

inicio = time()

valor_limite = int(num_maximo**0.5)

lista = [i for i in range(2, num_maximo + 1)]

primos = []

while True:
    if lista[0] > valor_limite:
        break
    primos.append(lista[0])

    lista = [x for x in lista if ((x % lista[0]) != 0)]

primos += lista

fim = time()

print(f"\nNúmeros primos até {num_maximo}:\n\n{primos}")
print(f"\nQuantidade de números primos até {num_maximo}: {len(primos)}")
print(f"\nTempo gasto: {fim - inicio}")

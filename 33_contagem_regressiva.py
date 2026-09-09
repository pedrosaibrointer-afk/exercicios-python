# Exercício 33: Crie um programa que realiza a contagem regressiva de 20 segundos

import time

print("Contagem regressiva de 20 segundos:")
for i in range(20, -1, -1):
    print(i)
    time.sleep(1)
print("Tempo acabou!")
